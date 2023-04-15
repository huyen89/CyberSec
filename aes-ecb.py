from Crypto.Cipher import AES
import os
import base64
from bitarray import bitarray
from Crypto.Random import get_random_bytes

# Đường dẫn tệp cần mã hóa
file_path = 'plaintext.txt'

# Đường dẫn tệp được mã hóa
encrypted_file_path = 'ciphertext.txt'

# Khóa AES
key = get_random_bytes(16)

# Điều chỉnh kích thước khối
block_size = 16

# Tạo đối tượng mã hóa AES
cipher = AES.new(key, AES.MODE_ECB)

# Đọc nội dung tệp
with open(file_path, 'rb') as file:
    data = file.read()

# Điều chỉnh độ dài dữ liệu để đúng kích thước khối
padding_length = block_size - len(data) % block_size
data += bytes([padding_length]) * padding_length

# Mã hóa dữ liệu
encrypted_data = cipher.encrypt(data)

# Mã hóa dữ liệu thành chuỗi
encrypted_data_string = base64.b64encode(encrypted_data).decode('utf-8')

# Ghi dữ liệu mã hóa vào tệp mới dưới dạng chuỗi
with open(encrypted_file_path, 'w') as encrypted_file:
    encrypted_file.write(encrypted_data_string)

# # Chuyển đổi dữ liệu thành chuỗi bit
# ba = bitarray()
# ba.frombytes(encrypted_data)

# # Ghi dữ liệu mã hóa dưới dạng chuỗi bit vào tệp mới
# with open(encrypted_file_path, 'wb') as encrypted_file:
#     ba.tofile(encrypted_file)