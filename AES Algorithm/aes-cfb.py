from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

# Khóa và vectơ khởi tạo (IV)
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Đường dẫn tệp cần mã hóa
file_path = 'plaintext.txt'

# Đường dẫn tệp được mã hóa
encrypted_file_path = 'ciphertext.txt'

# Đọc nội dung của tệp cần mã hoá
with open(file_path, 'rb') as file:
    plaintext = file.read()

# Khởi tạo đối tượng AES với chế độ CFB
cipher = AES.new(key, AES.MODE_CFB, iv)

# Mã hóa nội dung tệp
encrypted_data = cipher.encrypt(pad(plaintext, AES.block_size))

# Mã hóa dữ liệu thành chuỗi
encrypted_data_string = base64.b64encode(encrypted_data).decode('utf-8')

# Ghi dữ liệu mã hóa vào tệp mới dưới dạng chuỗi
with open(encrypted_file_path, 'w') as encrypted_file:
    encrypted_file.write(encrypted_data_string)
