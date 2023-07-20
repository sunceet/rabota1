import random

def game():
    win = 0
    loss = 0
    consecutive_losses = 0

    while consecutive_losses < 3:
        guess = input("Орёл (0) или решка (1)? Введите 0 или 1: ")

        if guess == "0" or guess == "1":
            guess = int(guess)
            result = random.randint(0, 1)

            if guess == result:
                print("Поздравляю, вы угадали!")
                win += 1
                consecutive_losses = 0

            else:
                print("Вы не угадали.")
                loss += 1
                consecutive_losses += 1

            print("Выигрыши: ", win)
            print("Проигрыши: ", loss)

        else:
            print("Игра завершена.")
            break

game()
