import requests
import time

ano = 2010

for i in range(1,5):
    
    if i == 1: 
        print('-'*50)
        time.sleep(2)
        params = {
            'limit': 50,
            'offset': 0
        }
        
        res = requests.get(f'https://api.enem.dev/v1/exams/{ano}/questions', params=params)
        questoes = res.json()['questions']
        for questao in questoes:
            print(f'{questao['title']}   -   {questao['discipline']}')
            print('')
            
        print('')
        print('puxa 50        - total de questões: 50')
    elif i == 2: 
        print('-'*50)
        time.sleep(2)
        params = {
            'limit': 50,
            'offset': 50
        }
        
        res = requests.get(f'https://api.enem.dev/v1/exams/{ano}/questions', params=params)
        questoes = res.json()['questions']
        for questao in questoes:
            print(f'{questao['title']}   -   {questao['discipline']}')
            print('')
        print('')
        print('puxa mais 50   - total de questões: 100')
    elif i == 3: 
        print('-'*50)
        time.sleep(2)
        params = {
            'limit': 50,
            'offset': 100
        }
        
        res = requests.get(f'https://api.enem.dev/v1/exams/{ano}/questions', params=params)
        questoes = res.json()['questions']
        for questao in questoes:
            print(f'{questao['title']}   -   {questao['discipline']}')
            print('')
        print('')
        print('puxa mais 50   - total de questões: 150')
    elif i == 4: 
        print('-'*50)
        time.sleep(2)
        params = {
            'limit': 30,
            'offset': 150
        }
        
        res = requests.get(f'https://api.enem.dev/v1/exams/{ano}/questions', params=params)
        questoes = res.json()['questions']
        for questao in questoes:
            print(f'{questao['title']}   -   {questao['discipline']}')
            print('')
        print('')
        print('puxa mais 30   - total de questões: 180')
        print('-'*50)



    