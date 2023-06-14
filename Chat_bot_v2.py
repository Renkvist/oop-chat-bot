from __future__ import annotations
import math
import re
from typing import List
from colorama import Fore, Style
import datetime


# збереження діалогу
now = datetime.datetime.now()
file_name = f"dialog-{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

def save_message(author, text):
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    message = f"{time} - {author}: {text}\n"
    with open(file_name, 'a', encoding = "utf-8") as file:
        file.write(message)

def s_print(text):
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    author = 'Бот'
    message = f"{time} - {author}: {text}\n"
    with open(file_name, 'a', encoding = "utf-8") as file:
        file.write(message)
    print(text)

def s_input(text1):
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    author = 'Бот'
    message1 = f"{time} - {author}: {text1}\n"      
    with open(file_name, 'a', encoding = "utf-8") as file:
        file.write(message1)
    text2 = input(text1)

    time = now.strftime('%H:%M:%S')    
    author = 'Користувач'
    message2 = f"{time} - {author}: {text2}\n"
    with open(file_name, 'a', encoding = "utf-8") as file:
        file.write(message2)
    return text2

# означення функцій для підтем

# Математика та фізика
Ohm_power = lambda y, z: y/z
Ohm_voltage = lambda x, z: x*z
Ohm_resistance = lambda x, y: y/x

def Ohm():
    s_print(f'{Fore.BLUE}Введи значення для двох відомих величин, пропусти третю\nі я знайду її для тебе!')
    x = s_input(f'{Fore.BLUE}I (сила струму) = {Fore.YELLOW}')
    y = s_input(f'{Fore.BLUE}U (напруга) = {Fore.YELLOW}')
    z = s_input(f'{Fore.BLUE}R (сила опору) = {Fore.YELLOW}')
    try: x = float(x)
    except:
        try:
            float(y)
            float(z)
        except: s_print(f'{Fore.BLUE}Щось пішло не так(')
        else: s_print(f'{Fore.BLUE}I = {Ohm_power(float(y), float(z))} А')
    else:
        try: y = float(y)
        except:
            try:
                float(x)
                float(z)
            except: s_print(f'{Fore.BLUE}Щось пішло не так(')
            else: s_print(f'{Fore.BLUE}U = {Ohm_voltage(float(x), float(z))} В')
        else:
            try: z = float(z)
            except:
                try:
                    float(x)
                    float(y)
                except: s_print(f'{Fore.BLUE}Щось пішло не так(')
                else: s_print(f'{Fore.BLUE}R = {Ohm_resistance(float(x), float(y))} Ом')
            else: s_print(f'{Fore.BLUE}Щось пішло не так(')

Induction_function = lambda x, y: (1.2566 * 10**(-6) * x) / (2 * 3.14 * y)

def Induction():
    s_print(f'{Fore.BLUE}Введи значення для всіх величин,\nа я знайду значення індукції магнітного поля!')
    x = s_input(f'{Fore.BLUE}I (сила струму) = {Fore.YELLOW}')
    y = s_input(f'{Fore.BLUE}r (відстань до провідника (м)) = {Fore.YELLOW}')
    try:
        x = float(x)
        y = float(y)
    except: s_print(f'{Fore.BLUE}Щось пішло не так(')
    else: s_print(f'{Fore.BLUE}B = {Induction_function(float(x), float(y))} Тл')

Coulomb = '9 * 10^9 Н * м^2 / Кл^2'

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def LSM(x, y): return abs(x * y) // GCD(x, y)

def GCD_LSM():
    s_print(f'{Fore.BLUE}Введи значення двох чисел,\nа я знайду їхні найбільший спільний дільник (НСД)\nта найменше спільне кратне (НСК)!')
    x = s_input(f'{Fore.BLUE}Перше число = {Fore.YELLOW}')
    y = s_input(f'{Fore.BLUE}Друге число = {Fore.YELLOW}')
    try:
        x = float(x)
        y = float(y)
    except: s_print(f'{Fore.BLUE}Щось пішло не так(')
    else:
        s_print(f'{Fore.BLUE}НСД = {GCD(float(x), float(y))}')
        s_print(f'{Fore.BLUE}НСК = {LSM(float(x), float(y))}')

