
num_list = [i for i in range(1, 33)]
guess = num_list[round((len(num_list)) / 2)-1]
low_define = False
high_define = False
print(guess)

while True:
    num = input("low or high or correct : ")

    if not num_list:
        print("Sorry we ran out of numbers")
        break

    elif num == "correct":
        print("Yes i won")
        break

    elif num.lower() == "low":

        if low_define:

            low_define = False
            number = num_list[round((len(num_list)) / 2) - 1]
            a = []
            for i in num_list:
                if i < number:
                    a.append(i)

            for i in a:
                num_list.remove(i)

            if number in num_list:
                num_list.remove(number)

            if guess in num_list:
                num_list.remove(guess)

            print(num_list)

            print(number)
            continue

        if guess in num_list:
            num_list.remove(guess)

        number = num_list[round((len(num_list)+1)/4)-1]


        print(num_list)
        print(number)
        num_2 = input("low or high or correct : ")

        if not num_list:
            print("Sorry we ran out of numbers")
            break

        elif num_2.lower() == "correct":
            print("Yes i won")
            break

        elif num_2.lower() == "low":
            a = []
            for i in num_list:
                if i < number:
                    a.append(i)

            for i in a:
                num_list.remove(i)

            if number in num_list:
                num_list.remove(number)

            if guess in num_list:
                num_list.remove(guess)

            print(num_list)
            guess = num_list[round((len(num_list)) / 2) - 1]
            print(guess)

        elif num_2.lower() == "high":
            high_define = True
            for i in range(number, guess+1):
                if i in num_list:
                    num_list.remove(i)


            if number in num_list:
                num_list.remove(number)

            if guess in num_list:
                num_list.remove(guess)

            print(num_list)
            guess = num_list[round(3*len(num_list)/4)-1]
            print(guess)

    elif num.lower() == "high":
        if guess in num_list:
            num_list.remove(guess)
        print(num_list)
        number = num_list[round(3*len(num_list)/4)-1]
        if high_define:
            number = num_list[round((len(num_list)) / 2) - 1]
            high_define = False
        print(number)
        num_2 = input("low or high or correct : ")

        if not num_list:
            print("Sorry we ran out of numbers")
            break

        elif num_2.lower() == "correct":
            break

        elif num_2.lower() == "high":
            a = []
            for i in num_list:
                if i > number:
                    a.append(i)

            for i in a:
                num_list.remove(i)

            if number in num_list:
                num_list.remove(number)

            if guess in num_list:
                num_list.remove(guess)

            print(num_list)
            guess = num_list[round((len(num_list)) / 2)-1]
            print(guess)

        elif num_2.lower() == "low":
            low_define = True
            for i in range(guess, number+1):
                if i in num_list:
                    num_list.remove(i)

            if number in num_list:
                num_list.remove(number)

            if guess in num_list:
                num_list.remove(guess)

            print(num_list)
            guess = num_list[round((len(num_list)+1)/4)-1]
            print(guess)
