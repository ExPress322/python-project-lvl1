import prompt
import random
import math


def question():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    print(f'Question: {num1} {num2}')
    tans = math.gcd(num1, num2)
    ans = input('Your answer: ')
    if int(ans) == tans:
        return 'Correct!'
    else:
        return f'"{ans}" is wrong answer ;(. Correct answer was "{tans}".'


def main():
    score = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    while score < 3:
        answer = question()
        if answer == 'Correct!':
            print(answer)
            score += 1
        else:
            print(answer)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
