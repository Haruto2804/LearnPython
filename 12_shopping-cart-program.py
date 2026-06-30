import os

# Khởi tạo dữ liệu
foods = []
prices = []
total = 0

# Tiêu đề chương trình
print("╭" + "─" * 43 + "╮")
print("│" + "        GIỎ HÀNG THÂN THIỆN OVO          " + "│")
print("╰" + "─" * 43 + "╯")

while True:
    food = input("\n🛒 Nhập món ăn muốn mua (bấm 'q' để dừng): ").strip()
    if food.lower() == 'q':
        break
    
    if not food:
        print("❌ Tên món ăn không được để trống!")
        continue

    try:
        price = float(input(f"💰 Nhập giá cho [{food}]: $"))
        if price < 0:
            print("❌ Giá tiền không thể là số âm!")
            continue
            
        foods.append(food)
        prices.append(price)
        total += price
        print(f"✅ Đã thêm [{food}] vào giỏ hàng.")
    except ValueError:
        print("❌ Vui lòng nhập một số hợp lệ cho giá tiền!")

# Xóa màn hình cho sạch sẽ (tùy chọn, hoạt động tốt trên Terminal thực tế)
# os.system('cls' if os.name == 'nt' else 'clear')

# Giao diện hóa đơn cuối cùng
print("\n" + "═" * 45)
print(" 🛒 HOÁ ĐƠN MUA HÀNG CỦA BẠN ".center(45, "✨"))
print("═" * 45)
print(f" {'Tên món':<25} │ {'Giá tiền':>13} ")
print("─" * 45)

# Duyệt và in theo dạng bảng thẳng hàng
for i in range(len(foods)):
    print(f"  • {foods[i]:<22} │ ${prices[i]:>12.2f}")

print("─" * 45)
print(f" 💵 TỔNG CỘNG:".ljust(27) + f"${total:>14.2f}")
print("═" * 45)
print("🌟 Cảm ơn bạn đã mua hàng! Hẹn gặp lại! 🌟\n")