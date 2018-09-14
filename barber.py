import re

from telebot import apihelper,types

import constants as const
from constants import bot
import proxy


# Посылает дату и время записи человека 
def get(message, service, date_user, time_user):
    size = int(len(date_user) - 1)

    #Понедельник
    if date_user[size:-6:-1] == ')кинь':
        j = 0
        for i in const.arr_1:
             if time_user == i:
                const.arr_1.pop(j)
             j = j + 1
     #Вторник
    elif date_user[size:-6:-1] == ')кинр':
        j = 0
        for i in const.arr_2:
            if time_user == i:
                const.arr_2.pop(j)
            j = j + 1
    #Среда
    elif date_user[size:-6:-1] == ')адер':
        j = 0
        for i in const.arr_3:
            if time_user == i:
                const.arr_3.pop(j)
            j = j + 1
    #Четверг
    elif date_user[size:-6:-1] == ')грев':
        j = 0
        for i in const.arr_4:
            if time_user == i:
                const.arr_4.pop(j)
            j = j + 1
    #Пятница
    elif date_user[size:-6:-1] == ')ацин':
        j = 0
        for i in const.arr_5:
            if time_user == i:
                const.arr_5.pop(j)
            j = j + 1
    #Суббота
    elif date_user[size:-6:-1] == ')атоб':
        j = 0
        for i in const.arr_6:
            if time_user == i:
                const.arr_6.pop(j)
            j = j + 1
    #Воскресенье
    elif date_user[size:-6:-1] == ')еьне':
        j = 0
        for i in const.arr_7:
            if time_user == i:
                const.arr_7.pop(j)
            j = j + 1

    bot.send_message(const.id, "Запись клиента {0} {1}(id = {2})\nУслуга: {3}\nДата: {4}\nВремя: {5}".format(const.first_name, 
                                                                                            const.last_name,
                                                                                            str(message.from_user.id),
                                                                                            service,
                                                                                            date_user,
                                                                                            time_user))

#Посылает отмену записи клиента
def get_del(message, service, date_user, time_user):
    bot.send_message(const.id, "Клиент {0} {1}(id = {2}), отменил запись\nУслуга: {3}\nДата: {4}\nВремя: {5}".format(const.first_name, 
                                                                                                     const.last_name,
                                                                                                     str(message.from_user.id),
                                                                                                     service,
                                                                                                     date_user,
                                                                                                     time_user))

#Выбор времени
def times(message, keyb):
    # TODO
    #lenght = int(len(const.data_user[message.chat.id][6]) - 1):-6:-1

    #Понедельник
    if const.data_user[message.chat.id][6][int(len(const.data_user[message.chat.id][6]) - 1):-6:-1] == ')кинь':
        if len(const.arr_1) == 0:
            bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
            return

        for w in const.arr_1:
          keyb.row(w)

        const.data_user[message.chat.id][2] = False
        const.data_user[message.chat.id][3] = True

        print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
        bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
    #Вторник
    elif const.data_user[message.chat.id][6][int(len(const.data_user[message.chat.id][6]) - 1):-6:-1] == ')кинр':
        if len(const.arr_2) == 0:
            bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
            return

        for w in const.arr_2:
          keyb.row(w)

        const.data_user[message.chat.id][2] = False
        const.data_user[message.chat.id][3] = True

        print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
        bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
    #Среда
    elif const.data_user[message.chat.id][6][int(len(const.data_user[message.chat.id][6]) - 1):-6:-1] == ')адер':
        if len(const.arr_3) == 0:
            bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
            return

        for w in const.arr_3:
          keyb.row(w)

        const.data_user[message.chat.id][2] = False
        const.data_user[message.chat.id][3] = True

        print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
        bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
    #Четверг
    elif const.data_user[message.chat.id][6][int(len(const.data_user[message.chat.id][6]) - 1):-6:-1] == ')грев':
        if len(const.arr_4) == 0:
            bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
            return

        for w in const.arr_4:
          keyb.row(w)
        
        const.data_user[message.chat.id][2] = False
        const.data_user[message.chat.id][3] = True

        print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
        bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
    #Пятница
    elif const.data_user[message.chat.id][6][int(len(const.data_user[message.chat.id][6]) - 1):-6:-1] == ')ацин':
        if len(const.arr_5) == 0:
            bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
            return

        for w in const.arr_5:
          keyb.row(w)    

        const.data_user[message.chat.id][2] = False
        const.data_user[message.chat.id][3] = True

        print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
        bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
    #Суббота
    elif const.data_user[message.chat.id][6][int(len(const.data_user[message.chat.id][6]) - 1):-6:-1] == ')атоб':
        if len(const.arr_6) == 0:
            bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
            return

        for w in const.arr_6:
          keyb.row(w) 
        
        const.data_user[message.chat.id][2] = False
        const.data_user[message.chat.id][3] = True

        print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
        bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
    #Воскресенье
    elif const.data_user[message.chat.id][6][int(len(const.data_user[message.chat.id][6]) - 1):-6:-1] == ')еьне':
        if len(const.arr_7) == 0:
            bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
            return

        for w in const.arr_7:
          keyb.row(w)
        
        const.data_user[message.chat.id][2] = False
        const.data_user[message.chat.id][3] = True

        print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
        bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)

