# ==========================================
# HỌC VỀ FORMAT SPECIFIERS TRONG PYTHON (f-string)
# Cú pháp chung: {value:flags}
# ==========================================

val_float = 3.14159
val_int = 42
val_pos = 123
val_neg = -123
text = "Python"

print("--- 1. Định dạng số thập phân: .(number)f ---")
# Làm tròn đến số chữ số thập phân chỉ định (Fixed point)
print(f"Mặc định: {val_float}")
print(f"Làm tròn 2 chữ số: {val_float:.2f}")
print(f"Làm tròn 0 chữ số: {val_float:.0f}")
print()

print("--- 2. Cấp phát khoảng trống: :(number) ---")
# Cấp phát một số lượng khoảng trống nhất định cho chuỗi/số
print(f"Cấp phát 10 khoảng trống: [{val_int:10}]")
print(f"Cấp phát 10 khoảng trống cho chữ: [{text:10}]")
print()

print("--- 3. Thêm số 0 phía trước: :03 ---")
# Cấp phát khoảng trống và tự động điền thêm số 0 vào các chỗ trống phía trước
print(f"Độ dài 3, điền số 0: {val_int:03}")
print(f"Độ dài 5, điền số 0: {val_int:05}")
print()

print("--- 4. Căn lề: :< , :> , :^ ---")
# :< lùi trái, :> lùi phải, :^ căn giữa (thường kết hợp với số lượng khoảng trống)
print(f"Lùi trái  (10 khoảng trống): [{text:<10}]")
print(f"Lùi phải  (10 khoảng trống): [{text:>10}]")
print(f"Căn giữa  (10 khoảng trống): [{text:^10}]")
print()

print("--- 5. Hiển thị dấu cộng số dương: :+ ---")
# Luôn hiển thị dấu + cho số dương (số âm mặc định luôn có dấu -)
print(f"Số dương có dấu: {val_pos:+}")
print(f"Số âm vẫn có dấu: {val_neg:+}")
print()

print("--- 6. Đặt dấu ở vị trí ngoài cùng bên trái: := ---")
# Đặt dấu cộng/trừ ở rìa trái của khoảng trống đã cấp phát
print(f"Mặc định khi cấp phát 8 khoảng trống: [{val_neg:8}]")
print(f"Dấu đẩy sang trái cùng với ':=':      [{val_neg:=8}]")
print(f"Kết hợp dấu '+' và '=':              [{val_pos:+=8}]")
print()

print("--- 7. Thêm khoảng trắng trước số dương: :  ---")
# Thêm một khoảng trắng trước số dương để nó thẳng hàng với các số âm có dấu trừ
print(f"Số dương (có khoảng trống): [{val_pos: }]")
print(f"Số âm (giữ nguyên dấu -):   [{val_neg: }]")
print()

print("--- 8. Dấu phẩy phân tách phần ngàn: :, ---")
# Thêm dấu phẩy cho các số lớn để dễ đọc
big_number = 1000000
print(f"Số lớn mặc định: {big_number}")
print(f"Có dấu phân tách: {big_number:,}")
print()

print("--- BONUS: Kết hợp nhiều flags cùng lúc ---")
# Bạn có thể kết hợp: căn lề, dấu, độ rộng, dấu phẩy và làm tròn thập phân
money = 12345.6789
print(f"Kết hợp phức tạp: Mức lương của bạn là [{money:>+15,.2f}]")
# Ý nghĩa: Căn phải (>), hiện dấu dương (+), rộng 15 ô, có dấu phẩy (,), làm tròn 2 số thập phân (.2f)