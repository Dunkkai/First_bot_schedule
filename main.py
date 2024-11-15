from datetime import datetime, date, time

import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, types, filters, executor
from tkn import TOKEN
import asyncio
import logging
import aiogram.utils

token = TOKEN

bot = Bot(token=token)
dp = Dispatcher(bot)

prekb = types.ReplyKeyboardMarkup(resize_keyboard=True)
prebutt = [types.KeyboardButton(text='расписание 105-й группы'), types.KeyboardButton(text='Звонки')]
prekb.add(*prebutt)

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [types.KeyboardButton(text='А'), types.KeyboardButton(text='Б'), types.KeyboardButton(text="Вернуться назад")]
kb.add(*buttons)

"""kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [types.KeyboardButton(text='Первая'),types.KeyboardButton(text='Вторая')]
kb.add(*buttons)"""

choose_week = types.InlineKeyboardMarkup()
buttons_gr = [types.InlineKeyboardButton(text='Первая', callback_data='perv(a)'),
              types.InlineKeyboardButton(text='Вторая', callback_data='vtor(a)')]
choose_week.add(*buttons_gr)

choose_week_1 = types.InlineKeyboardMarkup()
buttons_gr_1 = [types.InlineKeyboardButton(text='Первая', callback_data='perv(b)'),
                types.InlineKeyboardButton(text='Вторая', callback_data='b-2')]
choose_week_1.add(*buttons_gr_1)


@dp.message_handler(filters.Text(contains='расписание 105-й группы'))
async def globff(message: types.Message):
    await message.answer(text='Выбери подгруппу', reply_markup=kb)


@dp.message_handler(filters.Text(contains='А'))
async def globl(message: types.Message):
    await message.answer(text='Выбери учебную неделю', reply_markup=choose_week)


@dp.message_handler(filters.Text(contains='Б'))
async def globl(message: types.Message):
    await message.answer(text='Выбери учебную неделю', reply_markup=choose_week_1)


@dp.callback_query_handler(filters.Text(contains='perv(a)'))
async def callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="""
            расписание подгруппы а(1 неделя)
понедельник:
1. 
2. Введение в И.И. 406 (Гущина О.А) (105)	
3. Основы проги 413 (Фирсова С.А.) (105 а)
4. Основы проги 218 (фирсова С.А.) (104 105)


Вторник
1. Дискретная математика к.16 406 (Сыромясов А.О.) (105)
2. Дискретная математика к.16 305 (Сыромясов А.О.) (105)
3. Основы программирования [к.1 203] (ФИРСОВА С.А.)
4. 

Среда
1. Алгоритмы и структуры данных 220 (Кулягин А.И.) (105 а)
2.
3.

Четверг
1. 
2.Ознакомительная практика 312 (Кутыркина М.А.) (105 а)
3.Алгоритмы и структуры данных [к.1 218] (КАЛЕДИН О.Е.) (104 и 105)
4. 
5.Безопасность жизнедеятельности [к.28 234] (ГЛОТОВ С.В.)

Пятница
1. 
2. Иностранный язык (Англ.) [к.1 415] (САМОЙЛОВА Е.В.) (105 а)
3. Дискретная математика [к.1 309] (СЫРОМЯСОВ А.О.) (105)
4. Введение в искусственный интеллект [к.1 506] (КУТЫРКИНА М.А.) (105 а)	
5.

Суббота
1.
2.
3. Математический анализ [к.1 212] (МЕЩЕРЯКОВА С.И.) (104 и 105)
4. Математический анализ [к.1 309] (МЕЩЕРЯКОВА С.И.) (105)
""", )
    await callback_query.answer()


@dp.callback_query_handler(filters.Text(contains='vtor(a)'))
async def callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="""
            расписание подгруппы а(2 неделя)
понедельник:
1.
2.
3.Основы программирования [к.1 413] (ФИРСОВА С.А.) (105 а)
4. Основы программирования [к.1 218] (ФИРСОВА С.А.)
5. Безопасность жизнедеятельности [к.1 218] (ИГАЙКИНА И.И.)

Вторник
1. Дискретная математика [к.16 406] (СЫРОМЯСОВ А.О.) (105)
2. Дискретная математика [к.16 305] (СЫРОМЯСОВ А.О.) (105)	
3. 
4. Элективные дисцип(модули) по физ-ре  и спорту (Наумкина ТС) (105?)

Среда
1.Алгоритмы и структуры данных [к.1 220] (КУЛЯГИН А.И.) (105 а)
2.
3.

Четверг
1. Ознакомительная практика [к.1 312] (КУТЫРКИНА М.А.) (105 а)
2. Ознакомительная практика [к.1 312] (КУТЫРКИНА М.А.)
3. Алгоритмы и структуры данных [к.1 218] (КАЛЕДИН О.Е.)
4.		
5. Безопасность жизнедеятельности [к.28 234] (ГЛОТОВ С.В.)
6.

Пятница
1. Иностранный язык (Англ.) [к.1 415] (САМОЙЛОВА Е.В.)
2. Иностранный язык (Англ.) [к.1 415] (САМОЙЛОВА Е.В.)
3. Дискретная математика [к.1 309] (СЫРОМЯСОВ А.О.)
4. Введение в искусственный интеллект [к.1 312] (КУТЫРКИНА М.А.)		
5. 

Суббота
1.
2.
3. Математический анализ [к.1 212] (МЕЩЕРЯКОВА С.И.) (104 и 105)
4. Математический анализ [к.1 309] (МЕЩЕРЯКОВА С.И.) (105)
""", )
    await callback_query.answer()


