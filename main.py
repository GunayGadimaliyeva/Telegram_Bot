API_KEY = '5605322705:AAFRK5nsOGpn_gFProzXoeGfP-g4QI9XMd4'
from telegram.ext import *
from telegram import *
import responses as R
from requests_html import HTML, HTMLSession
import telebot
from telebot import types



session = HTMLSession()

r = session.get('https://technest.idda.az/')
section = r.html.find('section')[2]
section2 = r.html.find('section')[7]
institutions =  section2.find('.slider__item a')
names =  section2.find('.slider__item a img')
specialties = section.find('.main__list--item')
print('Bot started...')

def start_command(update, context):
    update.message.reply_text(
    'Technest bot-a xoş gəlmisən!',
    reply_markup=ReplyKeyboardMarkup([
        [KeyboardButton('/name')],
        [KeyboardButton('/help')],
    ])
    )
    

def help_command(update, context):
    update.message.reply_text(
    'Əvvəlcə Technest təqaüdçüsü olub olmadığını öyrənməliyəm :)',
    reply_markup=ReplyKeyboardMarkup([
        [KeyboardButton("/yesIam")],
        [KeyboardButton('/wanttobe')],
    ])
)

def askname_command(update, context):
    user = update.message.chat['first_name']
    update.message.reply_text(f'Salam,{user}!\nAdım Technest bot-dur.Tanış olmağımıza sevindim! Canlı deyiləm, bu səbəbdən xəstələnmirəm, yatmıram, sorğuları cavabsız qoymuram. Ən əsası 24/7 sənə xidmət etmək üçün buradayam.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)
    
    
def options_command(update, context):
    update.message.reply_text(
        'Əla. Demək ki, sən də ekosistem oyunçularından birinə çevrilmisən.',
    reply_markup=ReplyKeyboardMarkup([
        [KeyboardButton('/enterCV')],
        [KeyboardButton('/vacancies')],
        [KeyboardButton('/specialities')],
        [KeyboardButton('/institutions')],
    ])
    )

def instutions_command(update, context):
    markup =[]
    for i in range(len(institutions)):
        markup = markup + [ InlineKeyboardButton(text=names[i].attrs['alt'], url=' '.join((institutions[i].absolute_links)))]
        
    update.message.reply_text(
        'Təhsil almaq istədiyin mərkəzi seç:',
        reply_markup = InlineKeyboardMarkup([markup])
    )
    

    
def speciality_command(update, context):
    markup =[]
    for i in range(len(specialties)):
        markup = markup + [ InlineKeyboardButton(text=(specialties[i].text).split('-')[0], url='https://docs.google.com/forms/d/e/1FAIpQLSces3KXHF9rtGSON9i_CUjZYQyw4rFvmLRBXNE7HeXQRanFww/viewform')]
        
    update.message.reply_text(
        'Təhsil almaq istədiyin ixtisası seç:',
        reply_markup = InlineKeyboardMarkup([markup])
    )


def wish_command(update, context):
    update.message.reply_text(
    'Möhtəşəm! Gözəl seçimdir! Technest haqqında məlumatın var mı?',
    reply_markup=ReplyKeyboardMarkup([
        [KeyboardButton('/yes',)],
        [KeyboardButton('/no')],
    ])
    )

def apply_command(update, context):
    update.message.reply_text(
    'Əla! Elə isə sənə uyğun olan təqaüd proqramına müraciət et!', 
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Go to the applicaion form', url='https://docs.google.com/forms/d/e/1FAIpQLSces3KXHF9rtGSON9i_CUjZYQyw4rFvmLRBXNE7HeXQRanFww/viewform')],
    ])
)

def info_command(update, context):
    update.message.reply_text(
    'Linkə keçid edərək məlumat əldə edə bilərsən!', 
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Go to the website', url='https://technest.idda.az/')],
    ])
)
def error (update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('name', askname_command))
    dp.add_handler(CommandHandler("yesIam",options_command))
    dp.add_handler(CommandHandler('institutions',instutions_command))
    dp.add_handler(CommandHandler('specialities',speciality_command))
    dp.add_handler(CommandHandler('wanttobe',wish_command))
    dp.add_handler(CommandHandler('yes',apply_command))
    dp.add_handler(CommandHandler('no',info_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))






    # dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

