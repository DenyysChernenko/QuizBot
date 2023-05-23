import telebot
import random
from telebot import types
BOT_TOKEN = '6036332987:AAHea3RMb_mSjNKPy2wCWeCpOWkN7HG1Kiw'
bot = telebot.TeleBot(BOT_TOKEN)
topic_history = []


question_counter = 1
correct_answers = 0
options = []
answer = ''
# Functions for tests



# Functions for tests


@bot.message_handler(func=lambda message: message == 'A1-A2')
def test_a1_a2(message):
    # bot.send_message(message.chat.id,'<b>CHECKKKKKKKKKK </b>', parse_mode='html')
    global question_counter
    global correct_answers
    global options
    global answer

    if question_counter >= 10:
        bot.send_message(message.chat.id, f'You have finished the test with {correct_answers} correct answers!')
        question_counter = 1
        correct_answers = 0
        options = []
        return

    with open('A1-A2.txt', 'r') as file:
        lines = file.readlines()
        index = random.randint(1, len(lines) // 2)
        index = index * 2 - 1 if index * 2 - 1 <= len(lines) else len(lines)


        if index <= len(lines):
            question = lines[index-1]
            options = lines[index].split(",")
            answer = options[0].strip()
            bot.send_message(message.chat.id, f'index - {index}')
            bot.send_message(message.chat.id, f'index - {len(lines)}')


            random.shuffle(options)

            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            answer_buttons = [telebot.types.KeyboardButton(option.strip()) for option in options]
            markup.add(*answer_buttons)
            markup.add('Back')

            bot.send_message(message.chat.id, f'{question_counter}. {question}', reply_markup=markup)
            bot.register_next_step_handler(message, handle_answer)


def handle_answer(message):
    global question_counter
    global correct_answers

    if message.text == answer:
        correct_answers += 1
        bot.reply_to(message, f'Correct answer! Correct answers: {correct_answers}✔️')
        test_a1_a2(message)
    elif message.text == 'Back':
        bot.send_message(message.chat.id, f'You have finished the test with {correct_answers} correct answers!')
        question_counter = 1
        correct_answers = 0
        return buttons_grammar(message)
    else:
        bot.reply_to(message, f'Wrong answer! Correct answers: {correct_answers}❌')
        bot.send_message(message.chat.id, f'Correct answer is: \"{answer}\"🕵️‍♂️')
        test_a1_a2(message)

    question_counter += 1
    if question_counter >= 10:
        bot.send_message(message.chat.id, f'You have finished the test with {correct_answers} correct answers!')
        question_counter = 1
        correct_answers = 0
        return buttons_grammar(message)


















# Functions
def help(message):
    choosen_option_message = 'You have chosen <b>Help</b> option!\n'
    help_message = (
        f"Hi, <b>{message.from_user.first_name}!</b> Our tasks are designed to improve your English grammar and vocabulary.\n"
        "Grammar will give you a solid understanding of the rules and structures that govern the English language.\n"
        "Vocabulary will give you a wide range of words and their meanings.\n"
        "Thanks a lot for using our quizbot.\n"
    )
    bot.send_message(message.chat.id, choosen_option_message, parse_mode='html')
    bot.send_message(message.chat.id, help_message, parse_mode='html')

def about_authors(message):
    choosen_option_message = 'You have chosen <b>About authors</b> option!\n'
    about_authors_message = (
                            f"We are the Ukranian students Denys and Ivan, who study not in Ukraine.\n"
                            f"We appreciate you for using our bot to learn English.\n" 
                            "English is fun!\n" )
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
    level_message = "Now, you must pich your current level of Engllish.\n"
    bot.send_message(message.chat.id, level_message, reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['Vocabulary learning'])
def buttons_vocabulary(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    first_level_button = types.KeyboardButton('A1-A2')
    second_level_button = types.KeyboardButton('B1-B2')
    third_level_button = types.KeyboardButton('C1-C2')
    back_button = types.KeyboardButton('Back')
    markup.add(first_level_button, second_level_button, third_level_button, back_button)
    choosen_option_message = f"You have chosen <b>Vocabulary learning.</b>\n"
    bot.send_message(message.chat.id, choosen_option_message, reply_markup=markup, parse_mode='html')
    level_message = "Now, you must pich your current level of Engllish.\n"
    bot.send_message(message.chat.id, level_message, reply_markup=markup, parse_mode='html')


# Parsing text
@bot.message_handler(content_types=['text'])
def buttons(message):
        if message.text == 'Help':
            help(message)
        elif message.text == 'About authors':
            about_authors(message)
        elif message.text == 'Grammar tests':
            topic_history.append('Grammar tests')
            buttons_grammar(message)
        elif topic_history and topic_history[-1] == 'Grammar tests' and message.text != 'Back':
            if message.text == 'A1-A2':
                bot.send_message(message.chat.id, 'Your chosen level: <b>A1-A2</b>', parse_mode='html')
                test_a1_a2(message)
            elif message.text == 'B1-B2':
                bot.send_message(message.chat.id, 'Your choosen level: <b>B1-B2</b>', parse_mode = 'html')
            elif message.text == 'C1-C2':
                bot.send_message(message.chat.id, 'Your choosen level: <b>C1-C2</b>', parse_mode = 'html')

            else:
                bot.send_message(message.chat.id, 'Please, choose one of the buttons below' , parse_mode = 'html')

        elif message.text == 'Vocabulary learning':
            topic_history.append('Vocabulary learning')
            buttons_vocabulary(message)
        elif topic_history and topic_history[-1] == 'Vocabulary learning' and message.text != 'Back':
            if message.text == 'A1-A2':
                bot.send_message(message.chat.id, 'Your choosen level: <b>A1-A2</b>', parse_mode = 'html')
            elif message.text == 'B1-B2':
                bot.send_message(message.chat.id, 'Your choosen level: <b>B1-B2</b>', parse_mode = 'html')
            elif message.text == 'C1-C2':
                bot.send_message(message.chat.id, 'Your choosen level: <b>C1-C2</b>', parse_mode = 'html')
            else:
                bot.send_message(message.chat.id, 'Please, choose one of the buttons below', parse_mode='html')
        elif message.text == 'Back':
            if len(topic_history) > 0:
                topic_history.pop()
                if len(topic_history) > 0:
                    message.text = topic_history[-1]
                else:
                    buttons_start(message)
        else:
            bot.send_message(message.chat.id, 'Please, choose one of the buttons below' , parse_mode = 'html')


bot.polling()