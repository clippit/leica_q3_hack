def xor_decrypt(input_file, output_file, key_byte):
    with open(input_file, "rb") as f:
        data = f.read()

    decrypted_data = bytearray(len(data))

    for i in range(len(data)):
        decrypted_data[i] = data[i] ^ key_byte

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

xor_decrypt("Q3___300.lfu", "Q3___300.xor.lfu", 0xFF)