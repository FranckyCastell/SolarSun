import time
import sys
import numpy as np


class bcolors:  # TEXT COLORS
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def slowprint(s):  # SLOW TEXT
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)


slowprint(f""" {bcolors.OKGREEN}
______  __                              ________       ______                
___  / / /______ ______________ _       __  ___/______ ___  /______ _________
__  /_/ / _  __ \__  ___/_  __ `/       _____ \ _  __ \__  / _  __ `/__  ___/
_  __  /  / /_/ /_  /    / /_/ /        ____/ / / /_/ /_  /  / /_/ / _  /    
/_/ /_/   \____/ /_/     \__,_/         /____/  \____/ /_/   \__,_/  /_/     
                                                                             
""")


#latitud = 41.4026
latitud_str = input(
    f'{bcolors.ENDC}{bcolors.BOLD}INSERTE LATITUD: {bcolors.ENDC}{bcolors.WARNING}')
latitud = float(latitud_str)

#data = 111
data_str = input(f'{bcolors.ENDC}{bcolors.BOLD}INSERTE DATA TOTAL DEL AÑO: {bcolors.ENDC}{bcolors.WARNING}')
print('')
print('-------------------------------')
print('')
data = float(data_str)

declinacion = 23.45*(np.sin(np.radians((360/365)*(data+284))))
print(f'{bcolors.ENDC}{bcolors.BOLD}DECLINACION DE LA TIERRA: {bcolors.ENDC}{bcolors.WARNING}{declinacion}º{bcolors.ENDC}')  # DECLINACION

angleHorari = np.degrees(
    np.arccos(-np.tan(np.radians(latitud))*np.tan(np.radians(declinacion))))

print(f'{bcolors.BOLD}ANGULO HORARIO DE LA TIERRA: {bcolors.ENDC}{bcolors.WARNING}{angleHorari}º{bcolors.ENDC}')  # ANGULO
print('')

horas = (angleHorari/15)

horasTotales = time.strftime("%H:%M:%S", time.gmtime(((horas*2)*60)*60))
# HORAS TOTALES
print(f'{bcolors.BOLD}EL DIA SOLAR DURA: {bcolors.ENDC}{bcolors.OKGREEN}{horasTotales} horas{bcolors.ENDC}')
print('')

# SOLAR

horaSurtSolar = time.strftime("%H:%M:%S", time.gmtime(((12-horas)*60)*60))
print(f'{bcolors.BOLD}HORA SORTIDA SOL SOLAR : {bcolors.ENDC}{bcolors.OKGREEN}{horaSurtSolar} horas{bcolors.ENDC}')

horaVaSolar = time.strftime("%H:%M:%S", time.gmtime(((12+horas)*60)*60))
print(f'{bcolors.BOLD}HORA SORTIDA SOL SOLAR : {bcolors.ENDC}{bcolors.OKGREEN}{horaVaSolar} horas{bcolors.ENDC}')
print('')