def arc_length():
    s_print(f'{Fore.BLUE}Введи значення радіусу кола та центрального кута α,\nа я знайду довжину дуги цього кола!')
    x = s_input(f'{Fore.BLUE}R (радіус) = {Fore.YELLOW}')
    y = s_input(f'{Fore.BLUE}α (кут у градусах) = {Fore.YELLOW}')
    try:
        x = float(x)
        y = float(y)
    except: s_print(f'{Fore.BLUE}Щось пішло не так(')
    else:
        s_print(f'{Fore.BLUE}L (довжина дуги кола) = {math.pi * {float(x)} * {float(y)} / 180}')

def triangle_area():
    s_print(f'''{Fore.BLUE}Наразі я вмію обчислювати площу трикутника лише за
формулою Герона (S = √p(p - a)(p - b)(p - c)).
Введи довжину трьох сторін, а я обрахую площу трикутника!''')
    x = s_input(f'{Fore.BLUE}Довжина першої сторони = {Fore.YELLOW}')
    y = s_input(f'{Fore.BLUE}Довжина другої сторони = {Fore.YELLOW}')
    z = s_input(f'{Fore.BLUE}Довжина третьої сторони = {Fore.YELLOW}')
    try:
        x = float(x)
        y = float(y)
        z = float(z)
    except: s_print(f'{Fore.BLUE}Щось пішло не так(')
    else:
        p = ((float(x) + float(y) + float(z)) / 2)
        S = math.sqrt(p * (p - float(x)) * (p - float(y)) * (p - float(z)))
        s_print(f'{Fore.BLUE}S (площа) = {S}')

sin = lambda x: math.sin(x)
cos = lambda x: math.cos(x)

def sin_cos():
    s_print(f'{Fore.BLUE}Введи градус кута, а я знайду його синус та косинус!')
    x = s_input(f'{Fore.BLUE}x = {Fore.YELLOW}')
    try: x = float(x)
    except: s_print(f'{Fore.BLUE}Щось пішло не так(')
    else: 
        x = math.radians(x)
        s_print(f'''{Fore.BLUE}sin(x) = {sin(float(x))}
cos(x) = {cos(float(x))}''')

# Географія
ocean = '''Найбільшим за площею океаном є Тихий океан, його площа складає близько
165,25 мільйонів квадратних кілометрів. Він займає майже 46% водної
поверхні Землі. Щоб краще уявити ці розміри, площа України (603 628 км^2)
є у 273 рази меншою!'''

city = '''За офіційними даними станом на 2021 рік, місто Токіо в Японії є містом
з найбільшою кількістю населення в світі, воно становить близько
38 мільйонів людей.'''

desert = '''Найбільшою пустелею в світі після Сахари є Пустеля Гобі, яка простягається
на площі близько 500 000 квадратних кілометрів, з яких приблизно
третина пустелі знаходиться на території північної частини Китаю,
а решта дві третини - в південній частині Монголії.'''

def azimuth():
    s_print(f'{Fore.BLUE}Послідовно введи координати двох точок, а я знайду азимут між ними!')
    x1 = s_input(f'{Fore.BLUE}Широта першої точки (від -90 до 90) = {Fore.YELLOW}')
    y1 = s_input(f'{Fore.BLUE}Довгота першої точки (від -180 до 180) = {Fore.YELLOW}')
    x2 = s_input(f'{Fore.BLUE}Широта другої точки (від -90 до 90) = {Fore.YELLOW}')
    y2 = s_input(f'{Fore.BLUE}Довгота другої точки (від -180 до 180) = {Fore.YELLOW}')
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except: s_print(f'{Fore.BLUE}Щось пішло не так(')
    else:
        x1_rad = math.radians(x1)
        y1_rad = math.radians(y1)
        x2_rad = math.radians(x2)
        y2_rad = math.radians(y2)
        diff_lon = y2_rad - y1_rad
        x = math.cos(x2_rad) * math.sin(diff_lon)
        y = math.cos(x1_rad) * math.sin(x2_rad) - math.cos(x2_rad) * math.sin(x1_rad) * math.cos(diff_lon)
        azimuth_rad = math.atan2(x, y)
        azimuth_deg = math.degrees(azimuth_rad)
        azimuth_deg = (azimuth_deg + 360) % 360
        s_print(f'{Fore.BLUE}Азимут = {azimuth_deg} градусів')

