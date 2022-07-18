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
    true_answer = progressive[qu_element - 1]
    answer = input('Your answer: ')
    if int(answer) == true_answer:
        return 'Correct!'
    else:
        return f'"{answer}" is wrong answer ;(. Correct answer was "{true_answer}".'


def main():
    score = 0
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
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
