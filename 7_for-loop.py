# ==============================================================================
# PHẦN 1: CÁC DẠNG VÒNG LẶP FOR CƠ BẢN
# ==============================================================================
print("--- PHẦN 1: CÁC DẠNG VÒNG LẶP FOR CƠ BẢN ---")

# 1.1 Duyệt qua một chuỗi (String)
print("1.1 Duyệt chuỗi:")
credit_card = "1234-5678"
for ky_tu in credit_card:
    print(ky_tu, end=" ")  # end=" " để in trên cùng một dòng
print("\n" + "-"*20)

# 1.2 Duyệt qua một danh sách (List)
print("1.2 Duyệt List:")
trai_cay = ["Táo", "Chuối", "Cam"]
for f in trai_cay:
    print(f"Tôi thích ăn {f}")
print("-"*20)

# 1.3 Duyệt vùng số với hàm range()
print("1.3 Dùng range(stop):")
for i in range(3):  # Chạy từ 0 đến 2
    print(i, end=" ")
print("\n")

print("1.4 Dùng range(start, stop):")
for i in range(2, 6):  # Chạy từ 2 đến 5
    print(i, end=" ")
print("\n")

print("1.5 Dùng range(start, stop, step):")
for i in range(1, 10, 2):  # Số lẻ từ 1 đến 9
    print(i, end=" ")
print("\n\n")


# ==============================================================================
# PHẦN 2: ĐIỀU HƯỚNG VÒNG LẶP (BREAK & CONTINUE)
# ==============================================================================
print("--- PHẦN 2: LỆNH ĐIỀU HƯỚNG ---")

# 2.1 Lệnh break (Thoát vòng lặp lập tức)
print("2.1 Thử nghiệm lệnh break (Dừng lại khi gặp số 5):")
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")
print("\n" + "-"*20)

# 2.2 Lệnh continue (Bỏ qua lượt hiện tại)
print("2.2 Thử nghiệm lệnh continue (Bỏ qua số 3):")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print("\n\n")


# ==============================================================================
# PHẦN 3: KIẾN THỨC NÂNG CAO
# ==============================================================================
print("--- PHẦN 3: KIẾN THỨC NÂNG CAO ---")

# 3.1 Dùng enumerate() để lấy cả chỉ số (index) và giá trị (value)
print("3.1 Dùng enumerate():")
ds_ten = ["An", "Bình", "Cường"]
for index,name in enumerate(ds_ten):
    print(f"Học sinh vị trí số {index} là: {name}")
print("-"*20)

# 3.2 Cấu trúc for ... else (else chạy khi vòng lặp hoàn thành, không bị break)
print("3.2 Thử nghiệm cấu trúc for...else:")
for i in range(3):
    print(f"Đang chạy lượt {i}")
else:
    print("-> Vòng lặp kết thúc thành công (Không bị break)!")
print("-"*20)

# Minh họa khi có break thì else KHÔNG chạy:
print("Minh họa for...else khi có break:")
for i in range(3):
    if i == 1:
        print("-> Bị break ở lượt 1!")
        break
else:
    print("Dòng này sẽ không bao giờ được in ra!")
print("-"*20)

# 3.3 Vòng lặp lồng nhau (Nested Loop) - Ví dụ in bảng tọa độ
print("3.3 Vòng lặp lồng nhau (Tọa độ i, j):")
for i in range(1, 4):        # Vòng lặp ngoài (dòng)
    for j in range(1, 3):    # Vòng lặp trong (cột)
        print(f"({i},{j})", end=" ")
    print()  # Xuống dòng sau khi chạy xong một dòng j
print("-"*20)
# 3.4 List Comprehension (Viết nhanh vòng lặp trên 1 dòng để tạo List)
print("3.4 List Comprehension:")
# Tạo danh sách bình phương các số từ 1 đến 4
binh_phuong = [x**2 for x in range(1, 5)]
print("Danh sách bình phương:", binh_phuong)