# Філологія
ten_p1 = f'''Всього англійська мова налічує 12 часів за класичним підходом до граматики.
Якщо розглядати їх детальніше, то існує 3 види часу для кожної групи
і 4 групи для кожного виду часу.
{Style.BRIGHT}Група Simple:
{Style.NORMAL}Present Simple використовують для виразу звичайної, регулярно повторюваної дії.
Past Simple використовують для виразу дії, яка відбулася у минулому.
Future Simple використовують для виразу дії, яка відбудеться у майбутньому.
{Style.BRIGHT}Група Continuous:
{Style.NORMAL}Present Continuous використовують для виразу дії, яка відбувається на даний
момент.
Past Continuous використовують для виразу дії, яка вже відбулася в певний
момент часу у минулому.
Future Continuous використовують для виразу дії, яка буде відбуватися у певний
момент часу в майбутньому.'''
ten_p2 = f'''{Style.BRIGHT}Група Perfect:
{Style.NORMAL}Present Perfect використовують для виразу дії, яка відбулася (або яка
відбувається), результат якої зв’язаний з теперішнім.
Past Perfect використовують для виразу дії, яка закінчилася раніше другої дії
або певного моменту у минулому.
Future Perfect використовують для виразу дії, яка завершиться до певного
моменту часу в майбутньому.
{Style.BRIGHT}Група Perfect Continuous:
{Style.NORMAL}Present Perfect Continuous використовують для виразу дії, яка розпочалася в
минулому і продовжується у теперішньому часі, або ж важлива тривалість дії.
Past Perfect Continuous використовують для виразу дії, яка розпочалася в
певний момент у минулому і продовжувалася деякий час до початку другої дії.
Future Perfect Continuous використовують для виразу дії, яка розпочавшись у
певний момент, все ще буде продовжуватися в якийсь момент часу у майбутньому.
'''
def tenses():
    s_print(Fore.BLUE + ten_p1)
    s_print(Fore.BLUE + ten_p2)

noun = '''Іменник та прикметник — різні частини мови. Іменник виконує функцію називання
предмета чи явища, тоді як основна функція прикметника — описати
цей предмет або явище. В українській мові прикметники також змінюються
не лише за відмінками і числом, а й за родами, на відміну від іменника.'''

# Робота з текстом
def abs_freq():
    path = s_input(f'''{Fore.BLUE}Введіть шлях до файлу, з яким будемо працювати.
Наприклад, "C:\\Users\\Renkvist\\Desktop\\Файлик.txt"
{Fore.YELLOW}''')
    word = s_input(f'{Fore.BLUE}Тепер введи слово, яке потрібно шукати: {Fore.YELLOW}')
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        s_print(f'{Fore.BLUE}Файл за вказаним шляхом не знайдено 🤷‍♂️')
    word_number = (text.lower().count(word.lower()))
    suffix = ("" if word_number == 1 or word_number % 10 == 1 else
            "и" if 2 <= word_number % 10 <= 4 else
            "ів")
    s_print(f'{Fore.BLUE}Шукане слово зустрічається {word_number} раз{suffix}')

def pal():
    path = s_input(f'''{Fore.BLUE}Зауваж, я можу знайти лише слова-паліндроми, а вирази, що складаються
з кількох слів і теж є паліндромами, я знайти не зможу!
Введіть шлях до файлу, з яким будемо працювати.
Наприклад, "C:\\Users\\Renkvist\\Desktop\\Файлик.txt"
{Fore.YELLOW}''')
    words_list = []
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        s_print(f'{Fore.BLUE}Файл за вказаним шляхом не знайдено 🤷‍♂️')
    for item in text.split():
        words_list.append(re.sub(r'[\d\W_]', '', item).lower())
    palindromes = []
    for word in words_list:
        if word == word[::-1]: palindromes.append(word)
    if not palindromes:
        s_print(f'{Fore.BLUE}На жаль, не вдалось знайти жодного паліндрома')
    else:
        s_print(f'{Fore.BLUE}Ось список усіх паліндромів, що мені вдалося знайти:')
        for word in palindromes: s_print(f'{Fore.BLUE}{word}')

def del_space():
    path = s_input(f'''{Fore.BLUE}Введіть шлях до файлу, з яким будемо працювати.
Наприклад, "C:\\Users\\Renkvist\\Desktop\\Файлик.txt"
{Fore.YELLOW}''')
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        s_print(f'{Fore.BLUE}Файл за вказаним шляхом не знайдено 🤷‍♂️')
    r_text = text.split()
    with open(path, 'w', encoding = 'utf-8') as file:
        file = file.write(r_text)
    s_print(f'{Fore.BLUE}Тепер із тексту прибрано усі зайві пробіли.')

