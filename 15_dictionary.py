# =====================================================================
# 1. KHỞI TẠO DICTIONARY BAN ĐẦU
# =====================================================================
print("--- 1. Dictionary Ban Đầu ---")
capitals = {
    "VietNam": "HaNoi",
    "USA": "Washington, D.C.",
    "India": "New Delhi",
    "Canada": "Ottawa",  # Đã sửa lại thủ đô chính xác của Canada nha!
}
print("Từ điển gốc:", capitals)
print("-" * 50)


# =====================================================================
# 2. CÁC METHOD TRUY XUẤT DỮ LIỆU (READ)
# =====================================================================
print("--- 2. Các Method Xem Dữ Liệu ---")

# .get() -> Lấy giá trị an toàn, không sợ bị crash/lỗi nếu key không có
print("Thủ đô VN (dùng get):", capitals.get("VietNam"))
print("Thủ đô Japan (dùng get):", capitals.get("Japan"))  # Trả về None
print("Thủ đô Japan (có default):", capitals.get("Japan", "Chưa cập nhật"))

# .keys() -> Lấy tất cả các Khóa (Tên nước)
print("Danh sách các nước (keys):", list(capitals.keys()))

# .values() -> Lấy tất cả các Giá trị (Tên thủ đô)
print("Danh sách các thủ đô (values):", list(capitals.values()))

# .items() -> Lấy cặp (key, value) - Thường dùng nhất với vòng lặp 'for'
print("Danh sách các cặp (items):", list(capitals.items()))

print("\nDuyệt qua từng phần tử bằng vòng lặp for:")
for country, city in capitals.items():
    print(f" * Quốc gia: {country} -> Thủ đô: {city}")
print("-" * 50)


# =====================================================================
# 3. CÁC METHOD THÊM VÀ SỬA ĐỔI (UPDATE)
# =====================================================================
print("--- 3. Các Method Thêm & Sửa Đổi ---")

# .update() -> Thêm mới nhiều phần tử hoặc sửa đổi giá trị cũ cùng lúc
capitals.update({"Germany": "Berlin", "VietNam": "Hà Nội"})
print("Sau khi update (Thêm Đức, sửa VN):", capitals)

# .setdefault() -> Lấy giá trị, nếu CHƯA CÓ thì tự động thêm vào dictionary luôn
phap_capital = capitals.setdefault("France", "Paris")
print("Giá trị lấy ra từ setdefault:", phap_capital)
print("Từ điển sau khi setdefault (Tự thêm France):", capitals)
print("-" * 50)


# =====================================================================
# 4. CÁC METHOD XÓA DỮ LIỆU (DELETE)
# =====================================================================
print("--- 4. Các Method Xóa ---")

# .pop() -> Xóa một key được chỉ định và trả về giá trị của key đó
removed_city = capitals.pop("USA")
print(f"Đã xóa nước USA (Thủ đô của nó là: {removed_city})")
print("Từ điển sau khi pop('USA'):", capitals)

# .popitem() -> Xóa phần tử cuối cùng vừa được thêm vào (ở đây là France)
last_item = capitals.popitem()
print(f"Đã xóa phần tử cuối cùng: {last_item}")
print("Từ điển sau khi popitem():", capitals)
print("-" * 50)


# =====================================================================
# 5. METHOD SAO CHÉP VÀ XÓA SẠCH (COPY & CLEAR)
# =====================================================================
print("--- 5. Copy và Clear ---")

# .copy() -> Tạo một bản sao độc lập (để nghịch phá không ảnh hưởng từ điển gốc)
capitals_backup = capitals.copy()
print("Đây là từ điển backup:", capitals_backup)

# .clear() -> Xóa sạch sành sanh mọi thứ trong từ điển
capitals.clear()
print("Từ điển gốc sau khi .clear():", capitals)  # Sẽ in ra dấu {} rỗng
print("Từ điển backup sau khi gốc bị xóa:", capitals_backup)  # Vẫn còn nguyên vẹn!
print("-" * 50)
