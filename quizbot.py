import telebot
from telebot import types
topic_history = []



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
                bot.send_message(message.chat.id, 'Your choosen level: A1-A2')
            elif message.text == 'B1-B2':
                bot.send_message(message.chat.id, 'Your choosen level: B1-B2')
            elif message.text == 'C1-C2':
                bot.send_message(message.chat.id, 'Your choosen level: C1-C2')
            else:
                bot.send_message(message.chat.id, 'Please, choose one of the buttons below' , parse_mode = 'html')

        elif message.text == 'Vocabulary learning':
            topic_history.append('Vocabulary learning')
            buttons_vocabulary(message)
        elif topic_history and topic_history[-1] == 'Vocabulary learning' and message.text != 'Back':
            if message.text == 'A1-A2':
                bot.send_message(message.chat.id, 'Your choosen level: A1-A2')
            elif message.text == 'B1-B2':
                bot.send_message(message.chat.id, 'Your choosen level: B1-B2')
            elif message.text == 'C1-C2':
                bot.send_message(message.chat.id, 'Your choosen level: C1-C2')
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
