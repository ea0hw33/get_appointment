import telebot 
from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_filters
from telebot.asyncio_handler_backends import State, StatesGroup
from telebot.asyncio_storage import StateMemoryStorage
from telebot import types
import asyncio

from main import *

sudo_user = 634351006 # telegram ID
authorized = False

bot = AsyncTeleBot('BOT_TOCKENT', state_storage=StateMemoryStorage())

class MyStates(StatesGroup):
    sms_code = State()

@bot.message_handler(commands = ["start"])   
async def start(message):
    if int(message.from_user.id) == sudo_user:
        await bot.send_message(message.from_user.id, text = "i'm alive, trying to login")
        authforportal38(LOGIN, PASSWORD)
        await bot.send_message(message.from_user.id, text = "done")
        while True:
            try:
                msg = get_status()
                if msg is not None:
                    await bot.send_message(message.from_user.id, text = msg)
            except Exception as e:
                await bot.send_message(message.from_user.id, text = type(e).__name__)
                break
            
@bot.message_handler(state=MyStates.sms_code)
async def ask_sms_code(message):
    code = None
    
    # await bot.send_message(message.chat.id, "code1")

    code = message.text
        
    loginform = driver.find_element(By.XPATH, "/html/body/esia-root/div/esia-login/div/div/esia-enter-mfa/esia-otp/div/form/div/esia-code-input/div/code-input/span[1]/input")
    loginform.send_keys(code)
    sleep(5)
 
    await bot.delete_state(message.from_user.id, message.chat.id)

    while True:
            msg = get_status()
            if msg is not None:
                if msg == 'need to login again':
                    await bot.send_message(message.from_user.id, text = msg)
                    break
                await bot.send_message(message.from_user.id, text = msg)
                
        
              
async def auth1(message):
    driver.get("https://esia.gosuslugi.ru/login/")
    code = None
    
    sleep(5)
    try:
        loginform = driver.find_element(By.ID, "login")
        loginform.send_keys(LOGIN + Keys.TAB + PASSWORD + Keys.ENTER)
    except Exception as e:
        print(type(e).__name__)
        loginform = driver.find_element(By.ID, "password")
        loginform.send_keys(PASSWORD + Keys.ENTER)
    
    sleep(5)
    
    if driver.current_url == 'https://esia.gosuslugi.ru/login/': 
        return await bot.send_message(message.chat.id, "check the code")
    else:
        await bot.send_message(message.chat.id, "auth done")
        while True:
            msg = get_status()
            if msg is not None:
                if msg == 'need to login again':
                    await bot.send_message(message.from_user.id, text = msg)
                    break
                await bot.send_message(message.from_user.id, text = msg)
        return message

bot.add_custom_filter(asyncio_filters.StateFilter(bot))
bot.add_custom_filter(asyncio_filters.IsDigitFilter())        
 

asyncio.run(bot.infinity_polling(timeout=60))
