import random

def random_number():
    maxNum = int(input("Enter the max number: "))
    minNum = int(input("Enter the min number: "))
    number = random.randint(minNum, maxNum)
    return number

def showResult(wins, total):
    if total > 0:
        win = (wins / total) * 100
        print(f"Games Won: {wins}")
        print(f"Total games played: {total}")
        print(f"Win percentage: {win:.2f}%")
    else:
        print("No game played yet.")
    return wins, total

def main():
    wins = 0
    totalgames = 0
    while True:
        number = random_number()
        guess = int(input("Guess a number: "))
        totalgames += 1
        if guess == number:
            print("You are right!!")
            wins += 1
        else:
            print(f" Oops! You lost! The number was: {number}")
        
        play = input("Do you want to play again? (yes/no): ").lower()
        if play != "yes":
            print("Goodbye!")
            showResult(wins, totalgames)
            break
        print("\nStarting new game...\n")

if __name__ == "__main__":
    main()
