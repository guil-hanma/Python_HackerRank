import calendar
import sys

print("Esse programa irá pegar o ano e mês inseridos e gerar o calendario do mesmo.")
year = int(input("Digite um ano: "))


while True:
    month = int(input("Digite um mês: "))
    if month in range(1, 13):
        break
    else:
        print("Insira um valor válido!")


print(f"Esse é o calendario de {year}/{month}")
print(calendar.month(theyear=year, themonth=month))
