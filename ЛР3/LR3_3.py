# TODO  Напишите функцию count_letters
def count_letters(main_str):
    i = 0
    while i < len(main_str):
        if main_str[i].isalpha() == False:
            main_str = main_str[:i] + " " + main_str[i + 1:]
        i += 1
    str_clear = ''.join(main_str.lower().split())
    return {letter: str_clear.count(letter) for letter in str_clear}

# TODO Напишите функцию calculate_frequency
def calculate_frequency(spisok_bukv):
    vsego_bukv = sum(spisok_bukv.values())
    bukvi = list(spisok_bukv)

    for i in bukvi:
        ch = spisok_bukv[i] / vsego_bukv
        spisok_bukv[i] = round(ch, 2)
    return spisok_bukv




main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
spisok_bukv = count_letters(main_str)
ch_spisok_bukv = calculate_frequency(spisok_bukv)
bukvi = list(ch_spisok_bukv)
for i in bukvi:
    print(f"{i}: {ch_spisok_bukv[i]:.2f}")