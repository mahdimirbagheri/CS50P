from random import randint

while True:

    try:
        level = int(input("Level: ").strip())

        if level >= 1:
            rand = randint(1, level)

            while True:
                guess = int(input("Guess: ").strip())

                try:
                    if guess > rand:
                        print("Too large!")
                    elif guess < rand:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
                except (ValueError, TypeError):
                    continue
            break
    except (ValueError, TypeError):
        continue
