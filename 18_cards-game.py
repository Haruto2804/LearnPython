import random

# 🎮 ĐỀ BÀI: GAME XÌ DÁCH MINI (BLACKJACK)
# Hệ thống sẽ tự động chia bài cho bạn (Người chơi) và Máy (Computer). Ai có tổng điểm gần 21 nhất thì thắng.
# Nếu quá 21 điểm thì "quắc" (thua).

# Quy ước điểm số của các lá bài:
# Các lá từ 2 đến 10: Số điểm bằng đúng số trên lá bài.

# Các lá hình Jack, Queen, King: Tính là 10 điểm.
card_points = {"Jack": 10, "Queen": 10, "King": 10}
# Lá Ace (Xì): Để cho đơn giản ở bản mini này, bạn tính cố định là 11 điểm (hoặc 1 điểm tùy bạn chọn khi code).
card_points.update({"Ace": 11})

print(card_points)
# Score của 2 người chơi
player_score = 0
computer_score = 0
result = ""
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
is_end_game = False
while not is_end_game:
    # Lượt của người chơi
    while True:
        choice = input("Bạn có muốn rút thêm bài không? (Y/N): ").upper()
        if choice == "N":
            break
        else:
            player_card = random.choice(cards)
            # Điểm của bài hiện tại
            if player_card in card_points:
                current_card_score = card_points[player_card]
            else:
                current_card_score = int(player_card)
            # Tổng điểm người chơi
            player_score += current_card_score
            print(
                f"Bài của bạn: ['{player_card}','{current_card_score}'] | Tổng điểm: {player_score}"
            )
            if player_score > 21:
                print("Bạn đã quắc (thua)!!!")
                is_end_game = True
                result = "Computer WIN!"
                break
    computer_has_drawn = ""
    # Lượt chơi của máy
    while is_end_game == False:
        if computer_score <= 11:
            computer_has_drawn = "yes"
            print(f"Máy đang có {computer_score} điểm -> Máy rút thêm bài...")
        elif 12 <= computer_score <= 16:
            computer_has_drawn = random.choice(["yes", "no"])
            print(f"Máy đang có {computer_score} điểm -> Máy rút thêm bài...")
        else:
            computer_has_drawn = "no"
        # điều kiện dừng rút bài của máy
        if computer_has_drawn == "no":
            print(f"Máy đang có {computer_score} điểm -> Máy dừng rút thêm bài...")
            is_end_game = True
            continue
        computer_card = random.choice(cards)
        if computer_card in card_points:
            current_card_score = card_points.get(computer_card)
        else:
            current_card_score = int(computer_card)
        computer_score += current_card_score
        if computer_score > 21:
            print(f"Máy đã quắc (thua)!!!")
            result = "You WIN!"
            is_end_game = True  # Đánh dấu game kết thúc
            break
if not result:
    if player_score < computer_score:
        result = "Computer WIN!"
    elif player_score > computer_score:
        result = "You WIN!"
    else:
        result = "DRAW !!!"

print("\n==============================")
print(f"🏆 Tổng điểm của bạn: {player_score}")
print(f"🤖 Tổng điểm của máy: {computer_score}")
print("🔥 KẾT QUẢ CUỐI CÙNG:", result)
print("==============================")
