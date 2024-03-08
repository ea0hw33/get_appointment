async def auth (message):
#     driver.get("https://esia.gosuslugi.ru/login/")
#     code = None
    
#     sleep(5)

#     loginform = driver.find_element(By.ID, "login")
#     loginform.send_keys(LOGIN + Keys.TAB + PASSWORD)
#     await bot.send_message(message.chat.id, "code")
#     await bot.set_state(message.from_user.id, MyStates.sms_code, message.chat.id)
    
#     async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         try:
#             print(data['sms_code'])
#             code = int(data['sms_code'])
#         except ValueError:
#             await bot.send_message(message.from_user.id, text = "invalid value, send code again")
#             await bot.set_state(message.from_user.id, MyStates.sms_code, message.chat.id)
        
#     loginform = driver.find_element(By.XPATH, "/html/body/esia-root/div/esia-login/div/div/esia-enter-mfa/esia-otp/div/form/div/esia-code-input/div/code-input/span[1]/input")
#     loginform.send_keys(code)
        