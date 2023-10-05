import pandas as pd
import datetime

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# .date pega a ordem (year, month, day)

exam_st_date = (2014, 12, 11)
date = datetime.date(*exam_st_date)
formatted_date = date.strftime("%d/%m/%Y")
print(f"Sua data de exame é: {formatted_date}")


# Forma simplificada extraindo os dados da tupla

exam_st_date = (11, 12, 2014)
day, month, year = exam_st_date

print(f"Sua data de exame é: {day}/{month}/{year}")
