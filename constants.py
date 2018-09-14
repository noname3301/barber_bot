from datetime import datetime,timedelta

import telebot
import locale

        #                                                      #w_u[1] #wk_u[2] #t_u[3]
        # const.data_user[message.chat.id] = [message.chat.id, False,  False,   False,
        #                                     #s_s[4]   #d_s[5]
        #                                     False,    False,
        #                                    #w_st[6]  #t_st[7]  #s_st[8]
        #                                    '',       '',       '']

locale.setlocale(locale.LC_ALL, "Russian")

#Имя пользователя
first_name = ""
last_name = ""

#Токен бота
token = ""

#Объявление бота
bot = telebot.TeleBot(token)

#id Главного пользователя(изменить!)
id = 427508080 #427508080 #428281929

#Недели для записи
now = datetime.now()
week_arr = []
for i in range(7):
    days = timedelta(1)   
    week_arr.append(now.strftime("%d %B(%A)"))
    now = now + days

#(True = записан, False = не записан)
write_user = False

# Куда пользователя направлять 
# при нажатии кнопкии назад
week_user = False
time_user = False

# Какие кнопки 
# в данный момент показывать
service_switch = False
day_switch = False

# Недели
week_string = ""

# Время
time_string = ""

# Услуги
service_string = ""

#Данные пользователя
# data_user = {'0000' : [0, False, False, False, 
#               False, False,  '', '', '']}
data_user = {}

#Понедельник
arr_1 = ['11:00', '12:00' , '13:00', '14:00']

#Вторник
arr_2 = []

#Среда
arr_3 = []

#Четверг
arr_4 = ['12:40', '15:00', '16:00']

#Пятница
arr_5 = ['15:00', '14:00', '16:00']

#Суббота
arr_6 = []

#Воскресенье
arr_7 = []
