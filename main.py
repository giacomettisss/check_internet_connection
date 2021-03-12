import requests
from datetime import datetime
import time


def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        info = 'Com internet'
        data_e_hora_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return [True, info, data_e_hora_atual]
    except requests.ConnectionError:
        info = 'Sem internet'
        data_e_hora_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return [False, info, data_e_hora_atual]
    except requests.exceptions.Timeout:
        return None
       

dados = []

counter = 0

def add_to_file(params_1, params_2, params_3):
    global counter
    
    db = open('db.txt', 'a+')
    if params_1 < params_2:
        db.write(str(params_3))
        db.write('\n')
        counter += 1
    db.close()

while True:
    # time.sleep(2)
    
    validation = check_internet()
    if validation is None:
        print("\nTIME OUT\n")
        continue

    elif len(dados) == 0:
        validation = check_internet()
        if validation[0]:
            print('Com internet às {}'.format(validation[2]))
            dados.append([validation[1], validation[2]])
        else:
            print('Sem internet às {}'.format(validation[2]))
            dados.append([validation[1], validation[2]])
        time.sleep(5)

    if validation[0]:
        print('Com internet às {}'.format(validation[2]))
        if dados[-1][0] != 'Com internet':
            dados.append([validation[1], validation[2]])
    else:
        print('Sem internet às {}'.format(validation[2]))
        if dados[-1][0] != 'Sem internet':
            dados.append([validation[1], validation[2]])

    # print(dados[-1])

    add_to_file(counter, len(dados), dados[-1])

