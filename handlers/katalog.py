from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user_state import BoglanishState, BoshqaRazmer
from keyboards.default.users_keyboard import send_contact, users_keyboard
from keyboards.inline.katalog_inline import category_keyboard, muddatli_tolov
from loader import dp, db, BASE, bot



@dp.message_handler(text="Бизнинг Каталог 📒")
async def bizning_katalog(message: types.Message):
    await message.answer(f"Ассалому алайкум {message.from_user.first_name}\nКеракли бўлим танланг ✅", reply_markup=await category_keyboard())


@dp.callback_query_handler(lambda call: call.data.split('_')[0] == "cat")
async def inline_katalog_callback(call: types.CallbackQuery, state: FSMContext):
    id = call.data.split('_')[1]
    data = await db.get_sub_categories(int(id))
    if data:
        media = []
        for i in data:
            work = types.InlineKeyboardButton(text=f'{i[1]}', callback_data=f'sub_{i[0]}')
            btn_work = types.InlineKeyboardMarkup(inline_keyboard=[[work]])
            for j in i[2:6]:
                media.append(types.InputMediaPhoto(media=open(f"{BASE}/admin/media/{j}", 'rb')))
            if len(media) == 4:
                await bot.send_media_group(chat_id=call.message.chat.id, media=media)
                await call.message.answer(f"⚜ {i[1]} ⚜ Коллекцияси учун гиламлар тўплами", reply_markup=btn_work)
                media = []
    else:
        await call.message.answer("Гиламлар мавжуд эмас ⛔")


