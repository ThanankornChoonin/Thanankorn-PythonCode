import random

def test_random():
    random_number = random.randint(1, 10) #สุ่มตัวเขระหว่าง 1-10
    print("== Guess  Number between (1-10) ==")
    guess_number = input("What is your guess number:")
    guess_number = int(guess_number)

    if random_number == guess_number:
        print("Congratulations")

    if random_number < guess_number:
        print("Too High")    

    if random_number > guess_number:    
        print("Too Low")

    
test_random()