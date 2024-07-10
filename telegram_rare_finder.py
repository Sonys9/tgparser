import requests, threading, random, os, time, re

fileid = str(random.randint(10000,99999))

def check(username):

    try:
        global issave, fileid

        os.system(f'title "Сохранено в telegramparser/results{fileid}.txt"')

        r = requests.get(f'https://t.me/{username}', timeout=5)

        if not f'''<div class="tgme_page_extra">
        @{username}
        </div>''' in r.text:

            r = requests.get(f'https://fragment.com/?query={username}', timeout=5)

            if f'''Unavailable''' in r.text.replace(' ', '').replace('\t', '').replace('\n', '') or '''Auctionsnotfound''' in r.text.replace(' ', '').replace('\t', '').replace('\n', '') or r.text.replace(' ', '').replace('\t', '').replace('\n', '') == '':

                print(f'Найден ник - {username}')

                if issave == '1': 
                    if not os.path.exists('telegramparser'): os.system('md telegramparser')
                    with open(f'telegramparser\\results{fileid}.txt', 'a') as f: f.write(f'\n@{username}')

    except:...
    #print(username)

def parse():

    while True:

        resp = input('\n[1] Использовать свою базу слов\n[2] Использовать общественную базу слов (30000 слов)\n\nВведите цифру:       ')

        if resp == '1':

            while True:

                wordsdir = input('\nВведите путь к файлу со словами:        ')

                if os.path.exists(wordsdir): 
                    with open(wordsdir, 'r') as f: return f.read().split('\n')
                else: print('\nПопробуй ещё раз!')

        elif resp == '2': 

            r = requests.get('https://kreekly.com/lists/30000-samyh-populyarnyh-angliyskih-slov/')

            words = re.findall("<span class='eng '>(.*?)</span>", r.text, re.DOTALL)

            wordss = []

            for word in words:

                for letter in word:

                    if letter not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM': word = word.replace(letter, '')
                
                wordss.append(word)

            return wordss

        else: print('\nПопробуй ещё раз!')

while True:

    method = input('\n[1] Рандомные символы\n[2] Ники с файла\n[3] 2 рандомных слова вместе\n[4] Рандомное слово\n[5] Рандомное слово + ваше слово\n[6] Слово + цифры\n\nВведите метод парсинга:      ')

    if method in ['1','2','3','4','5','6']:

        break

    else:

        print('\nПопробуй ещё раз!')
        
while True:

    if method == '1':

        lenght = input('\nКакая длина ников? (5-10):      ')

        try: lenght = int(lenght)
        except: 
            print('\nПопробуй ещё раз!')
            continue

        if lenght > 4 and lenght < 11:

            break

        else:

            print('\nПопробуй ещё раз!')

    elif method == '2':

        directory = input('\nВведите директорию с файлом:       ')

        if os.path.exists(directory): break

        else:

            print('\nПопробуй ещё раз!')

    elif method == '3':

        response = input('\n[1] Ставить _ между словами\n[2] Не ставить _ между словами\n[3] Всё сразу\n\nВведите цифру:       ')

        if response in ['1', '2', '3']:break

        else:

            print('\nПопробуй ещё раз!')

    elif method == '4': break

    elif method == '5':

        response = input('\n[1] Писать рандомное слово перед вашим\n[2] Писать рандомное слово после вашего\n[3] Проверять оба способа\n\nВведите цифру:       ')

        if response in ['1', '2', '3']:
            while True:
                userwords = input('\nВведите ваше слово (можно несколько через запятую (слово, слово, слово)):     ').replace(' ', '').split(',')

                if len(userwords) == 1:
                    if len(userwords[0]) > 16 or len(userwords[0]) < 2: print('\nПопробуй ещё раз! (слово большое / слово маленькое)')
                    else: break
                else:
                    good = True
                    for word in userwords:
                        if len(word) > 16 or len(word) < 2: 
                            print('\nПопробуй ещё раз! (одно из слов большое / одно из слов маленькое)')
                            good = False
                    if good: break
                        

            while True:
                    response2 = input('\n[1] Ставить _ между словами\n[2] Не ставить _ между словами\n[3] Всё сразу\n\nВведите цифру:       ')

                    if response2 in ['1', '2', '3']:break

                    else:

                        print('\nПопробуй ещё раз!')

            break

        else:

            print('\nПопробуй ещё раз!')

    elif method == '6':

        while True:

            userwords = input('\nВведите ваше слово (можно несколько через запятую (слово, слово, слово)):     ').replace(' ', '').split(',')

            if len(userwords) == 1:
                if len(userwords[0]) > 16 or len(userwords[0]) < 2: print('\nПопробуй ещё раз! (слово большое / слово маленькое)')
                else:break
            else:
                good = True
                for word in userwords:
                    if len(word) > 16 or len(word) < 2: 
                        print('\nПопробуй ещё раз! (одно из слов большое / одно из слов маленькое)')
                        good = False
                if good: break

        while True:
            numlenght = input('\nВведите кол-во цифр:       ')
            try: 
                int(numlenght)
                break
            except: print('\nПопробуй ещё раз!')

        break # 1 2 6

while True:

    if method not in ['1','2','6']:

        usermaxlenght = input('\nВведите максимальную длину ника:       ')

        try: 
            usermaxlenght = int(usermaxlenght)
            break
        except: print('\nПопробуй ещё раз!')
    
    else:break

