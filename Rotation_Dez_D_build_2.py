import datetime
import calendar


# from datetime import date, timedelta, datetime


# Создали класс хранения дез.средств Test
class Dez:

    def __init__(self, name, conc_regular, conc_general):
        self.name = name
        self.conc_regular = conc_regular
        self.conc_general = conc_general


almadez = Dez("«Алмадез»", "1%", "2%")
teflex = Dez("«Тефлекс»", "1,5%", "2,5%")
peroxide = Dez("«Прогресс» 0,5 % раствор + Перекись водорода", "3%", "6%")

dict_dez = {"a": almadez, "t": teflex, "p": peroxide}


def get_next(prev, cur):
    if prev == almadez and cur == peroxide:
        return teflex
    elif prev == teflex and cur == peroxide:
        return almadez
    elif prev == peroxide and (cur == teflex or cur == almadez):
        return peroxide
    elif (prev == almadez and cur == teflex) or (prev == teflex and cur == almadez) or (
            prev == peroxide and cur == peroxide):
        return print("Ошибка в перечне ротации! Перекись всегда идет между Алмадезом и Тефлексом!")


def get_week_day(year_cur, cur_month, day):
    return calendar.weekday(year_cur, cur_month, day)


def days_cur_month(year_cur, cur_month):
    # сделать автоматический рассчет last_day
    last_day = calendar.monthrange(year_cur, cur_month)[1]
    d1 = datetime.date(year_cur, cur_month, 1)
    d2 = datetime.date(year_cur, cur_month, last_day)
    days = [d1 + datetime.timedelta(days=x) for x in range((d2 - d1).days + 1)]

    return days


def generate_dez_list(all_days, prev, cur):
    # цикл по всем дням из days (обходим все дни месяца)
    for day in all_days:
        # определяем день недели для текущего дня
        temp_day = get_week_day(int(day.strftime('%Y')), int(day.strftime('%m')), int(day.strftime('%d')))
        # Если день недели - понедельник:
        if temp_day == 0:
            # меняем средство cur
            temp_dez = get_next(prev, cur)
            # а то, которое было cur, переносим в prev
            prev = cur
            cur = temp_dez

            print('(', temp_day, ')' + "\t " + day.strftime('%d.%m.%Y') + "\t " + cur.name + "\t " + cur.conc_general)
        else:
            print('(', temp_day,
                  ')' + "\t " + day.strftime('%d.%m.%Y') + "\t " + cur.name + "\t " + "\t " + cur.conc_regular)


all_days = days_cur_month(year_cur=int(input('Введите год (например, 2021): ')),
                          cur_month=int(input('Введите месяц (например, 7): ')))

generate_dez_list(all_days,
                  prev=dict_dez[input('Введите предыдущее дез.средство (a - Алмадез, t - Тефлекс, p - Перекись): ')],
                  cur=dict_dez[input('Введите текущее дез.средство (a - Алмадез, t - Тефлекс, p - Перекись): ')])
