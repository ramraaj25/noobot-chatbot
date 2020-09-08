from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import playsound
from gtts import gTTS
import logging
from train import get_latest_response
from train import bot
from chatterbot.conversation import Statement
import os
from chatterbot import utils

ip = input(">>>")
reply_num = 0
while ip.lower() != 'bye':
    bot_reply = bot.get_response(ip)

    bot_reply = bot_reply.text

    speech = gTTS(text=bot_reply, lang='en', slow=False)
    speech.save(f'reply{reply_num}.mp3')

    playsound.playsound(f'reply{reply_num}.mp3')
    reply_num += 1

    if bot_reply == 'I am sorry, but I do not understand.':
        res = input("Do you want to record your own response?(Y/N)")
        if res.lower() == 'y':
            text = input("Enter your response: ")
            improved_statement = Statement(
                text, in_response_to=ip, storage=bot.storage)
            improved_statement.save()

    ip = input(">>>")

    if ip == '!feedback':
        text = input("Enter your response: ")
        feedback = Statement(text, in_response_to=ip, storage=bot.storage)
        print(feedback.text)
        feedback.save()
        ip = input(">>>")

for filename in os.listdir("./"):
    if filename.startswith("reply"):
        os.remove(filename)