while True:

    issave = input('\n[1] Сохранять ники в файл\n[2] Не сохранять ники в файл\n\nВведите цифру:      ')

    if issave in ['1','2']:
        
        break

    else:

        print('\nПопробуй ещё раз!')

while True:

    cd = input('\nВведите кд между чеками (в секундах):      ')

    try: cd = float(cd)
    except: 
        print('\nПопробуй ещё раз!')
        continue

    break

if method == '1':

    print('\nУспешно! Запуск...')

    nicks = []

    while True:

        username = ''.join(random.choices('qwertyuiopasdfghjklzxcvbnm1234567890_', k=5))

        if username[0] in '1234567890_' or username[-1] == '_' or '__' in username: continue

        if username not in nicks:

            time.sleep(cd)

            threading.Thread(target=check, args=(username,)).start()

            nicks.append(username)

elif method == '2':

    with open(directory, 'r') as f: nicks = f.read().split('\n')

    while True:
        if nicks[-1] == '': nicks.pop(-1)
        elif len(str(nicks[-1])) < 5 or len(str(nicks[-1])) > 32: nicks.pop(-1)
        else: break

    while True:
        if nicks[0] == '': nicks.pop(0)
        elif len(str(nicks[0])) < 5 or len(str(nicks[0])) > 32: nicks.pop(-1)
        else: break

    threads = []

    print('\nУспешно! Запуск...')

    for username in nicks: 

        time.sleep(cd)
        
        thr = threading.Thread(target=check, args=(username,))
        thr.start()
        threads.append(thr)

    for thread in threads: thread.join()

elif method == '3':

    words = parse()

    print('\nУспешно! Запуск...')

    usernames = []

    while True:

        if response == '3':
                
            for i in range(50):
                username = f'{random.choice(words)}_{random.choice(words)}'
                if len(username) <= usermaxlenght:
                        
                    if username not in usernames:

                        time.sleep(cd)
                        
                        threading.Thread(target=check, args=(username,)).start()

                        usernames.append(username)
                        break
            
            for i in range(50):
                username = f'{random.choice(words)}{random.choice(words)}'
                if len(username) <= usermaxlenght:
                        
                    if username not in usernames:

                        time.sleep(cd)
                        
                        threading.Thread(target=check, args=(username,)).start()

                        usernames.append(username)
                        break

            else:

                for i in range(50):
                    username = f'{random.choice(words)}{"" if response == "2" else "_"}{random.choice(words)}'
                    if len(username) <= usermaxlenght:

                        time.sleep(cd)
                        
                        threading.Thread(target=check, args=(username,)).start()

                        usernames.append(username)
                        break

elif method == '4':

    words = parse()

    print('\nУспешно! Запуск...')

    usernames = []

    while True:

        for i in range(50):
            username = random.choice(words)
            if len(username) <= usermaxlenght:

                if username not in usernames:

                    time.sleep(cd)
                    
                    threading.Thread(target=check, args=(username,)).start()

                    usernames.append(username)
                    break

elif method == '5':

    words = parse()

    print('\nУспешно! Запуск...')

    usernames = []

    while True:

        for userword in userwords:

            if response == '1' or response == '3':

                if response2 == '3': 

                    for i in range(50):

                        username = f'{userword}_{random.choice(words)}'
                        if len(username) <= usermaxlenght:

                            if username not in usernames:

                                time.sleep(cd)
                                
                                threading.Thread(target=check, args=(username,)).start()

                                usernames.append(username)  
                                break
                    
                    for i in range(50):
                    
                        username = f'{userword}{random.choice(words)}'
                        if len(username) <= usermaxlenght:

                            if username not in usernames:

                                time.sleep(cd)
                                
                                threading.Thread(target=check, args=(username,)).start()

                                usernames.append(username)  
                                break

                else:
                    
                    for i in range(50):
                        username = f'{userword}{"_" if response2 == "1" else ""}{random.choice(words)}'
                        if len(username) <= usermaxlenght:

                            if username not in usernames:

                                time.sleep(cd)
                                
                                threading.Thread(target=check, args=(username,)).start()

                                usernames.append(username)  
                                break

            if response == '2' or response == '3':

                if response2 == '3': 

                    for i in range(50):
                        username = f'{random.choice(words)}_{userword}'
                        if len(username) <= usermaxlenght:

                            if username not in usernames:

                                time.sleep(cd)
                                
                                threading.Thread(target=check, args=(username,)).start()

                                usernames.append(username)  
                                break
                    
                    for i in range(50):
                        username = f'{random.choice(words)}_{userword}'
                        if len(username) <= usermaxlenght:

                            if username not in usernames:

                                time.sleep(cd)
                                
                                threading.Thread(target=check, args=(username,)).start()

                                usernames.append(username)  
                                break

                else:
                    for i in range(50):
                        username = f'{random.choice(words)}{"_" if response2 == "1" else ""}{userword}'

                        if len(username) <= usermaxlenght:

                            if username not in usernames:

                                time.sleep(cd)
                                
                                threading.Thread(target=check, args=(username,)).start()

                                usernames.append(username)  
                                break

elif method == '6': 

    print('\nУспешно! Запуск...')

    numlenght = int(numlenght)

    for word in userwords:

        for i in range(int('9'*numlenght)):

            username = f'{i}'
            if len(username) != numlenght:
                for k in range(numlenght-len(username)):
                    username = f'0{username}'
            username = f'{word}{username}'

            time.sleep(cd)
                                
            threading.Thread(target=check, args=(username,)).start()

input('Сканирование закончено. Для закрытия нажмите ENTER.')