def alph_sort():
    path = s_input(f'''{Fore.BLUE}Введіть шлях до файлу, з яким будемо працювати.
Наприклад, "C:\\Users\\Renkvist\\Desktop\\Файлик.txt"
{Fore.YELLOW}''')
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        s_print(f'{Fore.BLUE}Файл за вказаним шляхом не знайдено 🤷‍♂️')
    words = text.split()
    sorted_words = sorted(words, key=str.lower)
    sorted_text = ' '.join(sorted_words)
    with open(path, 'w', encoding = 'utf-8') as file:
            text = file.write(sorted_text)
    s_print(f'{Fore.BLUE}Тепер текст відсортовано за алфавітом.')

def longest_starts_vowel():
    path = s_input(f'''{Fore.BLUE}Введіть шлях до файлу, з яким будемо працювати.
Наприклад, "C:\\Users\\Renkvist\\Desktop\\Файлик.txt"
{Fore.YELLOW}''')
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        s_print(f'{Fore.BLUE}Файл за вказаним шляхом не знайдено 🤷‍♂️')
    vowels = ['а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']
    words = text.lower().split()
    longest_word = ''
    longest_words = []
    for word in words:
        for x in vowels:
            check = word.startswith(x)
            if check == True:
                if len(longest_word) < len(word):
                    longest_word = word
                    longest_words = []
                    longest_words.append(word)
                elif len(longest_word) == len(word):
                    longest_words.append(word)
    if not longest_words: s_print(f'{Fore.BLUE}На жаль, не вдалося знайти жодного слова, що починалося б із голосної.')
    else:
        s_print(f'{Fore.BLUE}Ось список усіх найдовших слів, що починаються із голосної:')
        for word in longest_words: s_print(f'{Fore.BLUE}{word}')

def longest_without_vowels():
    path = s_input(f'''{Fore.BLUE}Введіть шлях до файлу, з яким будемо працювати.
Наприклад, "C:\\Users\\Renkvist\\Desktop\\Файлик.txt"
{Fore.YELLOW}''')
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        s_print(f'{Fore.BLUE}Файл за вказаним шляхом не знайдено 🤷‍♂️')
    vowels = ['а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']
    words = text.lower().split()
    no_vowels_words = [word for word in words if not any(vowel in word for vowel in vowels)]
    longest_word = ''
    longest_words = []
    for word in no_vowels_words:
        if len(longest_word) < len(word):
            longest_word = word
            longest_words = []
            longest_words.append(word)
        elif len(longest_word) == len(word):
            longest_words.append(word)
    if not longest_words: s_print(f'{Fore.BLUE}На жаль, не вдалося знайти жодного слова, що не містило б голосних.')
    else:
        s_print(f'{Fore.BLUE}Ось список усіх найдовших слів, що не містять голосних:')
        for word in longest_words: s_print(f'{Fore.BLUE}{word}')

# Загальні
def current_time():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M:%S')
    s_print(f'{Fore.BLUE}Зараз {time}')

def current_month():
    now = datetime.datetime.now()
    month_number = now.month
    month_list = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
    for month in range(len(month_list)):
        if month_number == month: s_print(f'{Fore.BLUE}Надворі ось цей місяць — {month_list[month]}')

songs = '''Я як бот не можу мати вподобань, тому наведу топ-5 пісень мого власника.
1. Evanescence — Bring Me To Life
2. Within Temptation — Ice Queen
3. Nickelback — When We Stand Together
4. Evanescence — Erase This
5. Арсен Мірзоян — Бувай малий
'''

topics_dictionary = {
    'Математика й фізика': {'Закон Ома': Ohm, 'Формула Ампера': Induction,
    'Кулонівська стала': Coulomb, 'Найбільший спільний дільник і найменше спільне кратне': GCD_LSM,
    'Довжина дуги кола': arc_length, 'Площа трикутника': triangle_area,
    'sin(x) та cos(x)': sin_cos}, 
    'Географія': {'Найбільший океан': ocean, 'Найзаселеніше місто': city,
    '2-га найбільша пустеля': desert, 'Азимут від точки А до точки B': azimuth},
    'Філологія': {'Часи в англійській мові': tenses, 'Різниця між іменником та прикметником': noun},
    'Робота з текстом': {'Абсолютна частота слова в тексті': abs_freq, 'Пошук паліндромів': pal, 
    'Видалення зайвих пробілів': del_space, 'Сортування слів за алфавітом': alph_sort, 
    'Найдовші слова, що починаються з голосної': longest_starts_vowel, 'Найдовші слова без голосних':
    longest_without_vowels},
    'Загальні': {'Котра година?': current_time, 'Який зараз місяць?': current_month, '5 улюблених пісень':
    songs}
}

