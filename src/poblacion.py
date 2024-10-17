from collections import namedtuple
import csv
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', ['pais', 'codigo', 'año', 'censo'])
ruta = '/Users/mac/us-Lab/Poblacion-US/data/population.csv'

lista_anyos = [anyo for anyo in range(1960, 2017)]


def lee_poblacion(ruta_fichero: str) -> list[RegistroPoblacion]:
    reg_poblacion_list = []
    with open(ruta_fichero, 'r', newline='' ,encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            reg_poblacion_list.append(RegistroPoblacion(pais=str(row[0]),
                                                        codigo=str(row[1]),
                                                        año=int(row[2]),
                                                        censo=int(row[3])),
                                                        )
    return reg_poblacion_list


def calcula_paises(poblaciones: list[RegistroPoblacion]) -> set[str]:
    paises = set()

    for poblacion in poblaciones:
        paises.add(poblacion.pais)
    
    return paises
# print(calcula_paises(lee_poblacion('/Users/mac/us-Lab/Poblacion-US/data/population.csv')))


def filtra_por_pais(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str) -> list[RegistroPoblacion]:
    pais_datos = []

    for poblacion in poblaciones:
        if poblacion.pais == nombre_o_codigo or poblacion.codigo == nombre_o_codigo:
            pais_datos.append((poblacion.pais, poblacion.censo))
    
    return pais_datos
# print(filtra_por_pais(lee_poblacion(ruta), 'Zimbabwe'))


def filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str]) -> list[tuple]:
    pais_anyo_datos = []

    for poblacion in poblaciones:
        if poblacion.año == anyo and poblacion.pais in paises:
            pais_anyo_datos.append((poblacion.pais, poblacion.censo))
    
    return pais_anyo_datos
# print(filtra_por_paises_y_anyo(lee_poblacion(ruta), 1960, ('Zimbabwe', 'Yemen')))


def muestra_evolucion_poblacion(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str) -> None:
    titulo = f'Grafic of {nombre_o_codigo}'
    censos = [filtra_por_pais(poblaciones, nombre_o_codigo)[x][1] for x in range(0, len(filtra_por_pais(poblaciones, nombre_o_codigo)))]

    plt.title(titulo)
    plt.plot(lista_anyos, censos)
    plt.show()
# muestra_evolucion_poblacion(lee_poblacion(ruta), 'CEB')


def muestra_comparativa_paises_anyo(poblaciones, anyo, paises) -> None:
    titulo = 'Grafic'
    paises_censos = filtra_por_paises_y_anyo(poblaciones, anyo, paises)

    paises, censos = zip(*paises_censos)

    plt.title(titulo)
    plt.bar(paises, censos)
    plt.show()
muestra_comparativa_paises_anyo(lee_poblacion(ruta), 2015, ('Afghanistan', 'Argentina'))