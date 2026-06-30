a = 6
result = "là số chẵn" if a%2 ==0 else "là số lẻ"
print(f"{a} {result}")
print(f"{a} { "Là số dương" if a > 0 else "Là số âm"}")
b = 7
c = 9
max_value = b if b>c else c
print(f"Số lớn nhất giữa {b} và {c} là {max_value}")
is_logged_in = False
print(f"Chào mừng, {"Thành viên" if is_logged_in else "Khách hàng"}")