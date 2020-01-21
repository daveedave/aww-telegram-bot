from telegram.ext import Updater, CommandHandler
import requests
import re
from bs4 import BeautifulSoup
import subprocess
import os

token = '<Insert Token here>'

def aww(bot, update):
    source_list = []
    url = 'https://www.reddit.com/r/aww/'
    chat_id = update.message.chat_id
    page = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    #top_source = soup.find('source')
    sources = soup.findAll('source')
    bot.send_message(chat_id=chat_id, text="The top cutest Video on reddit are loading right now")
    #dl_string ='youtube-dl ' + top_source['src']
    for source in sources:
    
        source_list.append(source['src'])
    
    dl_string ='youtube-dl ' + source_list[1]
    print("joooo")
    os.system(dl_string)
    print("nooooo")
    p = subprocess.Popen('find ./ -name "*.mp4"', stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = output.decode('utf-8')
    v = output.split('\n')
    print(v[0])
    for out in v:
        if len(out)>=5:
            bot.send_video(chat_id=chat_id, video=open(out, 'rb'), supports_streaming=True)    
    print("aww")


def main():
    global token
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('aww',aww))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
