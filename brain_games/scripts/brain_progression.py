import prompt
import random


def question():
    len_progress = random.randint(5, 10)
    first_element = random.randint(0, 100)
    arifm_prog = random.randint(3, 20)
    progressive = [first_element, ]
    quest = 'Question: '
    tmp = first_element
    i = 1
    while i <= len_progress:
        tmp += arifm_prog
        progressive += [tmp, ]
        i += 1
    qu_element = random.randint(2, len_progress - 1)
    i = 0
    while i < len_progress:
        if i == qu_element - 1:
            quest += '..' + ' '
        else:
            quest += str(progressive[i]) + ' '
        i += 1
    print(quest)
    tans = progressive[qu_element - 1]
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
    print('What number is missing in the progression?')
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
