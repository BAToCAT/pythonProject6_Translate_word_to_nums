
dict = {
    "ты": 1000, "м": 1000000,
    "сто": 100, "двес": 200, "трис": 300, "четырес": 400, "пятьс": 500, "шестьс": 600, "семьс": 700, "восемьс": 800, "девятьс": 900,
    "одинн": 11, "двен": 12, "трин": 13, "четырн": 14, "пятн": 15, "шестн": 16, "семн": 17, "восемн": 18, "девятн": 19,
    "двад": 20, "трид": 30, "сор": 40, "пятьд": 50, "шестьд": 60, "семьд": 70, "восемьд": 80, "девяно": 90,
    "деc": 10, "н": 0, "о": 1, "дв": 2, "т": 3, "ч": 4, "п": 5, "ш": 6, "с": 7, "в": 8, "д": 9, }

def string_to_number(s):
    sum = 0
    tmp = 0
    words = s.split()
    keys = list(dict.keys())
    for word in words:
        number = dict[next(filter(lambda key : word.startswith(key), keys))]
        if tmp > 0 and number > 900:
            sum = sum + (number * tmp)
            tmp = 0
        else:
            tmp = tmp + number
    return sum + tmp
print(string_to_number('тысяча'))