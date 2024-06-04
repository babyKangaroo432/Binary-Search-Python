#a free compiler: https://www.programiz.com/python-programming/online-compiler/
import math
user_input = int(input('Enter Your Number Please (1-∞): '))
print()
num_guesses = 0
highest_num = 10**math.ceil(math.log(user_input,10))
print(f'{highest_num:,} ')
lowest_num = 0
current_guess = highest_num//2
is_done = False
while not is_done:
    print(f'My Current Guess is: {current_guess:,}')
    num_guesses = num_guesses + 1
    if current_guess > user_input:
        highest_num = current_guess - 1
        current_guess = (highest_num + lowest_num)//2
    elif current_guess < user_input:
        lowest_num = current_guess + 1
        current_guess = (highest_num + lowest_num)//2
    else:
        print(f'Your number is {current_guess:,} and it took {num_guesses:,} guesses.')
        is_done = True
