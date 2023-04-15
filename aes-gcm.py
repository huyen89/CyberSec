from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import base64


# Tạo ngẫu nhiên key và nonce
key = get_random_bytes(16)
nonce = get_random_bytes(12)

# Đường dẫn tệp cần mã hóa
file_path = 'plaintext.txt'

# Đường dẫn tệp được mã hóa
encrypted_file_path = 'ciphertext.txt'

# Đọc nội dung của tệp cần mã hoá
with open(file_path, 'rb') as file:
    plaintext = file.read()

# Mã hóa dữ liệu với chế độ GCM
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
encrypted_data = cipher.encrypt(plaintext)

# Mã hóa dữ liệu thành chuỗi
encrypted_data_string = base64.b64encode(encrypted_data).decode('utf-8')

# Ghi dữ liệu mã hóa vào tệp mới dưới dạng chuỗi
with open(encrypted_file_path, 'w') as encrypted_file:
    encrypted_file.write(encrypted_data_string)