# Добавление времени
def add_time(message):

    #Последний элемент строки
    size = int(len(const.week_string) - 1)

    #Обьеденение в словарь
    text = str(message.text).split('/')

    print(const.week_string[size:-6:-1])   

    #Понедельник
    if const.week_string[size:-6:-1] == ')кинь':
        for w in text:
            const.arr_1.append(w)
        print(const.arr_1)

    #Вторник
    if const.week_string[size:-6:-1] == ')кинр':
        for w in text:
            const.arr_2.append(w)
        print(const.arr_2)

    #Среда
    if const.week_string[size:-6:-1] == ')адер':
        for w in text:
            const.arr_3.append(w)
        print(const.arr_3)

    #Четверг
    if const.week_string[size:-6:-1] == ')грев':
        for w in text:
            const.arr_4.append(w)
        print(const.arr_4)

    #Пятница
    if const.week_string[size:-6:-1] == ')ацин':
        for w in text:
            const.arr_5.append(w)
        print(const.arr_5)

    #Суббота
    if const.week_string[size:-6:-1] == ')атоб':
        for w in text:
            const.arr_6.append(w)
        print(const.arr_6)

    #Воскресенье
    if const.week_string[size:-6:-1] == ')еьне':
        for w in text:
            const.arr_7.append(w)
        print(const.arr_7)

#Завершение записи пользователя
def end(message, keyb):
    keyb.row('Все верно')
    keyb.row('Не та услуга')
    keyb.row('Не тот день', 'Не то время')

    keyb.row('Отмена')

    const.data_user[message.chat.id][8] = message.text
    print('Выбрана услуга: ' + const.data_user[message.chat.id][8])
    bot.send_message(message.chat.id, "Хорошо. Вот что вы выбрали:\nУслуга: {0}\nДень: {1}\nВремя: {2}".format(
                                                                                                const.data_user[message.chat.id][8], 
                                                                                                const.data_user[message.chat.id][6], 
                                                                                                const.data_user[message.chat.id][7]), 
                                                                                                reply_markup=keyb)

#Обработчик для создание расписания недель
@bot.message_handler(commands=['edit_weeks'])
def handle_edit_weeks(message):
    if message.chat.id == const.id:
        keyb = types.InlineKeyboardMarkup()

        #Вывод номера недели
        for w in const.week_arr:
            btn = types.InlineKeyboardButton(text=w, callback_data=w)
            keyb.add(btn)

        bot.send_message(const.id, """Выберите неделю для внесения новой записи:""", reply_markup=keyb)
    else:
        bot.send_message(message.chat.id, "")

