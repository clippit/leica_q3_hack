#pragma description Firmware of many Panasonic and Leica cameras
#pragma endian little

import type.magic;
import type.size;

bitfield FirmwareVersion {
    minor: 4;
    patch: 4;
    u8 major;
} [[format("version_format")]];

enum StorageType : u32 {
    TYPE1 = 0x02,
    TYPE2 = 0x03,
};

struct BuildDateTime {
    u8 minute;
    u8 hour;
    u8 day;
    u8 month;
} [[sealed, format("build_datetime_format")]];

struct FileHeader {
    type::Magic<"UPD\x00\x00\x02\x00\x00\x00\x02\x00\x00"> magic;
    char device_codename[16] [[format("string_format")]];
    
    FirmwareVersion version;
    FirmwareVersion version_dup;

    u16 unknown_1[2];
    BuildDateTime build_datetime;
    u32 unknown_2[4];

    u32 section_header_offset;
    type::Size32 sections_size;
};

struct Section {
    char name[12];
    u32 data_offset;
    type::Size32 data_size;
    u32 unknown_offset;
    StorageType storage_type;
    u8 sha256[32] [[sealed, format("hash_format")]];
    
    match (storage_type) {
        (StorageType::TYPE1): padding[16];
        (StorageType::TYPE2): u8 unknown2[16] [[sealed, format("hash_format")]];
    }
    
    std::mem::Bytes<data_size> data @(parent.file_header_dup.section_header_offset + data_offset) [[ single_color, name(std::format("DATA<{}>", name))]];
} [[fixed_size(92), name(std::format("{}", name)), comment(std::format("{} {}bytes", storage_type, data_size))]];

struct SectionHeader {
    char identifier[16] [[format("string_format")]];
    padding[16];
    u8 maybe_checksum[64] [[sealed, format("hash_format")]];
    padding[64];
    FileHeader file_header_dup;
    u32 section_header_size;
    type::Size32 section_data_size;
    u32 section_number;
    Section section_list[section_number];
};

fn hash_format(auto bytes) {
    str hash_hex;
    for(u8 i=0, i < sizeof(bytes), i+=1) {
        hash_hex = hash_hex + std::format("{:02X}",bytes[i]);
    }
    return hash_hex;
};

fn string_format(auto bytes) {
    return std::format("{}", bytes);
};

fn version_format(auto ver) {
    return std::format("{}.{}.{}", ver.major, ver.minor, ver.patch);
};

fn build_datetime_format(auto dt) {
    return std::format("{:02x}-{:02x} {:02x}:{:02x}", dt.month, dt.day, dt.hour, dt.minute);
};


FileHeader file_header @0x00;
u32 maybe_checksum @$;
SectionHeader section_header @file_header.section_header_offset;