# exchange bot 2.5

import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
import sqlite3
from datetime import datetime
TOKEN = '5040171237:AAEIY10mURQmP9OHvAWTchIhR6BdIF8ZQDg'
bot = telebot.TeleBot(TOKEN)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}


x = datetime.now()

connect = sqlite3.connect('users.db', check_same_thread=False)
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
    id INTEGER,
    name TEXT,
    data TEXT
)""")
connect.commit()


def crypto(input, output):
    try:
        if input.lower():
            input = input.upper()
        if output.lower():
            output = output.upper()

        r = requests.get(f"https://finance.yahoo.com/quote/{input}-{output}", headers=headers)
        html = BS(r.text, 'html.parser')
        crypto = html.find('fin-streamer',class_="Fw(b) Fz(36px) Mb(-4px) D(ib)")
        if input == 'BTC' or input == 'ETH':
            split = crypto.text.split('.')
            cryptocurrency = float(split[0].replace(',', ''))

            return cryptocurrency
        else:
            return crypto.text
    except AttributeError:
        bot.send_message(types.Message, "error")


def currency(input, output):
    try:
        if input.upper():
            input = input.lower()
        if output.upper():
            output = output.lower()
        r = requests.get(f'https://wise.com/gb/currency-converter/{input}-to-{output}-rate', headers=headers)
        html = BS(r.text, 'html.parser')
        currency = html.find('span',class_="text-success")
        return currency.text
    except AttributeError:
        bot.send_message(types.Message, "error")


@bot.message_handler(commands=['start'])
def start(message):
    # database
    people_iid = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_iid}")
    data = cursor.fetchone()
    if data is None:
        users_id = [ message.chat.id, "{0.first_name}".format(message.from_user), str(str(x.year) + '-' + str(x.month) +'-'+ str(x.day))]
        cursor.execute("INSERT INTO login_id VALUES(?,?,?);", users_id)
        connect.commit()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Crypto Exchange')
        item2 = types.KeyboardButton('Currency Exchange')
        markup.add(item1, item2, )
        bot.send_message(message.chat.id, "Hello {0.first_name}".format(message.from_user), reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Crypto Exchange')
        item2 = types.KeyboardButton('Currency Exchange')
        markup.add(item1, item2, )
        bot.send_message(message.chat.id, "Hello {0.first_name}".format(message.from_user), reply_markup=markup)
    

# function for inline buttons
def inline_burtton(message_id, funtion):
    msg =bot.send_message(message_id, 'The amount of your money')
    bot.register_next_step_handler(msg, funtion)


@bot.message_handler(content_types=['text'])

def bot_message(message):

    if message.chat.type =='private':
        # cryptoexchange
        if message.text == 'Crypto Exchange':
            markupcrypto=types.ReplyKeyboardMarkup(resize_keyboard=True)
            BTCexchange=types.KeyboardButton("Bitcoin Exchange")
            Dogeexchange=types.KeyboardButton("Dogecoin Exchange")
            Chiaexchange=types.KeyboardButton("Chia Exchange")
            Litecoinexchange=types.KeyboardButton("Litecoin Exchange")
            Dashexchange=types.KeyboardButton("Dash Exchange")
            Tronexcahange = types.KeyboardButton("Tron Exchange")
            BTCexchange=types.KeyboardButton("Bitcoin Exchange")
            backtoexchange = types.KeyboardButton('Back')
            bttexchange = types.KeyboardButton("Bittorrent Exchange")
            morecrypto = types.KeyboardButton('More Crypto')
            markupcrypto.add(BTCexchange,Dogeexchange ,Chiaexchange , Litecoinexchange, Dashexchange,Tronexcahange,bttexchange , morecrypto, backtoexchange)
            bot.send_message(message.chat.id, "Crypto Exchange", reply_markup=markupcrypto, )
        # btc
        elif message.text == 'Bitcoin Exchange':
            BTCinline = types.InlineKeyboardMarkup()
            BTCTOUSD=types.InlineKeyboardButton(text='BTC to USD',callback_data='BTC to USD')
            BTCTOEURO=types.InlineKeyboardButton(text='BTC to EURO',callback_data='BTC to EURO')
            BTCTORUB=types.InlineKeyboardButton(text='BTC to RUB',callback_data='BTC to RUB')
            BTCinline.add(BTCTOUSD,BTCTOEURO,BTCTORUB,)
            bot.send_message(message.chat.id, "Bitcoin Exchange", reply_markup=BTCinline, )
        # Doge
        elif message.text == 'Dogecoin Exchange':
            DOGEinline = types.InlineKeyboardMarkup()
            DOGETOUSD=types.InlineKeyboardButton(text='DOGE to USD',callback_data='DOGE to USD' )
            DOGETOEURO=types.InlineKeyboardButton(text='DOGE to EURO',callback_data='DOGE to EURO')
            DOGETORUB=types.InlineKeyboardButton(text='DOGE to RUB',callback_data='DOGE to RUB')
            DOGEinline.add(DOGETOUSD,DOGETOEURO,DOGETORUB,)
            bot.send_message(message.chat.id, "Dogecoin Exchange", reply_markup=DOGEinline, )
        # Chia
        elif message.text == 'Chia Exchange':
            CHIAinline = types.InlineKeyboardMarkup()
            CHIATOUSD=types.InlineKeyboardButton(text='Chia to USD',callback_data='Chia to USD')
            CHIATOEURO=types.InlineKeyboardButton(text='Chia to EURO',callback_data='Chia to EURO')
            CHIATORUB=types.InlineKeyboardButton(text='Chia to RUB',callback_data='Chia to RUB')
            CHIAinline.add(CHIATOUSD,CHIATOEURO,CHIATORUB,)
            bot.send_message(message.chat.id, "Chia Exchange", reply_markup=CHIAinline, )
        # Litecoin
        elif message.text == 'Litecoin Exchange':
            Litecoininline = types.InlineKeyboardMarkup()
            LitecoinTOUSD=types.InlineKeyboardButton(text='Litecoin to USD',callback_data='Litecoin to USD')
            LitecoinTOEURO=types.InlineKeyboardButton(text='Litecoin to EURO',callback_data='Litecoin to EURO')
            LitecoinTORUB=types.InlineKeyboardButton(text='Litecoin to RUB',callback_data='Litecoin to RUB')
            Litecoininline.add(LitecoinTOUSD,LitecoinTOEURO,LitecoinTORUB,)
            bot.send_message(message.chat.id, "Litecoin Exchange", reply_markup=Litecoininline, )
        # Dash
        elif message.text == 'Dash Exchange':
            Dashinline = types.InlineKeyboardMarkup()
            DashTOUSD=types.InlineKeyboardButton(text='Dash to USD',callback_data= 'Dash to USD')
            DashTOEURO=types.InlineKeyboardButton(text='Dash to EURO',callback_data='Dash to EURO')
            DashTORUB=types.InlineKeyboardButton(text='Dash to RUB',callback_data='Dash to RUB')
            Dashinline.add(DashTOUSD,DashTOEURO,DashTORUB,)
            bot.send_message(message.chat.id, "Dash Exchange", reply_markup=Dashinline, )
        # Tron Exchange
        elif message.text == 'Tron Exchange':
            Troninline = types.InlineKeyboardMarkup()
            TronTOUSD=types.InlineKeyboardButton(text='Tron to USD',callback_data='Tron to USD')
            TronTOEURO=types.InlineKeyboardButton(text='Tron to EURO',callback_data='Tron to EURO')
            TronTORUB=types.InlineKeyboardButton(text='Tron to RUB',callback_data='Tron to RUB')
            Troninline.add(TronTOUSD,TronTOEURO,TronTORUB,)
            bot.send_message(message.chat.id, "Tron Exchange", reply_markup=Troninline, )
        # Btt
        elif message.text == 'Bittorrent Exchange':
            Troninline = types.InlineKeyboardMarkup()
            BTTTOUSD=types.InlineKeyboardButton(text='BTT to USD',callback_data='BTT to USD')
            BTTTORUB=types.InlineKeyboardButton(text='BTT to RUB',callback_data='BTT to RUB')
            BTTTOEUR=types.InlineKeyboardButton(text='BTT to EUR0',callback_data='BTT to EURO')
            Troninline.add(BTTTOUSD,BTTTOEUR,BTTTORUB)
            bot.send_message(message.chat.id, "BTT Exchange", reply_markup=Troninline, )

        # Currency Exchange
        elif message.text == 'Currency Exchange':
            markupCurrency=types.ReplyKeyboardMarkup(resize_keyboard=True)
            USDEXCHANGE=types.KeyboardButton("USD Exchange")
            EUROEXCHANGE=types.KeyboardButton("EURO Exchange")
            RUBEXCHANGE=types.KeyboardButton("RUB Exchange")
            AMDEXCHANGE=types.KeyboardButton("AMD Exchange")
            backtoexchange = types.KeyboardButton('Back')
            morecurrency = types.KeyboardButton('More Currency')
            markupCurrency.add(USDEXCHANGE,EUROEXCHANGE ,RUBEXCHANGE , AMDEXCHANGE, morecurrency,backtoexchange )
            bot.send_message(message.chat.id, "Currency Exchange", reply_markup=markupCurrency, )
        # USD
        elif message.text == 'USD Exchange':
            USDinline = types.InlineKeyboardMarkup()
            USDTORUB=types.InlineKeyboardButton(text='USD to RUB', callback_data='USD to RUB')
            USDTOEURO=types.InlineKeyboardButton(text='USD to EURO',callback_data='USD to EURO')
            USDTOAMD=types.InlineKeyboardButton(text='USD to AMD',callback_data='USD to AMD')
            USDinline.add(USDTORUB,USDTOEURO,USDTOAMD,)
            bot.send_message(message.chat.id, "USD Exchange", reply_markup=USDinline, )
        # EURO
        elif message.text == 'EURO Exchange':
            EUROinline = types.InlineKeyboardMarkup()
            EUROTORUB=types.InlineKeyboardButton(text='EURO to RUB',callback_data='EURO to RUB')
            EUROTOUSD=types.InlineKeyboardButton(text='EURO to USD',callback_data='EURO to USD')
            EUROTOAMD=types.InlineKeyboardButton(text='EURO to AMD',callback_data='EURO to AMD')
            EUROinline.add(EUROTORUB,EUROTOUSD,EUROTOAMD,)
            bot.send_message(message.chat.id, "EURO Exchange", reply_markup=EUROinline, )
        # RUB
        elif message.text == 'RUB Exchange':
            RUBinline = types.InlineKeyboardMarkup()
            RUBTOUSD=types.InlineKeyboardButton(text='RUB to USD',callback_data= 'RUB to USD')
            RUBTOEURO=types.InlineKeyboardButton(text='RUB to EURO',callback_data='RUB to EURO')
            RUBTOAMD=types.InlineKeyboardButton(text='RUB to AMD',callback_data='RUB to AMD')
            RUBinline.add(RUBTOUSD,RUBTOEURO,RUBTOAMD,)
            bot.send_message(message.chat.id, "RUB Exchange", reply_markup=RUBinline, )
        # AMD
        elif message.text == 'AMD Exchange':
            AMDinline = types.InlineKeyboardMarkup()
            AMDTOUSD=types.InlineKeyboardButton(text='AMD to USD', callback_data='AMD to USD')
            AMDTOEURO=types.InlineKeyboardButton(text='AMD to EURO',callback_data='AMD to EURO')
            AMDTORUB=types.InlineKeyboardButton(text='AMD to RUB',callback_data='AMD to RUB')
            AMDinline.add(AMDTOUSD,AMDTOEURO,AMDTORUB,)
            bot.send_message(message.chat.id, "AMD Exchange", reply_markup=AMDinline, )

        # back to exchange
        #  backtoexchange = types.KeyboardButton('backtoexchange')
        elif message.text == 'Back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            CRYPTO=types.KeyboardButton("Crypto Exchange")
            currency=types.KeyboardButton("Currency Exchange")
            markup.add(CRYPTO,currency,)
            bot.send_message(message.chat.id, "Back", reply_markup=markup)

        elif message.text == "More Crypto":
            msg = bot.send_message(message.chat.id, "Input Crypto",)
            bot.register_next_step_handler(msg, process_crypto_step)

        elif message.text == "More Currency":
        # process_currency1_step
            msg = bot.send_message(message.chat.id, "Input Currency",)
            bot.register_next_step_handler(msg, process_currency1_step)
        # else
        else:
            bot.send_message(message.chat.id, text="I do not understand what you want from me")

        @bot.callback_query_handler(func=lambda call:True)
        def callback_inline(call):
            if call.message:
                 # BTC
                if call.data == 'BTC to USD':
                    inline_burtton(call.message.chat.id, btctousd)
                elif call.data == 'BTC to EURO':
                    inline_burtton(call.message.chat.id, btctoeur)
                elif call.data == 'BTC to RUB':
                    inline_burtton(call.message.chat.id, btctorub)
                # BTT
                elif call.data == 'BTT to USD':
                    inline_burtton(call.message.chat.id, btttousd)
                elif call.data == 'BTT to EURO':
                    inline_burtton(call.message.chat.id, btttoeur)
                elif call.data == 'BTT to RUB':
                    inline_burtton(call.message.chat.id, btttorub)
                # Doge
                elif call.data == 'DOGE to USD':
                    inline_burtton(call.message.chat.id, dogetousd)
                elif call.data == 'DOGE to EURO':
                    inline_burtton(call.message.chat.id, dogetoeur)
                elif call.data == 'DOGE to RUB':
                    inline_burtton(call.message.chat.id, dogetorub)
                # Chia   
                elif call.data == 'Chia to USD':
                    inline_burtton(call.message.chat.id, chiatousd)
                elif call.data == 'Chia to EURO':
                    inline_burtton(call.message.chat.id, chiatoeur)
                elif call.data == 'Chia to RUB':
                    inline_burtton(call.message.chat.id, chiatorub)
                # Litecoin   
                elif call.data == 'Litecoin to USD':
                    inline_burtton(call.message.chat.id, litetousd)
                elif call.data == 'Litecoin to EURO':
                    inline_burtton(call.message.chat.id, litetoeur)
                elif call.data == 'Litecoin to RUB':
                    inline_burtton(call.message.chat.id, litetorub)
                # Dash   
                elif call.data == 'Dash to USD':
                    inline_burtton(call.message.chat.id, dashtousd)
                elif call.data == 'Dash to EURO':
                    inline_burtton(call.message.chat.id, dashtoeur)
                elif call.data == 'Dash to RUB':
                    inline_burtton(call.message.chat.id, dashtorub)
                # Tron   
                elif  call.data == 'Tron to USD':
                    inline_burtton(call.message.chat.id, trontousd)
                elif  call.data == 'Tron to EURO':
                    inline_burtton(call.message.chat.id, trontoeur)
                elif  call.data == 'Tron to RUB':
                    inline_burtton(call.message.chat.id, trontorub)
                # Euro    
                elif  call.data == 'EURO to RUB':
                    inline_burtton(call.message.chat.id, eurptorub)
                elif   call.data == 'EURO to USD':
                    inline_burtton(call.message.chat.id, eurotousd)
                elif  call.data == 'EURO to AMD':
                    inline_burtton(call.message.chat.id, eurotoamd)
                #  RUB   
                elif   call.data == 'RUB to USD':
                    inline_burtton(call.message.chat.id, rubtousd)
                elif   call.data == 'RUB to EURO':
                    inline_burtton(call.message.chat.id, rubtoeur)
                elif   call.data == 'RUB to AMD':
                    inline_burtton(call.message.chat.id, rubtoamd)
                # AMD   
                elif  call.data == 'AMD to USD':
                    inline_burtton(call.message.chat.id, amdtousd)
                elif  call.data == 'AMD to EURO':
                    inline_burtton(call.message.chat.id, amdtoeur)
                elif  call.data == 'AMD to RUB':
                    inline_burtton(call.message.chat.id, amdtorub)
                # Dollar   
                elif call.data == 'USD to RUB':
                    inline_burtton(call.message.chat.id, usdtorub)
                elif  call.data == 'USD to EURO':
                    inline_burtton(call.message.chat.id, usdtoeur)
                elif  call.data == 'USD to AMD':
                    inline_burtton(call.message.chat.id, usdtoamd)

# examination float     
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# examination int
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False 

# function for crypto
def exchnage(message_text,input_crypto, input_currency, function, message) :
    chat_id = message.chat.id
    if is_float(message_text) == True or is_int(message_text) == True:
        res = float(message_text) * float(crypto(input_crypto, input_currency))
        bot.send_message(chat_id, res)

    elif is_float(message_text) == False or is_int(message_text) == False:
        bot.send_message(chat_id, "error")

        msg =bot.send_message(chat_id, 'The amount of your money')
        bot.register_next_step_handler(msg, function)

# function for currency
def exchange_currency(message_text,input_currency, output_currency, function, message):
    chat_id = message.chat.id
    if is_float(message_text) == True or is_int(message_text) == True:
        res = float(message_text) * float(currency(input_currency, output_currency))
        bot.send_message(chat_id, res)

    elif is_float(message_text) == False or is_int(message_text) == False:
        bot.send_message(chat_id, "error")


        msg =bot.send_message(chat_id, 'The amount of your money')
        bot.register_next_step_handler(msg,function )

# BTC 
def btctousd (message):
    exchnage(message.text,'btc', 'usd',btctousd ,message)


def btctoeur(message):
    exchnage(message.text,'btc', 'eur',btctoeur ,message)


def btctorub(message):
    exchnage(message.text,'btc', 'rub',btctorub ,message)


# BTT
def btttousd(message):
    exchnage(message.text,'BTT1', 'usd',btttousd ,message)


def btttoeur (message):
    exchnage(message.text,'BTT1', 'eur',btttoeur ,message)


def btttorub (message):
    exchnage(message.text,'BTT1', 'rub',btttorub ,message)
     

# Doge
def dogetousd(message):
    exchnage(message.text,'doge', 'usd',dogetousd ,message)


def dogetoeur(message):
    exchnage(message.text,'doge', 'eur',dogetoeur ,message)


def dogetorub(message):
    exchnage(message.text,'doge', 'rub',dogetorub ,message)


# Litecoin
def litetousd(message):
    exchnage(message.text,'ltc', 'usd',litetousd ,message)


def litetoeur(message):
    exchnage(message.text,'ltc', 'eur',litetoeur ,message)


def litetorub(message):
    exchnage(message.text,'ltc', 'rub',litetorub ,message)


# Dash
def dashtousd(message):
    exchnage(message.text,'dash', 'usd',dashtousd ,message)


def dashtoeur(message):
    exchnage(message.text,'dash', 'eur',dashtoeur ,message)

def dashtorub(message):
    exchnage(message.text,'dash', 'rub',dashtorub ,message)


# TRX
def trontousd(message):
    exchnage(message.text,'TRX', 'usd',trontousd ,message)


def trontoeur(message):
    exchnage(message.text,'TRX', 'eur',trontoeur ,message)


def trontorub(message):
    exchnage(message.text,'TRX', 'rub',trontorub ,message)


# chia
def chiatousd(message):
    exchnage(message.text,'XCH', 'usd',chiatousd ,message)


def chiatoeur(message):
    exchnage(message.text,'XCH', 'eur',chiatoeur ,message)


def chiatorub(message):
    exchnage(message.text,'XCH', 'rub',chiatorub ,message)


# usd
def usdtoamd(message):
    exchange_currency(message.text,'usd', 'amd', usdtoamd, message)


def usdtoeur(message):
    exchange_currency(message.text,'usd', 'eur', usdtoeur, message)


def usdtorub(message):
    exchange_currency(message.text,'usd', 'rub', usdtorub, message)


# eur
def eurotousd(message):
    exchange_currency(message.text,'eur', 'usd', eurotousd, message)


def eurotoamd(message):
    exchange_currency(message.text,'eur', 'amd', eurotoamd, message)


def eurptorub(message):
    exchange_currency(message.text,'eur', 'rub', eurptorub, message)


# rub
def rubtoamd(message):
    exchange_currency(message.text,'rub', 'amd', rubtoamd, message)


def rubtousd(message):
    exchange_currency(message.text,'rub', 'usd', rubtousd, message)


def rubtoeur(message):
    exchange_currency(message.text,'rub', 'eur', rubtoeur, message)


# amd
def amdtoeur(message):
    exchange_currency(message.text,'amd', 'eur', amdtoeur, message)


def amdtousd(message):
    exchange_currency(message.text,'amd', 'usd', amdtousd, message)


def amdtorub(message):
    exchange_currency(message.text,'amd', 'rub', amdtorub, message)


# crypto more algoritm

crypto_more = ''
currency_more = ''
amount_more = ''



def process_crypto_step(message):
    global crypto_more

    crypto_more = message.text


    msg = bot.send_message(message.chat.id, "Input Currency ")
    bot.register_next_step_handler(msg, process_currency_step)
    

def process_currency_step(message):

    global currency_more
   
    currency_more = message.text

    msg = bot.send_message(message.chat.id, "Amount ")
    bot.register_next_step_handler(msg, process_amount_step)

def process_amount_step(message):

    global crypto_more, currency_more, amount_more

    if is_float(message.text) == True or is_int(message.text) == True:

        amount_more = float(message.text)
        res = float(amount_more) * float(crypto(crypto_more, currency_more))
        bot.send_message(message.chat.id, res)

    elif is_float(message.text) == False or is_int(message.text) == False:
        bot.send_message(message.chat.id, "error")

# currency more algoritm

currency1_more = ''
currency2_more = ''
currency_amount_more = ''


def process_currency1_step(message):
    global currency1_more

    
    currency1_more = message.text


    msg = bot.send_message(message.chat.id, "Input Currency ")
    bot.register_next_step_handler(msg, process_currency2_step)


def process_currency2_step(message):

    global currency2_more

    currency2_more = message.text

    msg = bot.send_message(message.chat.id, "Amount")
    bot.register_next_step_handler(msg, process_currency_amount_step)


def process_currency_amount_step(message):

    global currency_amount_more, currency1_more, currency2_more

    if is_float(message.text) == True or is_int(message.text) == True:
        currency_amount_more = float(message.text)
        
        res = float(currency_amount_more) * float(currency(currency1_more, currency2_more))

        bot.send_message(message.chat.id, res)

    elif is_float(message.text) == False or is_int(message.text) == False:
        bot.send_message(message.chat.id, "error")

bot.polling(non_stop=True)
