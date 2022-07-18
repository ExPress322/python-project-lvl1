import prompt
import random


def question():
    number_for_question = random.randint(1, 1000)
    tans = 'yes'
    if number_for_question == 1:
        tans = 'no'
    if number_for_question > 1:
        i = 2
        while i < number_for_question:
            if number_for_question % i == 0:
                tans = 'no'
            i += 1
    print(f'Question: {number_for_question}')
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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
