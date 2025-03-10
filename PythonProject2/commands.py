from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand


START_COMMAND = Command('start')
START_BOT_COMMAND = BotCommand(command='start', description='Початок роботи')
ASTR_COMMAND = Command('astronomy')
ASTR_BOT_COMMAND = BotCommand(command='astronomy', description='Астрономія')
MATH_COMMAND = Command('math')
MATH_BOT_COMMAND = BotCommand(command='math', description='Математика')
PYTHON_COMMAND = Command('python')
PYTHON_BOT_COMMAND = BotCommand(command='python', description='Пайтон')
SEARCH_COMMAND = Command('search_thema')
SEARCH_BOT_COMMAND = BotCommand(command='search_thema', description='Пошук теми за категорією')
FILTER_COMMAND = Command('filter_astronomy')
FILTER_BOT_COMMAND = BotCommand(command='filter_astronomy', description='Пошук теми з астрономії на видом космічного тіла')
RANDOM_ASTRONOMY_COMMAND = Command('random_astronomy')
RANDOM_ASTRONOMY_BOT_COMMAND = BotCommand(command='random_astronomy', description='Випадкова тема з астрономії')
RANDOM_MATH_COMMAND = Command('random_math')
RANDOM_MATH_BOT_COMMAND = BotCommand(command='random_math', description='Випадкова тема з математики')
RANDOM_PYTHON_COMMAND = Command('random_python')
RANDOM_PYTHON_BOT_COMMAND = BotCommand(command='random_python', description='Випадкова тема з пайтон')