#Обработчик для очистки недель
@bot.message_handler(commands=['clean_weeks'])
def handle_clean_weeks(message):
    if message.chat.id == const.id:
        keyb = types.InlineKeyboardMarkup()

        btn = types.InlineKeyboardButton(text='OK', callback_data='OK_CLEAN')
        keyb.add(btn)

        bot.send_message(const.id, "Для подтверждения отчиски нажмине OK", reply_markup=keyb)
    else:
        bot.send_message(message.chat.id, "")


#Обработчик - start
@bot.message_handler(commands=['start'])
def start_handle(message):
                                                        #w_u[1] #wk_u[2] #t_u[3]
    const.data_user[message.chat.id] = [message.chat.id, False,  False,   False,
                                            #s_s[4]   #d_s[5] 
                                            False,    False,
                                            #w_st[6]  #t_st[7]  #s_st[8]
                                            '',       '',       '']

    if const.id == message.chat.id:
        keyb = types.ReplyKeyboardMarkup(True, False)

        keyb.row('/edit_weeks', '/clean_weeks')
        bot.send_message(const.id, "edit", reply_markup=keyb)

    #write_user
    elif const.data_user == {}:
        keyb = types.ReplyKeyboardMarkup(True, False)
        keyb.row('Записаться')
        keyb.row('Контакты')
        bot.send_message(message.from_user.id, 
                         "Привет!\nЯ бот который поможет тебе записаться на стрижку и.т.д", reply_markup=keyb)

    # Пользователь уже записан
    elif const.data_user[message.chat.id][1] == True:
        keyb_f = types.ReplyKeyboardMarkup(True, False)

        keyb_f.row('Отменить запись', 'Информация о записи')
        keyb_f.row('Контакты')

        bot.send_message(message.chat.id, "Вы уже записаны!\nУслуга: {0}\nДень: {1}\nВремя: {2}".format(
                                                                                                const.data_user[message.chat.id][8],
                                                                                                const.data_user[message.chat.id][6], 
                                                                                                const.data_user[message.chat.id][7]), 
                                                                                                reply_markup=keyb_f)
    # data_user != {} 
    elif const.data_user[message.chat.id][1] == False:
        keyb = types.ReplyKeyboardMarkup(True, False)
        keyb.row('Записаться')
        keyb.row('Контакты')
        bot.send_message(message.from_user.id, 
                         "Привет!\nЯ бот который поможет тебе записаться на стрижку и.т.д", reply_markup=keyb)
    