user_message = ''
bot_message = ''
topics_number_dict = topics_dictionary.copy()
subtopics_number_dict = topics_dictionary.copy()
topic_matches = '' 
subtopic_matches = ''  
def topics():
    global topic_matches
    topic_number = 0
    for key in topics_number_dict.keys():
        topic_number += 1
        topic_match = f'{key} — {str(topic_number)}'
        topic_matches += (f'{topic_match}\n')
        topics_number_dict[key] = topic_number
        subtopics_number_dict[topic_number] = subtopics_number_dict.pop(key)
    return topic_matches
topics()

def subtopics(number):
    subtopic_number = 0
    global subtopic_matches
    for x in subtopics_number_dict.get(number):
        subtopic_number += 1
        subtopic_match = f'{x} — {str(subtopic_number)}'
        subtopic_matches += (f'{subtopic_match}\n')
    return subtopic_matches


tutorial = f'''{Fore.BLUE}Щоб обрати тему, введи її номер в головному меню.
Щоб повернутись у меню, напиши "назад".
Щоб завершити сеанс, напиши "вихід".

Список наявних тем:
{topic_matches}'''


# інтерфейс

class Chat_Bot:

    def select_topic(self):
        global user_message
        global tutorial
        global topics_number_dict
        global subtopics_number_dict
        s_print(f'''{Fore.BLUE}Привіт! Я — твій універсальний помічник (або принаймні постараюсь таким бути).
Ти можеш задати мені будь-які запитання із списку для кожної окремої теми,
якою я володію.
Щоб розібратись із навігацією, напиши "керування".

{tutorial}''')
        while user_message != "вихід":
            user_message = input(Fore.YELLOW).lower()
            save_message('Користувач', user_message)
            if user_message == "вихід":
                s_print(Fore.BLUE + 'Бувайте!')
                break
            elif user_message == 'керування':
                s_print(tutorial)
                continue
            elif user_message == 'назад':
                s_print(Fore.BLUE + 'Ви вже в головному меню!')
                continue
            else:
                try:
                    user_message = int(user_message)
                except:
                    s_print(Fore.BLUE + 'Я не розумію цієї команди 🤨')
                    continue
                choice_1 = 0
                for key in topics_number_dict.keys():
                    choice_1 += 1
                    if user_message == choice_1: 
                        self.select_subtopic(choice_1)
                        if user_message == "вихід":
                            break
                        elif user_message == "назад":
                            s_print(f'''{Fore.BLUE}Вітаю в головному меню!
                                    
Список наявних тем:
{topic_matches}''')
                            break
                else:
                    s_print(Fore.BLUE + 'Теми під таким номером не існує 🫥')
                    continue

    def select_subtopic(self, choice_1):
        global user_message
        global subtopic_matches
        global topics_dictionary
        subtopic_matches = ''
        subtopics(choice_1)
        s_print(f'''{Fore.BLUE}
Оберіть підтему:
{subtopic_matches}''')
        key_1 = list(topics_number_dict.keys())[choice_1-1]
        while True:
            user_message = input(Fore.YELLOW).lower()
            save_message('Користувач', user_message)
            if user_message == "вихід":
                s_print(Fore.BLUE + 'Бувайте!')
                break
            elif user_message == 'керування':
                s_print(tutorial)
                continue
            elif user_message == 'назад':
                break
            else:
                try:
                    user_message = int(user_message)
                except:
                    s_print(Fore.BLUE + 'Я не розумію цієї команди 🤨')
                    continue
                choice_2 = 0
                for x in subtopics_number_dict.get(choice_1):
                    choice_2 += 1
                    if user_message == choice_2:
                        try: key_2 = list(topics_dictionary[key_1].values())[choice_2-1]()
                        except: key_2 = s_print(Fore.BLUE + list(topics_dictionary[key_1].values())[choice_2-1])
                        s_print(f'''{Fore.BLUE}
Оберіть підтему:
{subtopic_matches}''')
                        break
                else:
                    s_print(Fore.BLUE + 'Підтеми під таким номером не існує 🫥')
                    continue

bot = Chat_Bot()
bot.select_topic()