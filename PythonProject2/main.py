import asyncio
import logging
import random
import sys
from gc import callbacks
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import Message, CallbackQuery, URLInputFile, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from commands import START_COMMAND, START_BOT_COMMAND, ASTR_BOT_COMMAND, ASTR_COMMAND, MATH_BOT_COMMAND, MATH_COMMAND, PYTHON_BOT_COMMAND, PYTHON_COMMAND, SEARCH_COMMAND, SEARCH_BOT_COMMAND, FILTER_BOT_COMMAND, FILTER_COMMAND, RANDOM_MATH_COMMAND, RANDOM_MATH_BOT_COMMAND, RANDOM_PYTHON_COMMAND, RANDOM_PYTHON_BOT_COMMAND, RANDOM_ASTRONOMY_BOT_COMMAND, RANDOM_ASTRONOMY_COMMAND
from data import get_choise_astr, get_choise_math, get_choise_python
from keyboard import choise_keyboard_markup_astr, ChoiseCallBack, ChoiseCallBack2, choise_keyboard_markup_math, choise_keyboard_markup_python, ChoiseCallBack3
from models import Choise, ChoiseStates
from tocken import BOT_TOCKEN
from models_2 import Choise_2

TOKEN = getenv(BOT_TOCKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привіт, {html.bold(message.from_user.full_name)}"
                         f"\nВ меню крім цієї є ще 3 кнопки: Астрономія, Математика і Пайтон. В кожному іх них є багато чого цікавого, надіюсь вам сподобається."
                         f"\nПриємного читання!")


@dp.message(Command('astronomy')) #/films
async def command_astronomy(message: Message) -> None: # Message - це потипу тип данних
    astronomy = get_choise_astr()
    markup = choise_keyboard_markup_astr(astronomy)
    await message.answer("Астрономія",reply_markup=markup)


@dp.callback_query(ChoiseCallBack.filter())
async def callb_choise_astr(callback:CallbackQuery, callback_data:ChoiseCallBack) -> None:
    choise_id = callback_data.id
    choise_info = get_choise_astr(choise_id=choise_id)
    choise = Choise(**choise_info)
    text = f"Тема: {choise.name}\n" \
           f"Вид: {choise.type}\n" \
           f"Опис: {choise.description}\n"

    await callback.message.answer_photo(caption=text, photo=choise.poster)


@dp.message(Command('math')) #/films
async def command_math(message: Message) -> None:
    math = get_choise_math()
    markup = choise_keyboard_markup_math(math)
    await message.answer("Математика",reply_markup=markup)

@dp.callback_query(ChoiseCallBack2.filter())
async def callb_choise_math(callback:CallbackQuery, callback_data:ChoiseCallBack2) -> None:
    choise_id = callback_data.id
    choise_info = get_choise_math(choise_id=choise_id)
    choise = Choise_2(**choise_info)
    text = f"Тема: {choise.name}\n" \
           f"Опис: {choise.description}\n" \
           f"Посилання на відео: {choise.link}\n"

    await callback.message.answer_photo(caption=text, photo=choise.poster)


@dp.message(Command('python')) #/films
async def command_python(message: Message) -> None:
    python = get_choise_python()
    markup = choise_keyboard_markup_python(python)
    await message.answer("Пайтон",reply_markup=markup)

@dp.callback_query(ChoiseCallBack3.filter())
async def callb_choise_python(callback:CallbackQuery, callback_data:ChoiseCallBack3) -> None:
    choise_id = callback_data.id
    choise_info = get_choise_python(choise_id=choise_id)
    choise = Choise_2(**choise_info)
    text = f"Тема: {choise.name}\n" \
           f"Опис: {choise.description}\n" \
           f"Посилання на відео: {choise.link}\n"

    await callback.message.answer_photo(caption=text, photo=choise.poster)


@dp.message(Command("search_thema"))
async def search_thema(message:Message, state:FSMContext):
    await message.answer("Введіть Астрономія\Математика\Пайтон для пошуку:")
    await state.set_state(ChoiseStates.search_thema)


