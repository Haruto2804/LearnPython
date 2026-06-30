# Khởi tạo biến đếm
count = 1  

# Chừng nào count còn nhỏ hơn hoặc bằng 5 thì còn chạy code bên trong
while count <= 5:
    print(f"Lần lặp thứ: {count}")
    
    # QUAN TRỌNG: Phải tăng biến đếm lên, nếu không vòng lặp sẽ chạy vô tận!
    count += 1  

print("Đã thoát khỏi vòng lặp!")