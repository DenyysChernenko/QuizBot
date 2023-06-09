import telebot
import random
from telebot import types
user_topic_history = {}
user_data = {}
# Functions for tests

def vocabulary_tests(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {}

    if user_id in user_data and 'question_counter' in user_data[user_id] and user_data[user_id]['question_counter'] > 5:
        bot.send_message(message.chat.id,
                         f'You have finished the test with {user_data[user_id]["correct_answers"]} correct answers!!!!!')
        user_data[user_id] = {}
        return button_vocabulary(message)


    if user_id in user_data and 'chosen_lvl' not in user_data[user_id]:
         user_data[user_id]['chosen_lvl'] = None

    if message.text == 'A1-A2':
        file_names = 'A1-A2_vocabulary.txt'
        chosen_lvl = file_names
        user_data[user_id]['chosen_lvl'] = chosen_lvl
    elif message.text == 'B1-B2':
        file_names = 'B1-B2_vocabulary.txt'
        chosen_lvl = file_names
        user_data[user_id]['chosen_lvl'] = chosen_lvl
    elif message.text == 'C1-C2':
        file_names = 'C1-C2_vocabulary.txt'
        chosen_lvl = file_names
        user_data[user_id]['chosen_lvl'] = chosen_lvl
    else:
        chosen_lvl = user_data[user_id]['chosen_lvl']


    if 'question_counter' not in user_data[user_id]:
        user_data[user_id]['question_counter'] = 1

    if 'answer' not in user_data[user_id]:
        user_data[user_id]['answer'] = ''

    if 'correct_answers' not in user_data[user_id]:
        user_data[user_id]['correct_answers'] = 0

    with open(chosen_lvl, 'r') as file:
        lines = file.readlines()
        index = random.randint(1, len(lines) // 2)
        index = index * 2 - 1 if index * 2 - 1 <= len(lines) else len(lines)

        if index <= len(lines):
            question = lines[index-1]
            options = lines[index].split(",")
            answer = options[0].strip()
            random.shuffle(options)

            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            answer_buttons = [telebot.types.KeyboardButton(option.strip()) for option in options]
            markup.add(*answer_buttons)
            markup.add('Back')
            bot.send_message(message.chat.id, f'{chosen_lvl}')
            bot.send_message(message.chat.id, f'{index}')
            bot.send_message(message.chat.id, f'{index-1}')

            user_data[user_id]['answer'] = answer

            bot.send_message(message.chat.id, f'{user_data[user_id]["question_counter"]}. {question}',  reply_markup=markup)
            bot.register_next_step_handler(message, handle_answer)


def handle_answer(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return

    user_data[user_id]['question_counter'] += 1
    answer = user_data[user_id]['answer']

    if message.text == answer:
        user_data[user_id]['correct_answers'] += 1
        bot.reply_to(message, f'Correct answer! Correct answers: {user_data[user_id]["correct_answers"]}✔️')
        vocabulary_tests(message)
    elif message.text == 'Back':
        bot.send_message(message.chat.id,
                         f'You have finished the test with {user_data[user_id]["correct_answers"]} correct answers!')
        user_data[user_id] = {}
        return button_vocabulary(message)
    else:
        bot.reply_to(message, f'Wrong answer! Correct answers: {user_data[user_id]["correct_answers"]}❌')
        bot.send_message(message.chat.id, f'Correct answer is: \"{answer}\"🕵️‍♂️')
        vocabulary_tests(message)


# Functions for tests
def grammar_tests(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {}

    if user_id in user_data and 'question_counter' in user_data[user_id] and user_data[user_id]['question_counter'] > 10:
        bot.send_message(message.chat.id,
                         f'You have finished the test with {user_data[user_id]["correct_answers"]} correct answers!!!!!')
        user_data[user_id] = {}
        return buttons_grammar(message)

    if user_id in user_data and 'chosen_lvl' not in user_data[user_id]:
        user_data[user_id]['chosen_lvl'] = None

    if message.text == 'A1-A2':
        file_names = 'A1-A2_grammar.txt'
        chosen_lvl = file_names
        user_data[user_id]['chosen_lvl'] = chosen_lvl
    elif message.text == 'B1-B2':
        file_names = 'B1-B2_grammar.txt'
        chosen_lvl = file_names
        user_data[user_id]['chosen_lvl'] = chosen_lvl
    elif message.text == 'C1-C2':
        file_names = 'C1-C2_grammar.txt'
        chosen_lvl = file_names
        user_data[user_id]['chosen_lvl'] = chosen_lvl
    else:
        chosen_lvl = user_data[user_id]['chosen_lvl']

    if 'question_counter' not in user_data[user_id]:
        user_data[user_id]['question_counter'] = 1

    if 'answer' not in user_data[user_id]:
        user_data[user_id]['answer'] = ''

    if 'correct_answers' not in user_data[user_id]:
        user_data[user_id]['correct_answers'] = 0

    with open(chosen_lvl, 'r') as file:
        lines = file.readlines()
        index = random.randint(1, len(lines) // 2)
        index = index * 2 - 1 if index * 2 - 1 <= len(lines) else len(lines)

        if index <= len(lines):
            question = lines[index-1]
            options = lines[index].split(",")
            answer = options[0].strip()
            user_data[user_id]['answer'] = answer
            random.shuffle(options)

            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            answer_buttons = [telebot.types.KeyboardButton(option.strip()) for option in options]
            markup.add(*answer_buttons)
            markup.add('Back')

            bot.send_message(message.chat.id, f'{user_data[user_id]["question_counter"]}. {question}',reply_markup=markup)
            bot.register_next_step_handler(message, handle_answers)

def handle_answers(message):
    user_id = message.from_user.id

    user_data[user_id]['question_counter'] += 1
    answer = user_data[user_id]['answer']

    if message.text == answer:
        user_data[user_id]['correct_answers'] += 1
        bot.reply_to(message, f'Correct answer! Correct answers: {user_data[user_id]["correct_answers"]}✔️')
        grammar_tests(message)
    elif message.text == 'Back':
        bot.send_message(message.chat.id,
                         f'You have finished the test with {user_data[user_id]["correct_answers"]} correct answers!')
        user_data[user_id] = {}
        return buttons_grammar(message)
    else:
        bot.reply_to(message, f'Wrong answer! Correct answers: {user_data[user_id]["correct_answers"]}❌')
        bot.send_message(message.chat.id, f'Correct answer is: \"{answer}\"🕵️‍♂️')
        grammar_tests(message)


# Functions
def help(message):
    choosen_option_message = 'You have chosen <b>Help</b> option!\n'
    help_message = (
        f"Hi, <b>{message.from_user.first_name}!</b> Our tasks are designed to improve your English grammar and vocabulary.📚 \n"
        "<b>Grammar</b> topic you will have a different types of questions, and you need to choose the correct answer from 4 options.\n"
        "<b>Vocabulary</b> section mostly has three types of tests:\n"
        "finding a synonym, choosing the word by its definition, and inserting the correct word in a sentence.\n"
        "Thank you, guys, that you are using my quizbot!\n"
        "I really appreciate it.\n"
        "<b>⚠️WARNING️:</b> Please, guys, don't spam inside the tests. Just click on the button once, and wait for bot printing the next question.\n"
        "The bot is not perfect, and can break due to spamming answers. Thanks!\n"
    )
    bot.send_message(message.chat.id, choosen_option_message, parse_mode='html')
    bot.send_message(message.chat.id, help_message, parse_mode='html')

def about_authors(message):
    choosen_option_message = 'You have chosen <b>About authors</b> option!\n'
    about_authors_message = (
        f"Hi, guys! We are Denys and Ivan, two 18-year-old Ukrainian students who are studying abroad right now.\n"
        f"(you might know why 😊).\n"
        f"We want to create a really good Telegram bot, that can help you learn English anywhere!\n"
        f"Also, we are not quite proficient in programming, but we are currently studying it, and you can also help us with it!\n"
        "Here is my Telegram account for some feedback to improve our project:\n"
        "<a href='https://t.me/denischernenkoo'>Denys</a>\n"
        "We appreciate you for using our bot to learn English.\n"
    )
    bot.send_message(message.chat.id, choosen_option_message, parse_mode='html')
    bot.send_message(message.chat.id, about_authors_message, parse_mode='html')


# Start buttons
@bot.message_handler(commands=['start'])
def buttons_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    help_button = types.KeyboardButton('Help')
    about_button = types.KeyboardButton('About authors')
    grammar_button = types.KeyboardButton('Grammar tests')
    vocabulary_button = types.KeyboardButton('Vocabulary learning')
    markup.add(help_button, about_button, grammar_button, vocabulary_button)
    start_message = (
                      f"Hi, <b>{message.from_user.first_name}</b>, this is a quizbot to improve your English LVL\n"
                      "You can choose either grammar tests or vocabulary learning\n"
                      "You can press help button to get more information about tests and vocabulary learning\n" )
    bot.send_message(message.chat.id, start_message, reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['Grammar tests'])
def buttons_grammar(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    first_level_button = types.KeyboardButton('A1-A2')
    second_level_button = types.KeyboardButton('B1-B2')
    third_level_button = types.KeyboardButton('C1-C2')
    back_button = types.KeyboardButton('Back')
    markup.add(first_level_button, second_level_button, third_level_button, back_button)
    choosen_option_message = f"You have chosen <b>Grammar tests.</b>\n"
    bot.send_message(message.chat.id, choosen_option_message, reply_markup=markup, parse_mode='html')
    level_message = "Now, you must pick your current level of English.\n"
    bot.send_message(message.chat.id, level_message, reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['Vocabulary learning'])
def button_vocabulary(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    first_level_button = types.KeyboardButton('A1-A2')
    second_level_button = types.KeyboardButton('B1-B2')
    third_level_button = types.KeyboardButton('C1-C2')
    back_button = types.KeyboardButton('Back')
    markup.add(first_level_button, second_level_button, third_level_button, back_button)
    choosen_option_message = f"You have chosen <b>Vocabulary learning.</b>\n"
    bot.send_message(message.chat.id, choosen_option_message, reply_markup=markup, parse_mode='html')
    level_message = "Now, you must pick your current level of English.\n"
    bot.send_message(message.chat.id, level_message, reply_markup=markup, parse_mode='html')





# Parsing text
@bot.message_handler(content_types=['text'])
def buttons(message):
        user_id = message.chat.id
        if user_id not in user_topic_history:
            user_topic_history[user_id] = []

        if message.text == 'Help':
            help(message)
        elif message.text == 'About authors':
            about_authors(message)
        elif message.text == 'Grammar tests':
            user_topic_history[user_id].append('Grammar tests')
            buttons_grammar(message)
        elif user_topic_history[user_id] and user_topic_history[user_id][-1] == 'Grammar tests' and message.text != 'Back':
            if message.text == 'A1-A2':
                bot.send_message(message.chat.id, 'Your chosen level: <b>A1-A2</b>', parse_mode='html')
                grammar_tests(message)
            elif message.text == 'B1-B2':
                bot.send_message(message.chat.id, 'Your chosen level: <b>B1-B2</b>', parse_mode = 'html')
                grammar_tests(message)
            elif message.text == 'C1-C2':
                bot.send_message(message.chat.id, 'Your chosen level: <b>C1-C2</b>', parse_mode = 'html')
                grammar_tests(message)

            else:
                bot.send_message(message.chat.id, 'Please, choose one of the buttons below' , parse_mode = 'html')

        elif message.text == 'Vocabulary learning':
            user_topic_history[user_id].append('Vocabulary learning')
            button_vocabulary(message)
        elif user_topic_history[user_id] and user_topic_history[user_id][-1] == 'Vocabulary learning' and message.text != 'Back':
            if message.text == 'A1-A2':
                bot.send_message(message.chat.id, 'Your chosen level: <b>A1-A2</b>', parse_mode='html')
                vocabulary_tests(message)
            elif message.text == 'B1-B2':
                bot.send_message(message.chat.id, 'Your chosen level: <b>B1-B2</b>', parse_mode = 'html')
                vocabulary_tests(message)
            elif message.text == 'C1-C2':
                bot.send_message(message.chat.id, 'Your chosen level: <b>C1-C2</b>', parse_mode = 'html')
                vocabulary_tests(message)
        elif message.text == 'Back':
            if len(user_topic_history[user_id]) > 0:
                user_topic_history[user_id].pop()
                if len(user_topic_history[user_id]) > 0:
                    message.text = user_topic_history[user_id][-1]
                else:
                    buttons_start(message)
        else:
            bot.send_message(message.chat.id, 'Please, choose one of the buttons below' , parse_mode = 'html')


bot.polling()
