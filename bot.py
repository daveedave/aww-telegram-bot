from telegram.ext import Updater, CommandHandler
import requests
import re
from bs4 import BeautifulSoup
import subprocess
import os

token = '<Insert Token here>'

def aww(bot, update):
    source_list = []
    url_list = []
    url = 'https://www.reddit.com/r/aww/'
    chat_id = update.message.chat_id
    page = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    
    sources = soup.findAll('source')
    bot.send_message(chat_id=chat_id, text="The top cutest Video on reddit are loading right now")
    
    for source in sources:
    
        source_list.append(source['src'])
    
    for urls in source_list:
        url_list.append('youtube-dl ' + urls)
    
    
    for i in range(len(url_list)-1):

        os.system(url_list[i])
    print("joooo")
    os.system(dl_string)
    print("nooooo")
    p = subprocess.Popen('find ./ -name "*.mp4"', stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = output.decode('utf-8')
    v = output.split('\n')
    print(v[0])
    for out in v:
        if(out !='./4kx5z41u72c31-4kx5z41u72c31.mp4'):
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
