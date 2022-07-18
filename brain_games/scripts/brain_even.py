import prompt
import random


def question():
    number_for_question = random.randint(1, 1000)
    print(f'Question: {number_for_question}')
    tans = 'no'
    if number_for_question % 2 == 0:
        tans = 'yes'
    ans = input('Your answer: ')
    if ans == tans:
        return 'Correct!'
    else:
        return f'"{ans}" is wrong answer ;(. Correct answer was "{tans}".'


def main():
    score = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
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
