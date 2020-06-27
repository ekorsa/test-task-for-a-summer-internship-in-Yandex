# Задача 2. Встречи
# Чтобы не мешать коллегам на рабочем месте громкими обсуждениями, ребята
# назначают встречи на определенное время и бронируют переговорки. При
# бронировании нужно указать дату и время встречи, её длительность и список
# участников. Если у кого-то из участников получается две встречи в один и тот
# же момент времени, то в бронировании будет отказано с указанием списка людей,
# у которых время встречи пересекается с другими встречами. Вам необходимо
# реализовать прототип такой системы.
#
# Формат ввода
# В первой строке входного файла содержится одно число n (1 ≤ n ≤ 1000) — число
# запросов.
#
# В следующих n строках содержатся запросы по одному в строке. Запросы бывают
# двух типов:
#
# APPOINT day time duration k names1 names2… namesk
# PRINT day name
# day — номер дня в 2018 году (1 ≤ day ≤ 365)
#
# time — время встречи, строка в формате HH:MM (08 ≤ HH ≤ 21, 00 ≤ MM ≤ 59)
#
# duration — длительность встречи в минутах (15 ≤ duration ≤ 120)
#
# k — число участников встречи (1 ≤ k ≤ 10)
#
# namesi, name — имена участников, строки, состоящие из маленьких латинских
# букв (1 ≤ |name| ≤ 20). У всех коллег уникальные имена. Кроме того
# гарантируется, что среди участников одной встречи ни одно имя не встречается
# дважды.
#
# Формат вывода
# Если удалось назначить встречу (первый тип запросов), выведите OK.
#
# Иначе выведите в первой строке FAIL, а в следующей строке через пробел список
# имен участников, для которых время встречи пересекается с другими встречами,
# в том порядке, в котором имена были даны в запросе.
#
# Для второго типа запросов выведите для данного дня и участника список всех
# событий на данный момент в этот день в хронологическом порядке, по одному в
# строке, в формате
#
# HH:MM duration names1 names2 … namesk
#
# где имена участников следуют в том же порядке, что и в исходном описании
# встречи. Если событий в данный день для этого человека нет, то ничего
# выводить не нужно.
# Пример 1.
# Ввод
# 7
# APPOINT 1 12:30 30 2 andrey alex
# APPOINT 1 12:00 30 2 alex sergey
# APPOINT 1 12:59 60 2 alex andrey
# PRINT 1 alex
# PRINT 1 andrey
# PRINT 1 sergey
# PRINT 2 alex
# Вывод
# OK
# OK
# FAIL
# alex andrey
# 12:00 30 alex sergey
# 12:30 30 andrey alex
# 12:30 30 andrey alex
# 12:00 30 alex sergey


import datetime as dt


class Record:
    def __init__(self, record):
        day, time, duration, number_of_participants, *names_of_participants = record
        date_format = '%Y %j %H:%M'
        time = dt.datetime.strptime(f'2018 {day} {time}', date_format)
        self.begin_time = time
        self.end_time = time + dt.timedelta(minutes=int(duration))
        self.number_of_participants = number_of_participants
        self.names_of_participants = names_of_participants
        self.duration = duration


class MeetingRoom:
    def __init__(self):
        self.records = []

    def add_record(self, in_command):
        command = in_command.split(' ')
        if command[0] == 'APPOINT':
            self.appoint(command[1:])
        elif command[0] == 'PRINT':
            self.print_meeting(command[1:])

    def print_meeting(self, record):
        day, name_of_participants = record
        date_format = '%Y %j'
        time = dt.datetime.strptime(f'2018 {day}', date_format)
        for item_record in self.records:
            if time.date() == item_record.begin_time.date() and name_of_participants in item_record.names_of_participants:
                print(item_record.begin_time, item_record.duration,
                      *item_record.names_of_participants)

    def appoint(self, record):
        occupied = False
        new_record = Record(record)
        if len(self.records) == 0:
            self.records.append(Record(record))
            print('OK')
        else:
            for item_record in self.records:
                it_begin = item_record.begin_time
                it_end = item_record.end_time
                nr_begin = new_record.begin_time
                nr_end = new_record.end_time
                if not (nr_end <= it_begin or nr_begin >= it_end):
                    occupied = True
            if occupied:
                print('FAIL')
            else:
                self.records.append(Record(record))
                print('OK')


def main():
    room = MeetingRoom()
    # room.add_record('APPOINT 1 12:30 30 2 andrey alex')
    # room.add_record('APPOINT 1 11:30 30 2 andrey alex')
    # room.add_record('APPOINT 1 11:45 30 2 andrey alex')
    # room.add_record('APPOINT 1 12:00 30 2 andrey alex')
    # room.add_record('APPOINT 1 12:15 30 2 andrey alex')
    # room.add_record('APPOINT 1 12:30 30 2 andrey alex')
    # room.add_record('APPOINT 1 12:45 30 2 andrey alex')
    # room.add_record('APPOINT 1 13:00 30 2 andrey alex')
    # room.add_record('APPOINT 1 13:15 30 2 andrey alex')

    room.add_record('APPOINT 1 12:30 30 2 andrey alex')
    room.add_record('APPOINT 1 12:00 30 2 alex sergey')
    room.add_record('APPOINT 1 12:59 60 2 alex andrey')
    room.add_record('PRINT 1 alex')
    room.add_record('PRINT 1 andrey')
    room.add_record('PRINT 1 sergey')
    room.add_record('PRINT 2 alex')


if __name__ == '__main__':
    main()
