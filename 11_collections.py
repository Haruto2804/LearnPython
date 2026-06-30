# ==============================================================================
# TỔNG QUAN VỀ COLLECTIONS TRONG PYTHON
# ==============================================================================

# 1. Định nghĩa dữ liệu mẫu ban đầu
fruits_list = ["apple", "orange", "banana", "coconut", "apple"]   # List []
fruits_set = {"apple", "orange", "banana", "coconut", "apple"}    # Set {}
fruits_tuple = ("apple", "orange", "banana", "coconut", "apple") # Tuple ()

print("--- PHẦN 1: PHÂN BIỆT ĐẶC TÍNH SƠ KHỞI ---")

# LIST: Có thứ tự (Ordered), thay đổi được (Changeable), cho phép trùng lặp (Duplicates OK)
print("List giữ nguyên thứ tự và cho phép 2 quả apple:", fruits_list)

# SET: Không thứ tự (Unordered), không thể sửa phần tử tại vị trí cụ thể, KHÔNG trùng lặp (NO Duplicates)
print("Set tự động lọc trùng (chỉ còn 1 apple) và đảo vị trí ngẫu nhiên:", fruits_set)

# TUPLE: Có thứ tự (Ordered), KHÔNG THỂ thay đổi (Unchangeable), trùng lặp OK, Tốc độ nhanh hơn (FASTER)
print("Tuple giữ nguyên thứ tự và không thể thêm/xóa phần tử sau khi tạo:", fruits_tuple)
print("-" * 50)


# ==============================================================================
# PHẦN 2: CÁC HÀM KIỂM TRA DỮ LIỆU (Xuất hiện từ dòng 7-10 trong ảnh của bạn)
# ==============================================================================
print("--- PHẦN 2: CÁC HÀM HỖ TRỢ XỬ LÝ ---")

# 2.1 Hàm len(): Đo độ dài (số lượng phần tử)
print(f"Độ dài của List: {len(fruits_list)}") # Kết quả: 5
print(f"Độ dài của Set (đã lọc trùng): {len(fruits_set)}") # Kết quả: 4

# 2.2 Toán tử 'in': Kiểm tra một phần tử có nằm trong tập hợp hay không (Trả về True/False)
print("Kiem tra 'pineapple' co trong set khong?:", "pineapple" in fruits_set) # False
print("Kiem tra 'apple' co trong set khong?:", "apple" in fruits_set)       # True

# 2.3 Hàm dir() và help() (Thường dùng để tra cứu nhanh khi code)
# print(dir(fruits_set))  # -> In ra toàn bộ các phương thức (hàm) có thể dùng với Set
# print(help(fruits_set)) # -> In ra hướng dẫn sử dụng chi tiết của Set (bấm Q để thoát nếu chạy terminal)
print("-" * 50)


# ==============================================================================
# PHẦN 3: CÁC PHƯƠNG THỨC (METHODS) PHỔ BIẾN CỦA TỪNG LOẠI
# ==============================================================================
print("--- PHẦN 3: CÁC THAO TÁC QUAN TRỌNG VỚI MỖI LOẠI ---")

# --- 3.1 THAO TÁC VỚI LIST ---
print("[LIST METHODS]")
fruits_list.append("pineapple")  # Thêm vào cuối list
fruits_list.remove("orange")     # Xóa phần tử "orange"
fruits_list.insert(0, "mango")   # Chèn "mango" vào vị trí số 0
print("List sau khi chỉnh sửa:", fruits_list)
print("Lấy phần tử đầu tiên bằng Index (List[0]):", fruits_list[0]) 

# --- 3.2 THAO TÁC VỚI SET ---
print("\n[SET METHODS]")
fruits_set.add("pineapple")      # Thêm phần tử vào set
fruits_set.remove("banana")      # Xóa phần tử khỏi set
# fruits_set[0] -> LỖI! Set không có số thứ tự (index) nên không thể lấy dữ liệu kiểu này.
print("Set sau khi chỉnh sửa:", fruits_set)

# --- 3.3 THAO TÁC VỚI TUPLE ---
print("\n[TUPLE METHODS]")
# fruits_tuple.append("mango")   # LỖI! Tuple không cho phép thêm.
# fruits_tuple.remove("apple")   # LỖI! Tuple không cho phép xóa.
print("Tuple chỉ có các hàm đếm hoặc tìm vị trí:")
print("Số lần xuất hiện của 'apple' trong Tuple:", fruits_tuple.count("apple"))
print("Vị trí (Index) của 'orange' trong Tuple:", fruits_tuple.index("orange"))
print("-" * 50)


# ==============================================================================
# PHẦN 4: DUYỆT VÒNG LẶP FOR VỚI COLLECTIONS (Dòng 13 trong ảnh)
# ==============================================================================
print("--- PHẦN 4: DUYỆT FOR VỚI COLLECTIONS ---")

print("Duyệt qua Set (Các phần tử in ra sẽ không theo thứ tự cố định):")
for fruit in fruits_set:
    print(f" -> Quả: {fruit}")