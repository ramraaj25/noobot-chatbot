from chatterbot import ChatBot
from train import list_trainer
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


print(bot.storage.tagger.get_bigram_pair_string("where do you live"))

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
                text, in_response_to=ip, storage=bot.storage, search_in_response_to=bot.storage.tagger.get_bigram_pair_string(text))
            improved_statement.save()

    inp = input(">>>")

    if inp == '!feedback':
        text = input("Enter your response: ")
        feedback = Statement(text, in_response_to=ip, storage=bot.storage,
                             search_in_response_to=bot.storage.tagger.get_bigram_pair_string(text), conversation='training')
        print(feedback.text)
        feedback.save()

        # list_trainer.train([ip, text])
        print("Thank you for your contribution.")

        ip = input(">>>")
    else:
        ip = inp

for filename in os.listdir("./"):
    if filename.startswith("reply"):
        os.remove(filename)
