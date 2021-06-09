from datetime import datetime as dt
import schedule

text = input('Введите сообщение которое будет выводиться: ')
sleep = input(f"Введите в формате '00-07' промежуток времени, ",
              f"в который кукушка будет молчать: ")

down = sleep.split('-')[0]
up = sleep.split('-')[1]

if dt.now().minute != 0:
    count = 24 - dt.now().hour - 1
else:
    count = 24 - dt.now().hour


def clock():
    global count, text
    count -= 1
    if count == 0:
        return schedule.CancelJob
    else:
        print(text)

schedule.every().hour.at(':00').do(clock)

if dt.now().hour >= int(down) and dt.now().hour <= int(up):
    pass
else:
    while True:
        schedule.run_pending()