@dp.callback_query_handler(lambda call: call.data.split('_')[0] == 'sub')
async def product_katalog_inline(call: types.CallbackQuery):
    _id = call.data.split('_')[1]
    sub_data = await db.get_products_sub(int(_id))
    n = 1
    data = await db.get_product(int(_id))
    if data and len(data) > 1:
        boshqa_razmer = types.InlineKeyboardButton("🛠 Бошқа размер ⚙️", callback_data=f"razmer_{n}_{_id}_{data[n - 1][0]}")
        muddat = types.InlineKeyboardButton("⏳ Муддатли толов ⏳", callback_data=f"muddat_{n}_{_id}_{data[n - 1][0]}")
        end = types.InlineKeyboardButton('🔙', callback_data=f'back_{len(data) if n == 1 else n - 1}_{_id}')
        work = types.InlineKeyboardButton('💳 Сотиб Олиш 💸', callback_data=f'work_{n}_{_id}_{data[n - 1][0]}')
        next = types.InlineKeyboardButton('🔜', callback_data=f'next_{1 if n == len(data) else n + 1}_{_id}')
        btn = types.InlineKeyboardMarkup(inline_keyboard=[[boshqa_razmer], [work], [muddat], [end, next]])
        if data[n - 1][-3] == True:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅", reply_markup=btn, parse_mode="HTML")
        elif data[n - 1][-3] == False:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌", reply_markup=btn, parse_mode="HTML")

    elif data and len(data) == 1:
        boshqa_razmer = types.InlineKeyboardButton("🛠 Бошқа размер ⚙️", callback_data=f"razmer_{n}_{id}_{data[n - 1][0]}")
        muddat = types.InlineKeyboardButton("⏳ Муддатли толов ⏳", callback_data=f"muddat_{n}_{id}_{data[n - 1][0]}")
        work = types.InlineKeyboardButton('💳 Сотиб Олиш 💸', callback_data=f'work_{n}_{id}_{data[n - 1][0]}')
        btn_work = types.InlineKeyboardMarkup(inline_keyboard=[[boshqa_razmer], [work], [muddat]])
        if data[n - 1][-3] == True:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅", reply_markup=btn_work, parse_mode="HTML")
        elif data[n - 1][-3] == False:
            await call.message.answer_photo(photo=open(f"{BASE}/admin/media/{data[n - 1][1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[n - 1][4]} x {data[n - 1][5]}\n<b>Нархи:</b> {data[n - 1][4] * data[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌", reply_markup=btn_work, parse_mode="HTML")
    else:
        await call.message.answer(text='Ҳозирча Гиламлар мавжуд эмас!')


@dp.callback_query_handler(lambda callback: callback.data.split('_')[0] in ['back', 'work', 'next', 'razmer', 'muddat'])
async def callback_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    _id = callback.data.split('_')[2]
    sub_data = await db.get_products_sub(int(_id))
    stories = await db.get_product(int(_id))
    n = 1
    text = callback.data.split('_')
    if text[0] == 'back':
        n = int(text[1])
    elif text[0] == 'work':
        index = int(callback.data.split('_')[3])
        async with state.proxy() as data:
            data['media_id'] = index
            data['sub_id'] = _id
        await BoglanishState.phone.set()
        await callback.message.answer(text="Телефон рақамингизни юборинг ☎", reply_markup=send_contact)
        return
    elif text[0] == 'razmer':
        index = int(callback.data.split('_')[3])
        async with state.proxy() as data:
            data['media_id'] = index
            data['sub_id'] = _id
            data['n'] = n
        await BoshqaRazmer.boyi.set()
        await callback.message.answer(text="Гилам бойини киритинг ✍️")
        return
    elif text[0] == 'muddat':
        index = int(callback.data.split('_')[3])
        product = await db.get_products(int(index))
        if product[-3] == True:
            await callback.message.answer_photo(photo=open(f"{BASE}/admin/media/{product[1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {product[2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {product[3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {product[4]} x {product[5]}\n<b>Нархи:</b> {product[4] * stories[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅", reply_markup=await muddatli_tolov(product[0], _id), parse_mode="HTML")
        elif product[-3] == False:
            await callback.message.answer_photo(photo=open(f"{BASE}/admin/media/{product[1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {product[2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {product[3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {product[4]} x {product[5]}\n<b>Нархи:</b> {product[4] * stories[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌", reply_markup=await muddatli_tolov(product[0], _id), parse_mode="HTML")
        return
    elif text[0] == 'next':
        n = int(text[1])
    boshqa_razmer = types.InlineKeyboardButton("🛠 Бошқа размер ⚙️", callback_data=f"razmer_{n}_{_id}_{stories[n - 1][0]}")
    muddat = types.InlineKeyboardButton("⏳ Муддатли толов ⏳", callback_data=f"muddat_{n}_{_id}_{stories[n - 1][0]}")
    end = types.InlineKeyboardButton('🔙', callback_data=f'back_{len(stories) if n == 1 else n - 1}_{_id}')
    work = types.InlineKeyboardButton('💳 Сотиб Олиш 💸', callback_data=f'work_{n}_{_id}_{stories[n - 1][0]}')
    next = types.InlineKeyboardButton('🔜', callback_data=f'next_{1 if n == len(stories) else n + 1}_{_id}')
    btn = types.InlineKeyboardMarkup(inline_keyboard=[[boshqa_razmer], [work], [muddat], [end, next]])
    if stories[n - 1][-3] == True:
        await callback.message.answer_photo(photo=open(f"{BASE}/admin/media/{stories[n - 1][1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {stories[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {stories[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {stories[n - 1][4]} x {stories[n - 1][5]}\n<b>Нархи:</b> {stories[n - 1][4] * stories[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅", reply_markup=btn, parse_mode="HTML")
    elif stories[n - 1][-3] == False:
        await callback.message.answer_photo(photo=open(f"{BASE}/admin/media/{stories[n - 1][1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {stories[n - 1][2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {stories[n - 1][3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {stories[n - 1][4]} x {stories[n - 1][5]}\n<b>Нархи:</b> {stories[n - 1][4] * stories[n - 1][5] * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌", reply_markup=btn, parse_mode="HTML")
    await callback.answer(str(f"📑 Сиз шу саҳифадасиз: {n}"))


@dp.callback_query_handler(lambda call: call.data.split('_')[0] == "time")
async def time_query_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    lifetime = callback.data.split('_')[1]
    time_id = callback.data.split('_')[2]
    sub_id = callback.data.split('_')[3]
    product = await db.get_products(int(time_id))
    sub = await db.get_products_sub(int(sub_id))
    if product:
        kvadrat = (product[4] * product[5])
        one_foiz = sub[-2] / 100
        oylik_koeffitsient = lifetime / 3
        narx = ((one_foiz * (8 * oylik_koeffitsient) + sub[-2]) * kvadrat) / lifetime
        await callback.message.answer(f"Махсулотни <b>{lifetime}</b> ойлик муддатли тўловга харид қилсангиз ҳар ой <b>{narx}</b> сўмдан тўлашингиз керак бўлади!")
   

@dp.message_handler(state=BoshqaRazmer.boyi)
async def boshqa_razmer_boyi_handler(message: types.Message, state: FSMContext):
    try:
        boy = float(message.text)
    except:
        await message.answer("Илтимос рақам киритинг ♻️")
    else:
        async with state.proxy() as data:
            data['boy'] = boy
        await BoshqaRazmer.eni.set()
        await message.answer("Гилам энини киритинг ✍️")


@dp.message_handler(state=BoshqaRazmer.eni)
async def boshqa_razmer_eni_handler(message: types.Message, state: FSMContext):
    try:
        eni = float(message.text)
    except:
        await message.answer("Илтимос рақам киритинг ♻️")
    else:
        async with state.proxy() as datas:
            sub_id = datas['sub_id']
            product_id = datas['media_id']
            n = datas['n']
        sub_data = await db.get_products_sub(int(sub_id))
        data = await db.get_product(int(sub_id))
        product = await db.get_products(int(product_id))
        boshqa_razmer = types.InlineKeyboardButton("🛠 Бошқа размер ⚙️", callback_data=f"razmer_{n}_{datas['sub_id']}_{product[0]}")
        muddat = types.InlineKeyboardButton("⏳ Муддатли толов ⏳", callback_data=f"muddat_{n}_{datas['sub_id']}_{product[0]}")
        end = types.InlineKeyboardButton('🔙', callback_data=f"back_{len(data) if n == 1 else n - 1}_{datas['sub_id']}")
        work = types.InlineKeyboardButton('💳 Сотиб Олиш 💸', callback_data=f"work_{n}_{datas['sub_id']}_{product[0]}")
        next = types.InlineKeyboardButton('🔜', callback_data=f"next_{1 if n == len(data) else n + 1}_{datas['sub_id']}")
        btn = types.InlineKeyboardMarkup(inline_keyboard=[[work], [boshqa_razmer], [muddat], [end, next]])
        if product[-3] == True:
            await message.answer_photo(photo=open(f"{BASE}/admin/media/{product[1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {product[2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {product[3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {datas['boy']} x {eni}\n<b>Нархи:</b> {float(datas['boy']) * eni * sub_data[-2]} сум\n\nНасия Савдо Мавжуд ✅", reply_markup=btn, parse_mode="HTML")
        elif product[-3] == False:
            await message.answer_photo(photo=open(f"{BASE}/admin/media/{product[1]}", 'rb'), caption=f"<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {product[2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {product[3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {datas['boy']} x {eni}\n<b>Нархи:</b> {float(datas['boy']) * eni * sub_data[-2]} сум\n\nНасия Савдо Мавжуд Емас ❌", reply_markup=btn, parse_mode="HTML")
        await state.finish()


@dp.message_handler(state=BoglanishState.phone, content_types=types.ContentType.CONTACT)
async def phone_handler(message: types.Message, state: FSMContext):
    try:
        await message.answer("Телефон рақамингизни юборганингиз учун раҳмат!😊\nТез орада операторларимиз сиз билан боғланишади 👩🏻‍💻", reply_markup=users_keyboard)
        async with state.proxy() as data:
            _id = data['media_id']
            sub_id = data['sub_id']
        data = await db.get_products(int(_id))
        sub_data = await db.get_products_sub(int(sub_id))
        await bot.send_message(chat_id=5553781606, text=f"Mijoz Telefon raqami: {message.contact.phone_number}\n\nXarid qilmoqchi 🤝:\n\n<b>Коллекция:</b> {sub_data[1]}\n<b>Стиль:</b> {data[2]}\n<b>Ип тури:</b> {sub_data[-6]}\n<b>Ворси баландлиги:</b> {sub_data[-4]}\n<b>Зичлиги:</b> {sub_data[-5]}\n<b>Форма:</b> {data[3]}\n<b>Ранглар:</b> {sub_data[-3]}\n<b>Размер:</b> {data[4]} x {data[5]}\n<b>Нархи:</b> {data[4] * data[5] * sub_data[-2]} сум\n")
        await state.finish()
    except Exception as e:
        print(f"An exception occurred: {e}")


@dp.message_handler(commands="start", state=BoglanishState.phone)
async def start_phone(message: types.Message, state: FSMContext):
    await message.answer("Bosh Menu 🏠", reply_markup=users_keyboard)
    await state.finish()
