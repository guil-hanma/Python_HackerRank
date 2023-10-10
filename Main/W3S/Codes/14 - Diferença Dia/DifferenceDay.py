# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)


import datetime

print("Esse programa irá calcular a diferença de dias entre a data inicial e data final")

dtinicial = input("Insira a data inicial (AAAA/MM/DD): ")
dtfinal = input("Insira a data final (AAAA/MM/DD): ")


def formatar_data(data_str):
    partes = data_str.split('/')
    if len(partes) == 3:
        ano, mes, dia = map(int, partes)

        if len(str(mes)) == 1:
            mes = f"0{mes}"

        return f"{ano}, {mes}, {dia}"
    else:
        return None


dtinicial_formatada = formatar_data(dtinicial)
dtfinal_formatada = formatar_data(dtfinal)

if dtinicial_formatada and dtfinal_formatada:
    mes = None
    try:
        data_inicial = datetime.datetime.strptime(
            dtinicial_formatada, "%Y,%m,%d")
        data_final = datetime.datetime.strptime(dtfinal_formatada, "%Y,%m,%d")

        diferenca = data_inicial - data_final
        print(f"A diferença entre as datas é: {diferenca.days} dias")
    except ValueError:
        print("Formato inválido de data, verifique se está usando AAAA/MM/DD")
else:
    print("Formato inválido de data, verifique se está usando AAAA/MM/DD")
