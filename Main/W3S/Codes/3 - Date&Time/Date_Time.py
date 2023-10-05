import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now()
current_time_formated = current_time.strftime("%H:%M")

print(
    f"A data de hoje é: {current_date} \nE o horario é: {current_time_formated}")
