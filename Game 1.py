import random

def game_engine(max_attempts):
    is_win = False
    comp_num = random.randint(1, 100)
    
    for i in range(max_attempts):
        guess_num = int(input('Guess the number [1..100]: '))
        
        if guess_num == comp_num:
            print(f"You are a genius!\nYou guessed the correct number after {i + 1} attempts.")
            is_win = True
            break
        elif guess_num > comp_num:
            print("Your guessing number is greater than the computer's number.")
        else:
            print("Your guessing number is less than the computer's number.")
    
    print(f'Computer number is {comp_num}.')
    print("Good luck next time!")
    return is_win

def main():
    play_again = True
    total_games = 0
    total_wins = 0
    
    while play_again:
        level = input("Choose a level - easy(e), medium(m), hard(h): ").lower()
        
        if level == 'e':
            max_attempts = 9
        elif level == 'm':
            max_attempts = 6
        elif level == 'h':
            max_attempts = 4
        else:
            print("Invalid choice. Please select e, m, or h.")
            continue

        total_games += 1
        if game_engine(max_attempts):
            total_wins += 1

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input in ['yes', 'y']
    
    print(f"Total games played: {total_games}")
    print(f"Total wins: {total_wins}")

if __name__ == "__main__":
    main()