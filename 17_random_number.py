import random

# Định nghĩa các cấu hình/hằng số
LOW = 1
HIGH = 100
OPTIONS = ("rock", "paper", "scissors")

# Khởi tạo danh sách bài
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Trộn bài và in kết quả
random.shuffle(cards)
print(cards)
