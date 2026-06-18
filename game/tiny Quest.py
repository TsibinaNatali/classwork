import random
result_win_num =0
result_win_number =0
a=0
name = input("Введите ваше имя ")
game_type = int(input("какой будет режим игры? 1-игрок , 2-компьютер"))
if game_type == 2:
    while True:
        win_num = 0
        win_number = 0
        while True:
            num = random.randint(1,3)
            if num == 1:
                print("я загадал камень ")
            elif num == 2:
                print("я загадал ножницы ")
            else:
                print("я загадал бумагу ")

            while True:
                number = input("Введите число от 1 до 3 ")
                if num == 1:
                    print(f"{name} загадал камень ")
                    break
                elif num == 2:
                    print(f"{name} загадал ножницы ")
                    break
                elif num == 3:
                    print(f"{name} загадал бумагу ")
                    break
                else:
                    print("ошибка ввода ")
            if num < number or num == 3 and number == 1:
                print("компьютер победил")
                win_num += 1
            elif num == number:
                print("ничья")
            else:
                print("победа игрока")
                win_number += 1

            if win_num == 3:
                print(f"компьютер победил со счетом {win_num}:{win_number}")
            elif win_number == 3:
                print(f"пользователь победил со счетом: {win_number}:{win_num}")
                print(f"Итоговый счет : ПК -{result_win_num} Игрок-{result_win_number}")
                a = input("вы хотите еще сыграть(Y/X)")
            if a != "Y":
                break
            else:
                result_win_num1 = 0
                result_win_number1 = 0
                while True:
                    win_num1 = 0
                    win_number1 = 0
                    while True:
                        num1 = random.randint(1, 3)
                        if num1 == 1:
                            print("я загадал камень ")
                        elif num1 == 2:
                            print("я загадал ножницы ")
                        else:
                            print("я загадал бумагу ")

                            while True:
                                number1 = input("Введите число от 1 до 3 ")
                                if num1 == 1:
                                    print(f"{name} загадал камень ")
                                    break
                                elif num1 == 2:
                                    print(f"{name} загадал ножницы ")
                                    break
                                elif num1 == 3:
                                    print(f"{name} загадал бумагу ")
                                    break
                                else:
                                    print("ошибка ввода ")
                            if num1 < number1 or num1 == 3 and number1 == 1:
                                print("компьютер победил")
                                win_num1 += 1
                            elif num1 == number1:
                                print("ничья")
                            else:
                                print("победа игрока")
                                win_number1 += 1

                            if win_num1 == 3:
                                print(f"компьютер победил со счетом {win_num1}:{win_number1}")
                            elif win_number1 == 3:
                                print(f"пользователь победил со счетом {win_number1}:{win_num1}")
                                print(f"Итоговый счет : ПК {result_win_num1} Игрок{result_win_number1}")
                    a = input("вы хотите еще сыграть(Y/X)")
                    if a != "Y":
                        break