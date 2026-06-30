import time

my_time = int(input("Nhập thời gian đếm ngược (giây): "))

# Thêm dòng thông báo bắt đầu
print("\n=== ĐỒNG HỒ ĐẾM NGƯỢC ===")

for x in range(my_time, -1, -1): # Chạy về đến 0 để thấy số 00:00:00
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    
    # end="\r" giúp xóa dòng cũ và in đè lên tại chỗ
    print(f"⏱️  Thời gian còn lại: {hours:02}:{minutes:02}:{seconds:02}", end="\r")
    time.sleep(1)

# Xóa dòng đếm ngược cũ và in thông báo kết thúc to rõ
print(" " * 40, end="\r") 
print("🔔 KẾT THÚC HẾT GIỜ !!! 🔔\n")