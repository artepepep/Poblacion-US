from poblacion import *
import time

if __name__ == '__main__':
    print(calcula_paises(lee_poblacion('/Users/mac/us-Lab/Poblacion-US/data/population.csv')))
    print(filtra_por_pais(lee_poblacion(ruta), 'Zimbabwe'))
    print(filtra_por_paises_y_anyo(lee_poblacion(ruta), 1960, ('Zimbabwe', 'Yemen')))
    muestra_evolucion_poblacion(lee_poblacion(ruta), 'CEB')
    print('wait 5 seconds...')
    time.sleep(5)
    muestra_comparativa_paises_anyo(lee_poblacion(ruta), 2015, ('Afghanistan', 'Argentina'))