@dp.message(ChoiseStates.search_thema)
async def get_search_query(message:Message, state: FSMContext):
    query = message.text.lower()
    if query == 'астрономія':
        await message.answer("Введіть планету, зірку, галактику, сузір'я, комету, карликову планету або астероїд, про який ви хочете почитати: ")
        await state.set_state(ChoiseStates.search_thema_2)
    elif query == 'математика':
        await message.answer("Введіть тему або теорему, яка вас цікавить: ")
        await state.set_state(ChoiseStates.search_thema_2)
    elif query == 'пайтон':
        await message.answer("Введіть тему з Пайтону, яка вас цікавить: ")
        await state.set_state(ChoiseStates.search_thema_2)
    else:
        await message.reply("Такої категорії не знайдено.")

@dp.message(ChoiseStates.search_thema_2)
async def get_message(message:Message, state: FSMContext):
    astronomy = get_choise_astr()
    math = get_choise_math()
    python = get_choise_python()
    query = message.text.lower()
    results_astr = [thema for thema in astronomy if query in thema['name'].lower()]
    results_math = [thema for thema in math if query in thema['name'].lower()]
    results_python = [thema for thema in python if query in thema['name'].lower()]
    if results_astr:
        for category in results_astr:
            text = f"Тема: {category['name']}\n" \
                   f"Вид: {category['type']}\n" \
                   f"Опис: {category['description']}\n"
            await message.answer(f"Знайдено:")
            await message.answer_photo(caption=text, photo=URLInputFile(category['poster']))
    elif results_math:
        for category in results_math:
            text = f"Тема: {category['name']}\n" \
                   f"Опис: {category['description']}\n"
            await message.answer(f"Знайдено:")
            await message.answer_photo(caption=text, photo=URLInputFile(category['poster']))
    elif results_python:
        for category in results_python:
            text = f"Тема: {category['name']}\n" \
                   f"Опис: {category['description']}\n"
            await message.answer(f"Знайдено:")
            await message.answer_photo(caption=text, photo=URLInputFile(category['poster']))
    else:
        await message.answer("Такої теми не знайдено!")
        await state.clear()


@dp.message(Command("random_astronomy"))
async def random_astronomy(message:Message, state:FSMContext):
    astronomy = get_choise_astr()
    random_2 = random.randint(0,40)
    if astronomy:
        text = f"Тема: {astronomy[random_2]['name']}\n" \
                f"Вид: {astronomy[random_2]['type']}\n" \
                f"Опис: {astronomy[random_2]['description']}\n"
        await message.answer(f"Знайдено:")
        await message.answer_photo(caption=text, photo=URLInputFile(astronomy[random_2]['poster']))


@dp.message(Command("random_math"))
async def random_math(message:Message, state:FSMContext):
    math = get_choise_math()
    random_2 = random.randint(0,6)
    if math:
        text = f"Тема: {math[random_2]['name']}\n" \
                f"Опис: {math[random_2]['description']}\n"
        await message.answer(f"Знайдено:")
        await message.answer_photo(caption=text, photo=URLInputFile(math[random_2]['poster']))


@dp.message(Command("random_python"))
async def random_python(message:Message, state:FSMContext):
    python = get_choise_python()
    random_2 = random.randint(0,24)
    if python:
        text = f"Тема: {python[random_2]['name']}\n" \
                f"Опис: {python[random_2]['description']}\n"
        await message.answer(f"Знайдено:")
        await message.answer_photo(caption=text, photo=URLInputFile(python[random_2]['poster']))


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    bot = Bot(token=BOT_TOCKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands([START_BOT_COMMAND, ASTR_BOT_COMMAND, MATH_BOT_COMMAND, PYTHON_BOT_COMMAND, SEARCH_BOT_COMMAND, FILTER_BOT_COMMAND, RANDOM_PYTHON_BOT_COMMAND, RANDOM_ASTRONOMY_BOT_COMMAND, RANDOM_MATH_BOT_COMMAND])
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())