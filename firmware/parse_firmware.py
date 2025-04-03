#!/usr/bin/env python3
import os
import sys
import csv
import struct

def parse_firmware(filename):
    # Read the entire binary file.
    with open(filename, "rb") as f:
        data = f.read()

    # --- Parse FileHeader (offset 0, 64 bytes) ---
    # FileHeader layout:
    #   magic:           12 bytes
    #   device_codename: 16 bytes
    #   version:         2 bytes (first byte packs minor & patch, second is major)
    #   version_dup:     2 bytes
    #   unknown_1:       2 x 2 bytes = 4 bytes
    #   build_datetime:  4 bytes (minute, hour, day, month)
    #   unknown_2:       4 x 4 bytes = 16 bytes
    #   section_header_offset: 4 bytes
    #   sections_size:         4 bytes
    file_header_fmt = "<12s16s2s2sHH4B4I2I"
    file_header_size = struct.calcsize(file_header_fmt)  # should be 64 bytes
    file_header_data = data[0:file_header_size]
    file_header = struct.unpack(file_header_fmt, file_header_data)
    # The section_header_offset is the second-to-last field.
    section_header_offset = file_header[-2]

    # --- Parse SectionHeader (located at file_header.section_header_offset) ---
    # SectionHeader fixed part (236 bytes) layout:
    #   identifier:      16 bytes
    #   padding:         16 bytes
    #   maybe_checksum:  64 bytes
    #   padding:         64 bytes
    #   file_header_dup: FileHeader (64 bytes, same format as above)
    #   section_header_size: 4 bytes
    #   section_data_size:   4 bytes
    #   section_number:      4 bytes
    #
    # We build a combined format string. Note that file_header_dup uses the same format as above.
    section_header_fmt = "<16s16s64s64s" + "12s16s2s2sHH4B4I2I" + "III"
    section_header_size = struct.calcsize(section_header_fmt)  # should be 236 bytes
    sh_data = data[section_header_offset: section_header_offset + section_header_size]
    sh = struct.unpack(section_header_fmt, sh_data)
    # The file_header_dup is embedded starting at index 4 (after the first 4 fields)
    # Its fields (according to our file_header_fmt) are:
    #   [file_header_magic, device_codename, version, version_dup, unknown1_0, unknown1_1,
    #    build_datetime_min, build_datetime_hour, build_datetime_day, build_datetime_month,
    #    unknown2_0, unknown2_1, unknown2_2, unknown2_3, section_header_offset_dup, sections_size_dup]
    # We need the duplicated section_header_offset (used as the base for section data)
    # This field is at index 18 (0-based) in our unpacked tuple.
    file_header_dup_section_header_offset = sh[18]
    # The last three fields of the SectionHeader are:
    #   section_header_size, section_data_size, section_number.
    section_number = sh[22]

    # --- Parse the Section List ---
    # Each Section entry is fixed at 92 bytes with the following layout:
    #   name:         12 bytes
    #   data_offset:   4 bytes (unsigned int)
    #   data_size:     4 bytes (unsigned int)
    #   unknown_offset:4 bytes (unsigned int)
    #   storage_type:  4 bytes (unsigned int; 0x02 for TYPE2, 0x03 for TYPE3)
    #   sha256:       32 bytes
    #   match block: 16 bytes (if storage_type==TYPE3 this is unknown2; otherwise padding)
    #   reserved:     16 bytes (padding/reserved)
    section_entry_size = 92
    section_list_offset = section_header_offset + section_header_size
    sections = []

    section_fmt = "<12sIIII32s16s16s"  # total 92 bytes
    for i in range(section_number):
        offset = section_list_offset + i * section_entry_size
        sec_data = data[offset: offset + section_entry_size]
        (name_raw, data_offset_field, data_size, unknown_offset,
         storage_type, sha256_bytes, match_field, reserved) = struct.unpack(section_fmt, sec_data)
        # Process the section name (strip null bytes)
        name = name_raw.split(b'\x00', 1)[0].decode('ascii', errors='ignore')
        sha256_hex = sha256_bytes.hex().upper()
        # Determine storage type and, if TYPE3, extract unknown2
        if storage_type == 0x03:  # TYPE3
            storage_type_str = "TYPE3"
            unknown2_hex = match_field.hex().upper()
        elif storage_type == 0x02:
            storage_type_str = "TYPE2"
            unknown2_hex = ""
        else:
            storage_type_str = f"UNKNOWN(0x{storage_type:08X})"
            unknown2_hex = ""
        sections.append({
            "name": name,
            "data_offset": data_offset_field,
            "data_size": data_size,
            "storage_type": storage_type_str,
            "sha256": sha256_hex,
            "unknown2": unknown2_hex,
        })

    # --- Extract Section Data ---
    # The actual section data is located at:
    #   base_offset = file_header_dup.section_header_offset (from the duplicated file header)
    # plus each section's data_offset.
    base_offset = file_header_dup_section_header_offset

    # Create the "extracted" folder if it doesn't exist.
    extracted_folder = "extracted"
    if not os.path.exists(extracted_folder):
        os.makedirs(extracted_folder)

    for sec in sections:
        actual_offset = base_offset + sec["data_offset"]
        sec_data = data[actual_offset: actual_offset + sec["data_size"]]
        # Construct a filename (here we add a ".bin" extension)
        out_filename = os.path.join(extracted_folder, sec["name"] + ".bin")
        with open(out_filename, "wb") as outf:
            outf.write(sec_data)

    # --- Write CSV File ---
    # The CSV will include: name, size, storage_type, hash, and unknown2 (if exists)
    with open("sections.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "size", "storage_type", "hash", "unknown2"])
        for sec in sections:
            writer.writerow([sec["name"], sec["data_size"], sec["storage_type"], sec["sha256"], sec["unknown2"]])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_firmware.py <firmware_file>")
        sys.exit(1)
    firmware_file = sys.argv[1]
    parse_firmware(firmware_file)
    print("Parsing complete. CSV written to 'sections.csv' and section data extracted into the 'extracted' folder.")