#Обработчик введённого текста
@bot.message_handler(content_types=['text'])
def handle_text(message):

    const.first_name = message.chat.first_name
    const.last_name = message.chat.last_name

    if message.text == 'Контакты':
            keyb = types.InlineKeyboardMarkup()

            #Кнопки с ссылками на соц. сети
            btn_vk = types.InlineKeyboardButton(text="Vk", url="https://vk.com/id95702362")
            btn_inst = types.InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/andrey_starzhevskiy/")

            keyb.add(btn_vk)
            keyb.add(btn_inst)

            bot.send_message(message.chat.id, """Vk: https://vk.com/id95702362\nInstagram: https://www.instagram.com/andrey_starzhevskiy/""",
                            reply_markup=keyb)
    elif message.text == 'Информация о записи' and const.data_user[message.chat.id][1]:
        keyb_f = types.ReplyKeyboardMarkup(True, False)

        keyb_f.row('Отменить запись', 'Информация о записи')
        keyb_f.row('Контакты')

        bot.send_message(message.chat.id, "Услуга: {0}\nДень: {1}\nВремя: {2}".format(const.data_user[message.chat.id][8], 
                                                                                      const.data_user[message.chat.id][6], 
                                                                                      const.data_user[message.chat.id][7]), 
                                                                                      reply_markup=keyb_f)

    elif message.text == 'Да, уверен' and const.data_user[message.chat.id][1]:
        keyb_a = types.ReplyKeyboardMarkup(True, False)

        const.data_user[message.chat.id][1] = False

        keyb_a.row('Записаться')
        keyb_a.row('Контакты')

        get_del(message, const.data_user[message.chat.id][8], 
                                         const.data_user[message.chat.id][6], 
                                         const.data_user[message.chat.id][7])

        bot.send_message(message.chat.id, "Запись была отменена!", reply_markup=keyb_a)

    elif message.text == 'Нет' and const.data_user[message.chat.id][1]:
        keyb_f = types.ReplyKeyboardMarkup(True, False)

        keyb_f.row('Отменить запись', 'Информация о записи')
        keyb_f.row('Контакты')

        bot.send_message(message.chat.id, "Окей", reply_markup=keyb_f)

    elif message.text == 'Отменить запись' and const.data_user[message.chat.id][1]:
        key_b = types.ReplyKeyboardMarkup(True, False)

        key_b.row('Да, уверен')
        key_b.row('Нет')

        bot.send_message(message.chat.id, "Вы уверенны что хотите отменить запись", reply_markup=key_b)
        if const.data_user[message.chat.id][1] == False:
            keyb_a = types.ReplyKeyboardMarkup(True, False)

            keyb_a.row('Записаться')
            keyb_a.row('Контакты')


            bot.send_message(message.chat.id, "Вы не можите отменить запись т.к не записаны", reply_markup=keyb_a)

    elif const.data_user[message.chat.id][1] == False:
        keyb = types.ReplyKeyboardMarkup(True, False)

        if message.text == 'Записаться':
                                                                 #w_u[1] #wk_u[2] #t_u[3]
            const.data_user[message.chat.id] = [message.chat.id, False,  False,   False,
                                                #s_s[4]   #d_s[5] 
                                                False,    False,
                                                #w_st[6]  #t_st[7]  #s_st[8]
                                                '',       '',       '']

            keyb.row('Стрижка', 'Борода')
            keyb.row('Стрижка + Борода')
            keyb.row('Отмена')

            bot.send_message(message.chat.id, "Пожалуйста, выберите услугу", reply_markup=keyb)

        elif message.text == 'Стрижка' or message.text == 'Борода' or message.text == 'Стрижка + Борода':
            const.data_user[message.chat.id][2] = True
            if const.data_user[message.chat.id][4] != True:
                keyb.row(const.week_arr[0], const.week_arr[1])
                keyb.row(const.week_arr[2], const.week_arr[3])
                keyb.row(const.week_arr[4], const.week_arr[5])
                keyb.row(const.week_arr[6])

                keyb.row('Назад', 'Отмена')

                const.data_user[message.chat.id][8] = message.text

                bot.send_message(message.chat.id, "Выберите день", reply_markup=keyb)
            else:
                const.data_user[message.chat.id][4] = False
                end(message, keyb)

        elif message.text == 'Отмена':
            keyb.row('Записаться')
            keyb.row('Контакты')

            bot.send_message(message.chat.id, "Окей", reply_markup=keyb)

        elif message.text == 'Назад':
            if const.data_user[message.chat.id][2]:
                keyb.row('Стрижка', 'Борода')
                keyb.row('Стрижка + Борода')
                keyb.row('Отмена')

                bot.send_message(message.chat.id, "Пожалуйста, выберите услугу", reply_markup=keyb)
            elif const.data_user[message.chat.id][3]:
                const.data_user[message.chat.id][2] = True
                if const.data_user[message.chat.id][5] == False:
                    keyb.row(const.week_arr[0], const.week_arr[1])
                    keyb.row(const.week_arr[2], const.week_arr[3])
                    keyb.row(const.week_arr[4], const.week_arr[5])
                    keyb.row(const.week_arr[6])

                    keyb.row('Назад', 'Отмена')

                else:
                    const.data_user[message.chat.id][5] = False
                    end(message, keyb)
                bot.send_message(message.chat.id, "Выберите день", reply_markup=keyb)

        #Понедельник
        elif message.text[int(len(message.text) - 1):-6:-1] == ')кинь':
            if len(const.arr_1) == 0:
                bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
                return

            for w in const.arr_1:
                keyb.row(w)

            const.data_user[message.chat.id][2] = False
            const.data_user[message.chat.id][3] = True
            if const.data_user[message.chat.id][5] == False:
                keyb.row('Назад', 'Отмена')

            const.data_user[message.chat.id][6] = message.text
            print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
            bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
        #Вторник
        elif message.text[int(len(message.text) - 1):-6:-1] == ')кинр':
            if len(const.arr_2) == 0:
                bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
                return

            for w in const.arr_2:
                keyb.row(w)

            const.data_user[message.chat.id][2] = False
            const.data_user[message.chat.id][3] = True
            if const.data_user[message.chat.id][5] == False:
                keyb.row('Назад', 'Отмена')

            const.data_user[message.chat.id][6] = message.text
            print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
            bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
        #Среда
        elif message.text[int(len(message.text) - 1):-6:-1] == ')адер': 
            if len(const.arr_3) == 0:
                bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
                return

            for w in const.arr_3:
                keyb.row(w)

            const.data_user[message.chat.id][2] = False
            const.data_user[message.chat.id][3] = True
            if const.data_user[message.chat.id][5] == False:
                keyb.row('Назад', 'Отмена')

            const.data_user[message.chat.id][6] = message.text
            print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
            bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
        #Четверг
        elif message.text[int(len(message.text) - 1):-6:-1] == ')грев':
            if len(const.arr_4) == 0:
                bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
                return

            for w in const.arr_4:
                keyb.row(w)
        
            const.data_user[message.chat.id][2] = False
            const.data_user[message.chat.id][3] = True
            if const.data_user[message.chat.id][5] == False:
                keyb.row('Назад', 'Отмена')

            const.data_user[message.chat.id][6] = message.text
            print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
            bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
        #Пятница
        elif message.text[int(len(message.text) - 1):-6:-1] == ')ацин':
            if len(const.arr_5) == 0:
                bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
                return

            for w in const.arr_5:
                keyb.row(w)    

            const.data_user[message.chat.id][2] = False
            const.data_user[message.chat.id][3] = True
            if const.data_user[message.chat.id][5] == False:
                keyb.row('Назад', 'Отмена')

            const.data_user[message.chat.id][6] = message.text
            print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
            bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
        #Суббота
        elif message.text[int(len(message.text) - 1):-6:-1] == ')атоб':
            if len(const.arr_6) == 0:
                bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
                return

            for w in const.arr_6:
                keyb.row(w) 
        
            const.data_user[message.chat.id][2] = False
            const.data_user[message.chat.id][3] = True
            if const.data_user[message.chat.id][5] == False:
                keyb.row('Назад', 'Отмена')

            const.data_user[message.chat.id][6] = message.text
            print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
            bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)
        #Воскресенье
        elif message.text[int(len(message.text) - 1):-6:-1] == ')еьне':
            if len(const.arr_7) == 0:
                bot.send_message(message.chat.id, "Расписание на {} ещё не составлено".format(message.text))
                return

            for w in const.arr_7:
                keyb.row(w)
        
            const.data_user[message.chat.id][2] = False
            const.data_user[message.chat.id][3] = True
            if const.data_user[message.chat.id][5] == False:
                keyb.row('Назад', 'Отмена')

            const.data_user[message.chat.id][6] = message.text
            print('Выбрана неделя: ' + const.data_user[message.chat.id][6])
            bot.send_message(message.chat.id, "Выберите время", reply_markup=keyb)

        elif message.text == 'Все верно':
            const.data_user[message.chat.id][1] = True

            keyb_f = types.ReplyKeyboardMarkup(True, False)

            keyb_f.row('Отменить запись', 'Информация о записи')
            keyb_f.row('Контакты')

            get(message, const.data_user[message.chat.id][8], 
                const.data_user[message.chat.id][6], 
                const.data_user[message.chat.id][7])

            bot.send_message(message.chat.id, "Вы успешно записались!\nУслуга: {0}\nДень: {1}\nВремя: {2}".format(
                                                                                                const.data_user[message.chat.id][8],
                                                                                                const.data_user[message.chat.id][6], 
                                                                                                const.data_user[message.chat.id][7]), 
                                                                                                reply_markup=keyb_f)            

        elif message.text == 'Не та услуга':
            const.data_user[message.chat.id][4] = True
            keyb.row('Стрижка', 'Борода')
            keyb.row('Стрижка + Борода')
            keyb.row('Отмена')

            bot.send_message(message.chat.id, "Пожалуйста, выберите услугу", reply_markup=keyb)
        elif message.text == 'Не тот день':
            const.data_user[message.chat.id][5] = True
            const.data_user[message.chat.id][2] = True

            keyb.row(const.week_arr[0], const.week_arr[1])
            keyb.row(const.week_arr[2], const.week_arr[3])
            keyb.row(const.week_arr[4], const.week_arr[5])
            keyb.row(const.week_arr[6])

            bot.send_message(message.chat.id, "Выберите день", reply_markup=keyb)

        elif message.text == 'Не то время':
            times(message, keyb)

        elif message.text == 'Информация о записи':
            keyb.row('Записаться')
            keyb.row('Контакты')
            bot.send_message(message.from_user.id, "Привет!\nЯ бот который поможет тебе записаться на стрижку и.т.д", reply_markup=keyb)

        elif message.text == 'Отменить запись':
            keyb.row('Записаться')
            keyb.row('Контакты')
            bot.send_message(message.from_user.id, "Привет!\nЯ бот который поможет тебе записаться на стрижку и.т.д", reply_markup=keyb)

        elif message.text == re.findall(r'\d{1,2}:\d.', message.text)[0]:
            keyb.row('Все верно')
            keyb.row('Не та услуга')
            keyb.row('Не тот день', 'Не то время')

            keyb.row('Отмена')

            const.data_user[message.chat.id][5] = False
            const.data_user[message.chat.id][7] = message.text
            print('Выбрано время: ' + const.data_user[message.chat.id][7])
            bot.send_message(message.chat.id, "Хорошо. Вот что вы выбрали:\nУслуга: {0}\nДень: {1}\nВремя: {2}".format(const.data_user[message.chat.id][8], 
                                                                                                                       const.data_user[message.chat.id][6], 
                                                                                                                       const.data_user[message.chat.id][7]), 
                                                                                                                       reply_markup=keyb)

    else:
        bot.send_message(message.chat.id, "Вы уже сделали запись\nУслуга: {0}\nДень: {1}\nВремя: {2}".format(const.data_user[message.chat.id][8], 
                                                                                                             const.data_user[message.chat.id][6], 
                                                                                                             const.data_user[message.chat.id][7]))
        
#Обработчик - callback
@bot.callback_query_handler(func=lambda c: c)
def handle_callback(c):
    # Проверка на возможность редоктировать недели
    if const.id == c.message.chat.id and c.data != 'OK_CLEAN':
        for i in const.week_arr:
            if c.data == i:
                #Сохроняем значение выбранной недели
                const.week_string = str(c.data)

                send = bot.send_message(const.id, "Неделя: {}\nВведите время для записи в формате: 11:00/12:00/13:00/(time)/.../".format(i))
                bot.register_next_step_handler(send, add_time)
    
    # Пользовать отменил запись
    elif c.data == 'OK':
        keyb = types.ReplyKeyboardMarkup(True, False)

        keyb.row('Записаться')
        keyb.row('Контакты')

        const.week_user = False
        bot.send_message(c.message.chat.id, "Запись успешно отменена", reply_markup=keyb)

    # Очистить все недели
    elif c.data == 'OK_CLEAN':
        const.arr_1 = []
        const.arr_2 = []
        const.arr_3 = []
        const.arr_4 = []
        const.arr_5 = []
        const.arr_6 = []
        const.arr_7 = []

        bot.send_message(const.id, "Все недели очищены")