@dp.callback_query_handler(filters.Text(contains='perv(b)'))
async def callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="""
расписание подгруппы б(1 неделя)
понедельник:
1. 
2. Введение в искусственный интеллект [к.1 406] (ГУЩИНА О.А.)
3. 
4. Основы программирования [к.1 218] (ФИРСОВА С.А.)

Вторник
1. Дискретная математика [к.1 406] (СЫРОМЯСОВ А.О.)		
2. Дискретная математика [к.1 305] (СЫРОМЯСОВ А.О.)
3.   
4. 

Среда
1.
2.
3. Введение в искусственный интеллект [к.1 506] (КУТЫРКИНА М.А.)
4. Алгоритмы и структуры данных [к.1 413] (КУЛЯГИН А.И.)

Четверг
1.
2. Иностранный язык (Англ.) [к.1 415] (САМОЙЛОВА Е.В.)
3. Алгоритмы и структуры данных [к.1 218] (КАЛЕДИН О.Е.)
4. Ознакомительная практика [к.1 205] (КУТЫРКИНА М.А.)
5. Безопасность жизнедеятельности [к.28 234] (ГЛОТОВ С.В.)

Пятница
1. 
2. 
3. Дискретная математика [к.1 309] (СЫРОМЯСОВ А.О.)
4. Основы программирования [к.1 506] (ФИРСОВА С.А.)	
5. 

Суббота
1.
2.
3. Математический анализ [к.1 212] (МЕЩЕРЯКОВА С.И.) (104 и 105)
4. Математический анализ [к.1 309] (МЕЩЕРЯКОВА С.И.) (105)
""", )
    await callback_query.answer()


@dp.callback_query_handler(filters.Text(contains='b-2'))
async def callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="""
            расписание подгруппы б(2 неделя)
понедельник:
1. 
2. 
3. 
4. Основы программирования [к.1 218] (ФИРСОВА С.А.)
5. Безопасность жизнедеятельности [к.1 218] (ИГАЙКИНА И.И.)

Вторник
1. Дискретная математика [к.1 406] (СЫРОМЯСОВ А.О.)
2. Дискретная математика [к.1 305] (СЫРОМЯСОВ А.О.)
3. 
4. Элективные дисцип(модули) по физ-ре  и спорту (Наумкина ТС) (105?)

Среда
1. 
2. Основы программирования [к.1 312] (ФИРСОВА С.А.)
3. Введение в искусственный интеллект [к.1 506] (КУТЫРКИНА М.А.)
4. Алгоритмы и структуры данных [к.1 413] (КУЛЯГИН А.И.)

Четверг
1. Иностранный язык (Англ.) [к.1 415] (САМОЙЛОВА Е.В.)
2. Иностранный язык (Англ.) [к.1 415] (САМОЙЛОВА Е.В.)
3. Алгоритмы и структуры данных [к.1 218] (КАЛЕДИН О.Е.)
4. Ознакомительная практика [к.1 205] (КУТЫРКИНА М.А.)
5. Безопасность жизнедеятельности [к.28 234] (ГЛОТОВ С.В.)
6. Ознакомительная практика [к.1 205] (КУТЫРКИНА М.А.)

Пятница
1. 
2. 
3. Дискретная математика [к.1 309] (СЫРОМЯСОВ А.О.)
4. Основы программирования [к.1 506] (ФИРСОВА С.А.)	
5. 

Суббота
1.
2.
3. Математический анализ [к.1 212] (МЕЩЕРЯКОВА С.И.) (104 и 105)
4. Математический анализ [к.1 309] (МЕЩЕРЯКОВА С.И.) (105)
""", )
    await callback_query.answer()


@dp.message_handler(filters.Text(contains='Звонки'))
async def globfl(message: types.Message):
    await message.answer(text='''
1 пара  8:30-10:00
2 пара 10:10 11:40
3 пара 12:00 13:30
4 пара 13:45 15:15
5 пара 15:25 16:55
6 пара 17:05 18:35
7 пара 18:40 20:10''')


@dp.message_handler(filters.Text(contains='Вернуться назад'))
async def globfl(message: types.Message):
    await message.answer(text='Что вас интересует?', reply_markup=prekb)


@dp.message_handler(commands=['start'])
async def cmd_handler(message: types.Message):
    Imya = message.from_user.first_name
    now = datetime.now().time()
    if now >= datetime.strptime("04:00", "%H:%M").time() and now < datetime.strptime("10:00", "%H:%M").time():
        greeting = "Доброе утро"
    elif now >= datetime.strptime("10:00", "%H:%M").time() and now < datetime.strptime("18:00", "%H:%M").time():
        greeting = "Добрый день"
    else:
        greeting = "Добрый вечер"
    await   message.answer(f'{greeting}, {Imya}, выбери что тебя интересует!', reply_markup=prekb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)