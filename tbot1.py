
import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5356155891:AAH537_I0Syqo5-BmF1hvYZWQ-QNYT-vv64'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply( f"Assalomu alaykum {format(message.from_user.first_name)}. \n Wikipedia botga xush kelibsiz ! \n Men siz yozgan so`z va iboralar bo`yicha ma'lumotlarni "
                        f"chiqarib beruvchi botman\n Biror bir Adabiy so'z kiriting (joy nomi, mashhurlar ismi ...)\n Commandalar bilan tanishish uchun pastki chap burchakdagi"
                        f" ""menu"" tugmasini bosing, yoki /command buyrug`ini kiriting")

@dp.message_handler(commands=['command'])
async def send_about(message: types.Message):
    await message.reply("/uzbek-Ma'lumotni o'zbek tilida olish; \n /russian-Ma'lumotni rus tilida olish \n /english-Ma'lumotni ingliz tilida olish \n"
                        "/about-dasturchi haqida \n /command-buyruqlar bilan tanishish")

@dp.message_handler(commands=['about'])
async def send_about(message: types.Message):
    await message.reply(f"Bot dasturchisi Samarqand Davlat Universtiteti 1-bosqich talabasi Jaloliddinov Jafar. \n"
                        f"Phone number: +998 90 224 48 02\n"
                        f"Telegram: @jaloliddinov \n"
                        f"Instagram: https://instagram.com/jafar.jaloliddinov \n https://instagram.com/j_it_specialist")


@dp.message_handler(commands=['uzbek'])
async def send_about(message: types.Message):
    await message.reply("Ma'lumotlarni 🇺🇿O`ZBEK🇺🇿 tilida chop etish faollashtirildi. O`zgartirish uchun👇🏻\n /russian-Ma'lumotni rus tilida olish \n "
                        "/english-Ma'lumotni ingliz tilida olish")
    wikipedia.set_lang('uz')

@dp.message_handler(commands=['russian'])
async def send_about(message: types.Message):
    await message.reply("Активирована печать данных на 🇷🇺РУССКОМ🇷🇺 языке. Редактировать👇🏻\n "
                        "/uzbek-Получение информации на узбекском языке; \n /english-Получение информации на английском языке")
    wikipedia.set_lang('ru')

@dp.message_handler(commands=['english'])
async def send_about(message: types.Message):
    await message.reply("Data printing in 🇬🇧ENGLISH🇬🇧 has been activated. \nChange👇🏻 \n"
                        "/uzbek-Getting information in Uzbek; \n /english-Getting information in English")
    wikipedia.set_lang('')

@dp.message_handler()
async def send(message: types.Message):
    try:
         resp = wikipedia.summary(message.text)
         await message.answer(resp)
    except:
        await message.answer("Bu so'z bo'yicha uz.wikipedia.org da ma'lumot mavjud emas !")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)