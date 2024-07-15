import calendar
import locale

locale.setlocale(locale.LC_ALL, 'es_es')


def obtener_fila_dias(anio, mes, semana, sangria):
    primer_dia_semana, ultimo_dia_mes = calendar.monthrange(anio, mes)
    fin = ultimo_dia_mes + primer_dia_semana
    salida = cadena_sangria(sangria)

    for i in range(7*semana, 7*(semana + 1)):
        if i in range(primer_dia_semana, fin):
            salida += f'<td>{i - primer_dia_semana + 1}</td>'
        else:
            salida += '<td></td>'

    return salida + salto_de_linea()


def obtener_bloque_dias(anio, mes_inicial, columnas, sangria):
    cadena = ''
    for i in range(6):
        cadena += cadena_sangria(sangria) + '<tr>' + salto_de_linea()

        for j in range(columnas):
            cadena += obtener_fila_dias(anio, mes_inicial + j, i, sangria + 1)

        cadena += cadena_sangria(sangria) + '</tr>' + salto_de_linea()

    return cadena


def filas_nombre_dias(columnas, sangria):
    cadena = cadena_sangria(sangria) + '<tr>' + salto_de_linea()

    for i in range(columnas):
        cadena += cadena_sangria(sangria + 1) + \
            '<th>Lu</th><th>Ma</th><th>Mi</th><th>Ju</th><th>Vi</th><th>Sa</th><th>Do</th>' + salto_de_linea()

    cadena += cadena_sangria(sangria) + '</tr>' + salto_de_linea()
    return cadena


def cadena_sangria(tamanio):
    return tamanio * '    '


def salto_de_linea():
    return '\n'


def th_semestre(semestre, columnas, sangria):
    cadena = cadena_sangria(sangria) + \
        f'<th rowspan="{8 * 6 // columnas}">Semestre {semestre}</th>' + \
        salto_de_linea()

    return cadena


def th_trimestre(trimestre, columnas, sangria):
    cadena = cadena_sangria(sangria) + \
        f'<th rowspan="{8 * 3 // columnas}">Trimestre {trimestre}</th>' + \
        salto_de_linea()

    return cadena


def th_nombre_meses(mes_inicial, columnas, sangria):
    cadena = ''

    for i in range(mes_inicial, mes_inicial + columnas):
        cadena += cadena_sangria(sangria) + \
            f'<th colspan="7">{calendar.month_name[i]}</th>' + \
            salto_de_linea()

    return cadena


def calendario_trimestral(anio, sangria=1):
    cadena = cadena_sangria(sangria) + '<table border="1">' + salto_de_linea()
    columnas = 3

    cadena += cadena_sangria(sangria + 1) + \
        f'<caption>{anio}</caption>' + salto_de_linea()

    for i in range(0, 12, columnas):
        cadena += cadena_sangria(sangria + 1) + '<tr>' + salto_de_linea()

        if(i % 6 == 0):
            cadena += th_semestre(((i)//6)+1, columnas, sangria + 2)

        cadena += th_trimestre(((i)//3)+1, columnas, sangria + 2)
        cadena += th_nombre_meses(i+1, columnas, sangria + 2)

        cadena += cadena_sangria(sangria + 1) + '</tr>' + salto_de_linea()
        cadena += filas_nombre_dias(columnas, sangria + 1)
        cadena += obtener_bloque_dias(2024, i + 1, columnas, sangria + 1)

    cadena += cadena_sangria(sangria) + '</table>'
    return cadena


# cadena = ''
# columnas = 3
# for i in range(1, 12, columnas):
#     cadena += fila_nombre_dias(columnas)
#     cadena += obtener_filas_meses(i, columnas)

# print(cadena)

print(calendario_trimestral(2024))
