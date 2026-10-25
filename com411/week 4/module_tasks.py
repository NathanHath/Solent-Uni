import random
minimum_value = int(input("what is the minimum number?"))
maximum_value = int(input("what is the maximum number?"))
random_number = int(random.randint(minimum_value, maximum_value))
answer = False
while answer == False:
    user_answer = int(input("what is the answer?"))
    if user_answer == random_number:
        answer = True
        print ("You got it!")
    elif user_answer < random_number:
        answer = False
        print ("Your guess is too low \n try again")
    elif user_answer > random_number:
        answer = False
        print ("Your guess is too high \n try again")
    else :
        user_answer = False
