from telegram.ext import Updater, CommandHandler
import requests
import re
from bs4 import BeautifulSoup
import subprocess
import os

token = '<Insert Token Here>'

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
    
    #os.system(dl_string)
    
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


def doggo(bot, update):
    url = get_url('https://random.dog/woof.json')
    chat_id = update.message.chat_id
    print(url)
    if url[-4:] == '.jpg' or url[-4:] == '.png':
        
        bot.send_photo(chat_id=chat_id, photo=url)
    else:
        bot.send_video(chat_id=chat_id, video=url, supports_streaming=True)    

    print("Dog Sent")

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def main():
    global token
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('aww',aww))
    dp.add_handler(CommandHandler('doggo',doggo))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
