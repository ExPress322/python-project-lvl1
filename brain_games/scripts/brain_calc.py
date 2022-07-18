import prompt
import random


def question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice('+-*')
    print(f'Question: {num1} {op} {num2}')
    if op == '+':
        true_answer = num1 + num2
    elif op == '-':
        true_answer = num1 - num2
    else:
        true_answer = num1 * num2
    answer = input('Your answer: ')
    if int(answer) == true_answer:
        return 'Correct!'
    else:
        return f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".'


def main():
    score = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
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
