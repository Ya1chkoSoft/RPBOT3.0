from email import message
import random
import pickle

from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart,Command

from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton

import app.database.requests as rq
import app.keyboard as kb

player: list = []
router = Router()

test: str = "ТЕСТ ПРОЙДЕН"
@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_users(message.from_user.id)
    await rq.redact_db(message.from_user.username)
    await message.answer("""<b>ПРИВЕТСТВУЮ В НАШЕМ РП БОТЕ</b>
                    <i>версия бота 3.0</i>
данный бот будет помогать вам в рп и тд:3
ниже будет распологаться меню, желаем вам удачи""",parse_mode='HTML', reply_markup=kb.main)
    
async def randomizers(rand):
    await message.reply(f'{rand}')

@router.message(F.text)
async def randomizer1(message: Message):
    global rand
    text = message.text.lower()
    rand = random.randint(1, 10)
    match text:
        case 'ранд': await message.reply(f'{rand}')
        case 'рандом': await message.reply(f'{rand}')
        case 'rand': await message.reply(f'{rand}')
        case 'random': await message.reply(f'{rand}')
        case 'тест': await message.reply(test)
        case 'Урон': await message.reply(random.randint(1,100))
        case 'кубик': await message.reply_dice()
        case 'ахуеть': await message.reply('<b>Звуки бравл старса</b>',parse_mode='HTML')

        case 'женщина':
            a = random.randint(1, 9)
            match a:
                case 1: await message.reply('Я ЖЕНЩИНА')
                case 2: await message.reply('АААААА ЖЕНЩИНЫ БЛЯТЬ')
                case 3: await message.reply('НЕЕЕЕЕЕТ УБЕРИ ЭТО')
                case 4: await message.reply('ЭТО ПРОСТО НЕВОЗМОЖНО!!!')
                case 5: await message.reply('СПАСАЙСЯ КТО МОЖЕТ')
                case 6: await message.reply('Ох Ахъ женщины топчег  \n  *Застрелил черта*  туда егооооо')
                case 7: await message.reply('ЖЕНЩИНА В ЧАТЕ!!! \nСРОЧНО ТРАХАТЬ')
                case 8: await message.reply('Надо забанить')
                case 9: await message.reply('Ну бывает')       
        case 'мужчина':
            a = random.randint(1, 9)
            match a:
                case 1: await message.reply('Я МУЖИК')
                case 2: await message.reply('АААААА МУЖИКИ, СВЕЖЕЕ МЯСО!!!')
                case 3: await message.reply('а вы знали что в корее все мужики поголовно КПОП и не натуралы')
                case 4: await message.reply('ЭТО ПРОСТО НЕВОЗМОЖНО!!!')
                case 5: await message.reply('Пошли в хоечку и отжарь меня по самое нихачу')
                case 6: await message.reply('Он любит смачно в попачку?')
                case 7: await message.reply('МУЖИК В ЧАТЕ!!! \nСРОЧНО ТРАХАТЬ И ПОШЛИ В ХОЙКУ')
                case 8: await message.reply('Надо повысить')
                case 9: await message.reply('БЫСТРО ЗОВИ ЕГО В ТЕРКУ! \n мы будем на пенсиле прыгать')

@router.callback_query(F.data == 'menubutton')
async def menu(callback: CallbackQuery):
    await callback.answer('успешно')
    await callback.message.edit_text('Вы перешли в меню, ниже кнопки с пояснениями',reply_markup=kb.menubuttons)

@router.callback_query(F.data == 'whatsrpbt')
async def defwhatsrpbutton(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('''<b>РП происходит от RolePlay</b>, <i>на рп вы отыгрываете за персонажа, он может быть любым, но ограничения устанавливает администрация</i>
                                     ''',parse_mode='HTML' ,reply_markup=kb.main)
    
@router.callback_query(F.data == 'rpcommandbuttom')
async def defrpcommandsbutton(callback: CallbackQuery):
    await callback.answer('успешно')
    await callback.message.edit_text('''рп комманды: 
<b>*действие*</b>(или жирным текстом)
<i>шёпот</i>
(мысли)
//вне рп''',parse_mode='HTML' ,reply_markup=kb.main)

@router.callback_query(F.data == 'botcommandbt')
async def defrpcommandsbutton(callback: CallbackQuery):
    await callback.answer('успешно')
    await callback.message.edit_text('''ранд(рандом,rand,random) - кидает рандомное значение от 1 до 10
урон - кидает прокид на урон(1-100)
кубик - кидает кубик
женщина,мужчина - угар комманды''',parse_mode='HTML' ,reply_markup=kb.main)
