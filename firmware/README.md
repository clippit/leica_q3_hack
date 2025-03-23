# Tools

* [LeicaPanasonicCameraFirmware.hexpat](./LeicaPanasonicCameraFirmware.hexpat): [ImHex](https://imhex.werwolv.net/) Pattern for the firmware file. Leica and Panasonic share the same firmware format. However, Panasonic Lumix firmwares are not XOR-obscured.
* [xor_decrypt.py](./xor_decrypt.py): Utility for XOR

# Leica Q3 firmware Analysis

* File name: Q3___300.lfu
* File size: 211,516,416 bytes

The whole file is XORed with `0xFF`.

## File Header (512 bytes)

```
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
00000000  55 50 44 00 00 02 00 00  00 02 00 00 44 43 31 32  UPD.........DC12
00000010  33 31 00 00 00 00 00 00  00 00 00 00 00 03 00 03  31..............
00000020  04 00 01 00 42 13 07 11  00 00 00 00 03 00 00 00  ....B...........
00000030  00 00 00 00 03 00 00 00  00 02 00 00 00 7A 9B 0C  .............z..
00000040  1C 2E 35 5F 00 00 00 00  00 00 00 00 00 00 00 00  ..5_............
```

* Magic number: 50 50 44 ‘UPD’
* “DC1231”: maybe device codename
* 00 03: version number 3.0.0
* 42 13 07 11: 11/07 13:42???
* 00 02 00 00: size of file header (512 bytes)
* 00 7A 9B 0C: file size excluding this header (211515904 bytes)
* 1C 2E 35 5F: checksum?


## Section Header (5632 bytes)

```
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
00000200  6C 65 69 63 61 00 00 00  00 00 00 00 00 00 00 00  leica...........
00000210  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00000220  13 CA C0 3B 89 E9 40 6D  11 E0 D4 C5 32 17 82 8F  ...;..@m....2...
00000230  91 B6 A8 5B 5C A8 9B 0A  A8 A0 F0 F8 57 BF 6E EA  ...[\.......W.n.
00000240  7F 41 61 D1 5F 7E 53 D8  A0 48 A9 5A 2D 4D 2F FA  .Aa._~S..H.Z-M/.
00000250  AD 1E 5E F3 9F DF 42 EC  C5 A7 9F 33 3D A0 23 89  ..^...B....3=.#.
00000260  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00000270  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00000280  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
00000290  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
000002A0  55 50 44 00 00 02 00 00  00 02 00 00 44 43 31 32  UPD.........DC12
000002B0  33 31 00 00 00 00 00 00  00 00 00 00 00 03 00 03  31..............
000002C0  04 00 01 00 42 13 07 11  00 00 00 00 03 00 00 00  ....B...........
000002D0  00 00 00 00 03 00 00 00  00 02 00 00 00 7A 9B 0C  .............z..
000002E0  00 16 00 00 00 64 9B 0C  38 00 00 00              .....d..8...
```

* 0x200 - 0x21F (23 bytes): only a “leica” string
* 0x220 - 0x25F (64 bytes): maybe a checksum
* 0x260 - 0x29F (64 bytes): padding with 0x00
* 0x2A0 - 0x2DF (64 bytes): identical with the file header
* 0x2E0: section header size (5632 bytes)
* 0x2E4: size of the section data (211510272 bytes)
* 0x2E8: number of sections (56)

### Sections metadata (each 92 bytes)

```
Hex View  00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
 
00000340                           6C 6F 61 64 65 72 31 00          loader1.
00000350  00 00 00 00 00 16 00 00  00 00 02 00 00 00 00 00  ................
00000360  03 00 00 00 A2 DE E6 A9  79 24 6F 16 22 3A BA 58  ........y$o.":.X
00000370  6C 18 28 3B C1 66 10 99  8B 0E 25 B0 C1 37 6C ED  l.(;.f....%..7l.
00000380  A3 82 D6 60 F5 2F 8D E8  A9 D8 AE D6 5D 2F 0C 9F  ...`./......]/..
00000390  1B 3B 9B 16 00 00 00 00  00 00 00 00 00 00 00 00  .;..............
000003A0  00 00 00 00                                      ....
```

* 0x348 - 0x353: section name
* 0x354: data offset from the section header
* 0x358: section data size
* 0x35C: maybe another offset
* 0x360: storage type, values can be 2 or 3
* 0x364 - 0x383: SHA256 checksum if the storage type is 2
* 0x384 - 0x393: unknown data for storage type 3, maybe an IV for decryption 

For storage type 3, the SHA256 is mismatch. One potential reason is that the hash is calculated after decryption.


### All section names (56 in total)

```
boot
loader1
loader2
loader3
storage
program
postboot1_r
postboot2_r
postboot3_r
postboot4_r
postboot5_r
postboot1_r
postboot3_r
postboot5_r
eep_ow_a
eep_ow_b
eep_adj
eep_fix
eep_act_a
eep_act_b
eep_exp_a
eep_exp_b
history
lens_hist
music
osdover
osddata
wifi_info
menu_save
kizu_data
vkizu_data
usbcharge
hm_c_prog
hm_d_prog
hm_c_ddr
hm_d_ddr
hm_d_nw
hm_d_nw_sng
hr_c_prog
hr_d_prog
hr_c_ddr
pzm_data
lns_micon
lns_micon_e
xtk
lut_data
dsp_kizu_c
dsp_kizu_d
bt_info
lpc_data
lpc_code
raw_kizu_c
raw_kizu_d
ext_ver
welcom_fs
mbr_dummy_d
```

## Section Data (from 0x1800)

The section data of storage type 2 is basically empty with 0x00 or 0xff. All other sections are in storage type 3 which are encrypted. The algorithm is unknown.
