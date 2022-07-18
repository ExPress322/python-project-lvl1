import prompt
import random
import math


def question():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    print(f'Question: {num1} {num2}')
    true_answer = math.gcd(num1, num2)
    answer = input('Your answer: ')
    if int(answer) == true_answer:
        return 'Correct!'
    else:
        return f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".'


def main():
    score = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    while score < 3:
        ans = question()
        if ans == 'Correct!':
            print(ans)
            score += 1
        else:
            print(ans)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
