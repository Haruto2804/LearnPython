
print("--- 1. IN HÌNH CHỮ NHẬT / HÌNH VUÔNG ---")

# Thêm vòng lặp while để ép người dùng nhập số nguyên dương hợp lệ, tránh bị lỗi crash code
while True:
    try:
        rows = int(input("Nhập số dòng: "))
        cols = int(input("Nhập số cột: "))
        if rows > 0 and cols > 0:
            break
        print("❌ Vui lòng nhập số lớn hơn 0!")
    except ValueError:
        print("❌ Vui lòng nhập một số nguyên hợp lệ!")

symbol = input("Nhập ký tự muốn in ra (Ví dụ: *, @, #): ")
print("\nKẾT QUẢ:")

# Đoạn code gốc rất chuẩn của bạn:
for x in range(rows):
    for y in range(cols):
        print(symbol, end="\t")  # Dùng \t để khoảng cách các cột đều nhau
    print()                      # Hết một dòng thì xuống dòng
print("-" * 40)


# ==============================================================================
# BỔ SUNG 1: IN HÌNH CHỮ NHẬT RỖNG (CHỈ IN VIỀN XUNG QUANH)
# Tư duy: Chỉ in ký tự nếu nằm ở hàng đầu, hàng cuối, cột đầu, hoặc cột cuối.
# ==============================================================================
print("--- 2. BIẾN THỂ: IN HÌNH CHỮ NHẬT RỖNG RUỘT ---")

print("KẾT QUẢ:")
for x in range(rows):
    for y in range(cols):
        # Điều kiện để nằm trên đường viền:
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            print(symbol, end="\t")
        else:
            print(" ", end="\t") # Nếu ở trong ruột thì in khoảng trắng
    print()
print("-" * 40)


# ==============================================================================
# BỔ SUNG 2: IN MA TRẬN TĂNG DẦN (NUMBER MATRIX)
# Không in ký tự cố định nữa, mà ứng dụng vòng lặp để tạo số thứ tự tự động tăng.
# ==============================================================================
print("--- 3. ỨNG DỤNG: IN BẢNG SỐ TỰ ĐỘNG TĂNG ---")

count = 1  # Biến đếm xuất phát từ 1
print("KẾT QUẢ:")
for x in range(rows):
    for y in range(cols):
        # In số hiện tại và định dạng cho thẳng hàng (ví dụ: lấy 2 khoảng trống)
        print(f"{count:02d}", end="\t")
        count += 1 # Sau mỗi lần in thì tăng số lên 1
    print()
print("-" * 40)


# ==============================================================================
# BỔ SUNG 3: TẠO BẢNG CỬU CHƯƠNG (BÀI TOÁN KINH ĐIỂN CỦA NESTED LOOP)
# Trực quan hóa phép nhân bằng ma trận hàng và cột.
# ==============================================================================
print("--- 4. ỨNG DỤNG THỰC TẾ: BẢNG CỬU CHƯƠNG MATRIX ---")
print("KẾT QUẢ (Ma trận nhân từ 1 đến 9):")

for x in range(1, 10+15):      # Đại diện cho thừa số thứ nhất (Dòng)
    for y in range(1, 10+1):  # Đại diện cho thừa số thứ hai (Cột)
        # Kết quả là tích của tọa độ dòng x cột
        print(f"{x}x{y}={x*y}", end="\t")
    print()