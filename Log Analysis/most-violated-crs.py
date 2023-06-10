import core_function

# Lưu địa chỉ file log vào file_path
file_path = 'modsec_debug.log'
# Pattern của biểu thức chính quy tìm kiếm các rule trong CRS trong file log
pattern = r'\[file\s\"/etc/apache2/modsecurity-crs/coreruleset-3.3.0/rules/(.*?).conf\"\]'

confFiles = core_function.find_pattern_in_line(file_path,pattern)

# Generate the attack report
core_function.generate_attack_report(confFiles,3,"Most Violated Rules","most-violated-crs.png")
