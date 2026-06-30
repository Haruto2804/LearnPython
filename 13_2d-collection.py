# ==============================================================================
# 🔥 BÀI TẬP ÔN TẬP: DANH SÁCH HAI CHIỀU (2D LISTS & 2D TUPLES) IN PYTHON 🔥
# ==============================================================================

print("=" * 60)
print(" CHỦ ĐỀ 1: MẠNG LƯỚI TẠP HÓA (2D LIST - DANH SÁCH 2 CHIỀU) ".center(60, "✨"))
print("=" * 60)

# 1. Khởi tạo các danh sách thành phần (1D Lists)
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# 2. Tạo danh sách 2 chiều chứa các danh sách trên
groceries = [fruits, vegetables, meats]

# ------------------------------------------------------------------------------
# 👉 Phần 1: Truy xuất phần tử theo tọa độ [Hàng][Cột]
# ------------------------------------------------------------------------------
print("\n🔹 [1] Truy xuất phần tử cụ thể:")
# groceries[0][2] -> Hàng 0 (fruits), Cột 2 (banana)
print(f"  • groceries[0][2] -> {groceries[0][2]}") 
# groceries[1][1] -> Hàng 1 (vegetables), Cột 1 (carrots)
print(f"  • groceries[1][1] -> {groceries[1][1]}") 
# groceries[2][0] -> Hàng 2 (meats), Cột 0 (chicken)
print(f"  • groceries[2][0] -> {groceries[2][0]}") 

# ------------------------------------------------------------------------------
# 👉 Phần 2: Duyệt qua từng danh sách con (In theo hàng)
# ------------------------------------------------------------------------------
print("\n🔹 [2] Duyệt qua từng bộ sưu tập (Từng hàng):")
for collection in groceries:
    print(f"  📂 Nhóm hàng: {collection}")

# ------------------------------------------------------------------------------
# 👉 Phần 3: Duyệt ma trận (Nested Loop - Vòng lặp lồng nhau) để in toàn bộ món ăn
# ------------------------------------------------------------------------------
print("\n🔹 [3] In toàn bộ thực phẩm dưới dạng bảng (Dùng Tab):")
for collection in groceries:
    print("  ", end="")  # Thụt lề đầu dòng cho đẹp
    for food in collection:
        print(f"{food:<12}", end="")  # Định dạng căn trái 12 ký tự thay vì dùng \t để đều hàng hơn
    print()  # Xuống dòng sau khi in hết một hàng


# ==============================================================================
# ✨ CHỦ ĐỀ 2: BÀI TẬP BÀN PHÍM ĐIỆN THOẠI (2D TUPLE - HẰNG SỐ MA TRẬN) ✨
# ==============================================================================
print("\n" + "=" * 60)
print(" CHỦ ĐỀ 2: BÀI TẬP BÀN PHÍM ĐIỆN THOẠI (2D TUPLE) ".center(60, "✨"))
print("=" * 60)

# Dùng Tuple lồng nhau khi dữ liệu cố định, không muốn bị chỉnh sửa (Immutable)
num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

print("\n📱 Giao diện bàn phím số:")
for row in num_pad:
    # Thêm khoảng trống ở đầu để căn giữa bàn phím cho đẹp
    print(" " * 24, end="") 
    for num in row:
        print(f"[{num}]", end="  ")  # Thêm ngoặc vuông tạo cảm giác giống phím bấm
    print()  # Xuống dòng cho hàng tiếp theo

print("\n" + "=" * 60)
print(" KIẾN THỨC CẦN NHỚ ".center(60, "📝"))
print("=" * 60)
print(" 1. List 2D là danh sách chứa các danh sách khác.")
print(" 2. Cú pháp truy xuất: matrix[row_index][column_index]")
print(" 3. Vòng lặp lồng nhau (Nested loop) là cách tốt nhất để duyệt ma trận.")
print("=" * 60 + "\n")