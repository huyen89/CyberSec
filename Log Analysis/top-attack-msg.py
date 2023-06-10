# Import function module
import core_function

# Lưu địa chỉ file log vào file_path
file_path = 'modsec_debug.log'
# Pattern của biểu thức chính quy tìm kiếm [msg "..."] trong file log
pattern = r'\[msg\s+"(.*?)[\(|"\]|\:]'

# Khởi tạo biến lưu trữ các msg
msgs = core_function.find_pattern_in_line(file_path,pattern)

# Generate the attack report
core_function.generate_attack_report(msgs,"Most Common Attacks","most-common-attacks.png")
