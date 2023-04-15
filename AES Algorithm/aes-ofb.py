from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
import base64
from Crypto.Random import get_random_bytes

# Khóa và vectơ khởi tạo (IV)
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Đường dẫn tệp cần mã hóa
file_path = 'plaintext.txt'

# Đường dẫn tệp được mã hóa
encrypted_file_path = 'ciphertext.txt'

# Tạo đối tượng AES với chế độ OFB
cipher = AES.new(key, AES.MODE_OFB, iv)

# Đọc nội dung của tệp cần mã hoá
with open(file_path, 'rb') as file:
    plaintext = file.read()

# Tạo đối tượng Counter với IV và giá trị ban đầu là 0
ctr = Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big'))

# Mã hoá dữ liệu
encrypted_data = cipher.encrypt(plaintext)

# Mã hóa dữ liệu thành chuỗi
encrypted_data_string = base64.b64encode(encrypted_data).decode('utf-8')

# Ghi dữ liệu mã hóa vào tệp mới dưới dạng chuỗi
with open(encrypted_file_path, 'w') as encrypted_file:
    encrypted_file.write(encrypted_data_string)