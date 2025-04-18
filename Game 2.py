import random

def game_engine():
    # Khởi tạo số tiền bắt đầu và số tiền cược
    money = 100000
    bet_amount = 10000
    win_count = 0
    
    print("Chào mừng đến với game Tài Xỉu!")
    print(f"Số tiền hiện tại của bạn: {money}")

    while money >= bet_amount:
        # Người dùng chọn trạng thái Tài, Xỉu hoặc cược vào số 5
        print("\nBạn có thể chọn:")
        print("1. Tài (Tổng xúc xắc > 5)")
        print("2. Xỉu (Tổng xúc xắc <= 5)")
        print("3. Cược vào số 5 (Nếu tổng bằng 5 thì thắng 3 lần cược)")
        
        select = int(input("Chọn (1/2/3): "))
        
        if select not in [1, 2, 3]:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
            continue
        
        # Gieo 2 con xúc sắc
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        sum_dice = die_1 + die_2
        
        print(f"Tổng xúc xắc: {sum_dice}")
        
        if sum_dice > 5:
            result = 1  # Tài
        elif sum_dice <= 5:
            result = 2  # Xỉu
        else:
            result = 3  # Không thể xảy ra
        
        # Kiểm tra kết quả
        if select == 3 and sum_dice == 5:
            money += bet_amount * 3
            win_count += 1
            print("Bạn thắng 3 lần tiền cược!")
        elif select == 1 and result == 1:
            money += bet_amount
            win_count += 1
            print("Bạn thắng!")
        elif select == 2 and result == 2:
            money += bet_amount
            win_count += 1
            print("Bạn thắng!")
        else:
            money -= bet_amount
            print("Bạn thua!")
        
        print(f"Số tiền hiện tại của bạn: {money}")
        
        # Kiểm tra tiền còn lại
        if money < bet_amount:
            print("Bạn không còn đủ tiền để tiếp tục chơi!")
            break
        
        # Hỏi người chơi có muốn tiếp tục không
        play_again = input("Bạn có muốn chơi tiếp không? (có/không): ").strip().lower()
        if play_again != "có":
            break
            
    # Thống kê kết quả
    print(f"\nKết thúc trò chơi!")
    print(f"Số tiền còn lại: {money}")
    print(f"Số ván thắng: {win_count}")

if __name__ == '__main__':
    game_engine()