import prompt
import random


def question():
    number_for_question = random.randint(1, 1000)
    true_answer = 'yes'
    if number_for_question == 1:
        true_answer = 'no'
    if number_for_question > 1:
        i = 2
        while i < number_for_question:
            if number_for_question % i == 0:
                true_answer = 'no'
            i += 1
    print(f'Question: {number_for_question}')
    answer = input('Your answer: ')
    if answer == true_answer:
        return 'Correct!'
    else:
        return f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".'


def main():
    score = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
