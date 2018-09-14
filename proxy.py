from telebot import apihelper,types

#Прокси для обхода блокировки
ip = '127.0.0.1'
port = '9050'

apihelper.proxy = {
  'https': 'socks5://{}:{}'.format(ip,port)
}
