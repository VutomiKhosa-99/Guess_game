def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again ")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0

print("Play this guessing game about animals")
print("Ready? . . . go!")

guess1 = input("Which animal is the only flying mammal? ")
check_guess(guess1, "bat")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the biggest animal on the planet? ")
check_guess(guess3, "Blue Whale")
guess4 = input("What is a male zebra called? ")
check_guess(guess4, "Stallion")
guess5 = input("Which bird can fly straight up, down, and backward? ")
check_guess(guess5, "hummingbird")
guess6 = input("Which animal has the highest blood pressure? ")
check_guess(guess6, "Giraffe")
guess7 = input("Which sea creature that can change its gender? ")
check_guess(guess4, "oyster")
guess8 = input("Which bird’s eye is bigger than its brain? ")
check_guess(guess4, "Ostrich")
guess9 = input("What color is a giraffe’s tongue? ")
check_guess(guess4, "Purple")
guess10 = input("Which animal leaps out of the water to communicate with others of its kind? ")
check_guess(guess4, "Whale")

print("Your Score is "+ str(score))