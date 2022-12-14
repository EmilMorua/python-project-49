import prompt
import brain_games.cli


def start_game(game, max_point=3) -> None:
    '''Accepts a function from the selected game module.
    Plays the game and ends the game'''

    count_correct_answ = 0
    while (count_correct_answ < max_point):
        question, answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
            count_correct_answ += 1
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                     f"Correct answer was '{answer}'.\n"
                     f"Let's try again, {brain_games.cli.name}!")
            exit()

    print(f"Congratulations, {brain_games.cli.name}!")
    exit()
