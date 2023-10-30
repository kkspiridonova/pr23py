import csv
name = 'gagag'

backpack = ["телефон", "бутылка воды"]

while (True):
    print("Напишите слово \"Играть\", чтобы начать. \n Напищите \"Концовки\", чтобы посмотреть концовки.")
   
    begining = str(input())
    if begining.startswith("Концовки") == True:
        with open('save.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    elif begining.startswith("Играть") == True:

        print ('Новелла "Под корнями"')
        input()
        print("Как вас зовут?")
        name = (input())

        import json
        data = { "name": name,
                "ruykzak": backpack,
                "endings": 0}
        with open ('output.json', 'w') as file:
            json.dump(data, file)

        def option_one(opt):
            print("1. Пойдете прогуляться перед работой")
            print("2. Попытаетесь заснуть")
            opt = int(input())
            return opt
        def option_two(opt):
            print("1. Рассказать, о том что вы нашли его.")
            print("2. Не рассказывать, о том что вы нашли его.")
            opt = int(input())
            return opt
        def option_three(opt):
            print("1.Продолжать искать")
            print("2.БЕЖАТЬ")
            opt = int(input())
            return opt
        def Rukzak(item):
            backpack.append(item)
            backpack1 = backpack
            return backpack1
        def personagi(name):
            сharacters = {
                    "Кэролайн Паффи":"- офицер полиции, ведет дело о мертвом ребенке.",
                    "Алекс" : "- лучший друг главного героя, внимательно следит за вашим состоянием.",
                    "Томми": "- младший брат главного героя, который чуть не умер из-за спора."
                }
            name1 = сharacters[name]
            return name1
        def suzet(number):
            suzets = " "
            endings = ["Правильное направление.", "Обычный день.", "Ложь во благо.", "3 метра под землей." ]
            opt = number
            if opt == 1:
                suzets = endings[0]
            elif opt == 2:
                suzets = endings[1]
            elif opt == 3:
                suzets = endings[2]
            elif opt == 4:
                suzets = endings[3]
            return(suzets)
        print ('У вас бессонница. Время 5 утра. Чем займетесь?')
        opt = option_one(input())
        while (True):
            match opt:
                    case 1: 
                        
                        print ('Прекрасный выбор. Вы решили пойти прогуляться.')
                        input()
                        print ('Вы посмотрели в окно. На улице стояла пасмурная холодная погода.')
                        input()
                        print ("Теперь нужно собрать рюкзак. Пока там лежит только телефон и бутылка воды.")
                        pack = Rukzak(input())
                        print ("Рюкзак:")
                        for item in pack:
                            print(item)
                        print ("Пора выходить.")
                        input()
                        print("Вы пришли на пляж.")
                        print("Волны шумно бились об камни, навевая тоску на ваш сонный разум.")
                        input()
                        print("Время пролетело незаметно, вам пора было идти на работу.") 
                        input()
                        print("Внезапно, что-то привлекло ваше внимание.")
                        input()
                        print("Точнее кто-то. \nНа берегу кто-то лежит")
                        input()   
                        print("Вы подходите к человеку на берегу.\nЭто мальчик лет 14, с вьющимися золотыми волосами.\nОн лежит неподвижно, уствавившись в небо")
                        input()
                        print("Его лицо кажется вам знакомым.")
                        input()
                        print("Вы подходите ближе, наклоняясь над мальчиком. \nМальчик не дышит")
                        input()
                        print("Вы дрожащими руками хватаете телефон и набираете 112.\nВидимо вы опоздаете на работу.")
                        input ()
                        print("Через полчаса приезжает полиция. Вас подходит допросить офицер Кэролайн.")
                        input()
                        print("Кэролайн: Здравствуйте.\n Меня зовут Кэролайн Паффи,\n можно просто офицер офицер Кэролайн.\nКак вас зовут?")
                        input()
                        print(name)
                        input()
                        print("Кэролайн: Приятно познакомиться. Вы знали этого мальчика? ")
                        input()
                        print ("Нет.")
                        input()
                        print ("Кэролайн: Хорошо, оставьте пожалуйста свой номер телефона, \nмне нужно будет задать вам еще пару вопросов.")
                        data = { "name": name,
                                "ruykzak": backpack,
                                "endings": 1}
                        with open ('output.json', 'w') as file:
                            json.dump(data, file)
                    case 2:
                        with open('save.csv', 'a+') as file:
                            filewriter = csv.writer(file)
                            filewriter.writerow([name, 'Обычный день'])
                        input()
                        print("Это приключенческая новела, зачем вы выбрали сон? \nПоздравляю с прохождением на Нормальную концовку\"Обычный день\".")
                        data = { "name": name,
                                "ruykzak": backpack,
                                "endings": 2}
                        with open ('output.json', 'w') as file:
                            json.dump(data, file)
                        exit()
            break



        input()
        print("Вы отправлеятесь на работу. \nУтреннее происшествие не дает вам покоя, но деньги важнее.")
        input()
        print("Рабочий день прошел как в тумане. \nУже 18:00 и вы собираетесь домой. Внезапно кто-то вас окликнул.")
        input()
        print("Это ваш друг Алекс. Он хочет с вами поговорить.")
        input()
        print(f"Алекс: Привет,{name}, давно не виделись. Как у тебя дела?")
        input()
        print("Привет, Алекс. Все хорошо. Сам как?")
        input()
        print("Алекс: Все просто прекрасно. Я переезжаю через неделю, решил навестить старых друзей")
        input()
        print("Рад слышать, что у тебя все наладилось.")
        input()
        print("Алекс: Да, спасибо. Как тебе идея сходить вечером выпить? Как в старые добрые.")
        input()
        print("Я не против.")
        input()
        print("Алекс: Отлично! Кстати, слышал о мальчике, чье тело нашли на берегу?")
        input()
        opt = option_two(input())
        while (True):
            match opt:
                case 1: 
                    input()
                    print("Я нашел этого мальчика. \nОфицер пообещала мне позвонить насчет него.")
                    input()
                    print("Алекс: О боже, ты в порядке? Наверное это ужасный стресс.")
                    input()
                    print("Я в порядке. Просто немного в шоке.")
                    input()
                    print("Алекс: Это естественно. Может нам стоит перенести встречу. \nТебе следует отдохнуть")
                    input()
                    print("Нет-нет, все в порядке. Я посплю перед нашей встречей.")
                    input()
                    print("Ну, если ты уверен. Тогда до встречи.")
                    input()
                    print("До встречи.")
                    data = { "name": name,
                                "ruykzak": backpack,
                                "endings": 11}
                    with open ('output.json', 'w') as file:
                            json.dump(data, file)
                case 2:
                    with open('save.csv', 'a+') as file:
                            filewriter = csv.writer(file)
                            filewriter.writerow([name, 'Не стоит врать друзьям'])
                    input()
                    print("Да, слышал. Это ужасно")
                    input()
                    print("Алекс: Разве не ты нашел его?")
                    input()
                    print("Нет, о чем ты говоришь?")
                    input()
                    print("Алекс: Кэролайн сказала, что ты вызвал полицию.")
                    input()
                    print("....")
                    input()
                    print("Алекс: Ладно... Тогда я пойду.")
                    input()
                    print("Пока") 
                    input()
                    print("Вы идете домой. \nВас не отпускает ощущение, что за вами кто-то наблюдает.")
                    input()
                    print("Следующие несколько дней, вам снятся исключительно кошмары. \nВы морально истощены. \nВам кажется, что кто-то зовет вас в лес.") 
                    input()
                    print("Вас навещает Алекс. \nВы не отвечали на его звонки, он забеспокоился. \nОн видит ваше состояние и решает отправить вас в психушку.")
                    input()
                    print("Поздравляю с прохождением играы на плохую концовку:\"Ложь во благо.\"\nНе стоит врать друзьям.")
                    data = { "name": name,
                                "ruykzak": backpack,
                                "endings": 12}
                    with open ('output.json', 'w') as file:
                            json.dump(data, file)
                    exit()
            break
        input()
        print("Вы отправляетесь домой и ложитесь спать.")
        input()
        print("Вы оказались на берегу, где нашли мальчика.\n Он сидит на том же месте. Он жив.")
        input()
        print(f"???: Привет, {name}, рад тебя видеть!")
        input()
        print("Привет. Я сплю?")
        input()
        print("???:Не совсем. Но это неважно. Мне необходима твоя помощь. \nТы же помнишь как меня зовут?")
        input()
        print("...Мы знакомы?")
        input()
        print("???:...Ты не помнишь меня? Я Томми!")
        input()
        print("Это имя Вам знакомо. Но вы не можеет вспомнить точно.")
        input()
        print("Не думаю, что помню тебя. Ты просто кошмар после долго дня.")
        input()
        print("Томми: Нет! Пострайся вспомнить!\n Я твой младший брат, неделю назад я пошел в лес, а теперь я здесь!")
        input()
        print("Вы начинаете вспоминать. Легенду о лесе. Спор. ")
        input()
        print("Ты пошел в лес и не вернулся... \nИ никто не помнит о тебе сейчас...\nКак мне тебя найти?")
        input()
        print("Томми: Я все еще в лесу, у старого дуба. Держи, это поможет тебе найти меня")
        print ("Рюкзак:")
        pack = Rukzak("компас")
        for item in pack:
            print(item)
        input()
        input()
        print("Вы просыпаетесь в холодном поту. Все, что вы помните - вам нужно попасть в лес.")
        input()
        print("Наверное стоит собрать рюкзак.")
        pack = Rukzak(input())
        print ("Рюкзак:")
        for item in pack:
            print(item)
        input()
        print("Вы уверены, что хотите пойти туда?")
        print("1. Да")
        print("2. Да")
        input()
        print("Вы отправляетесь в лес. \nВсю дорогу вам кажется, что за вами наблюдают.\n При приблежении к лесу ощущение усиливается")
        input()
        print("Войдя в лес, вы встречаетесь с мертвой тишиной. \nЛес что-то шепчет вам. Вы игнорируете и идете дальше.")
        input()
        print("Вы идете дальше, к старому дубу. Тьма сгущается.")
        input()
        print("Вы доходите до дуба. Но там никого нет.\nОднако вы слышите чье-то дыхание. Земля под вашими ногами дышит")
        input()
        print("Вы пытаетесь осмотреться, но шепот леса становится невыносим.")
        opt = option_three(input())
        while (True):
            match opt:
                    case 1:
                        with open('save.csv', 'a+') as file:
                            filewriter = csv.writer(file)
                            filewriter.writerow([name, 'Правильное направление'])
                        print("Вы решаете достать компас. Он должен помочь вам.")
                        input()
                        print("Но он вам не помогает. Стрелка стоит на месте.")
                        input()
                        print("Вы опускаете взгляд вниз. Из земли торчит рука.\nВ руке вы видите такой же компас, как у вас.")
                        input()
                        print("Вы понимаете, что Томми под землей.\n Руками вы разгребате землю и вытаскиваете мальчика.")
                        input()
                        print("Томми откашливает землю и траву. С ним все в порядке")
                        input()
                        print(f"Томми: {name}, нам надо убираться отсюда!")
                        input()
                        print("Вы выбегаете из леса и покидаете этот город.")
                        input()
                        print("Поздравляю с прохождением игры на хорошую концовку:\n\"Правильное направление.\"")
                        data = { "name": name,
                                "ruykzak": backpack,
                                "endings": 111}
                        with open ('output.json', 'w') as file:
                            json.dump(data, file)
                        input()
                    case 2: 
                        with open('save.csv', 'a+') as file:
                            filewriter = csv.writer(file)
                            filewriter.writerow([name, '3 метра под землей'])
                        print("Вы бежите, перепрыгивая корни и игнорируя шепот в ушах.\n Но лес не хочет вас отпускать")
                        input()    
                        print("Корни обхватывают ваши ноги, земля засасывает ботинки. \nМне кажется, вы не выберитесь.")
                        input()    
                        print("Поздравляю с прохождением игры на плохую концовку:\"3 метра под землей\"")
                        input()
                        data = { "name": name,
                                "ruykzak": backpack,
                                "endings": 112}
                        with open ('output.json', 'w') as file:
                            json.dump(data, file)  
                        exit()  
            break 
        while(True): 
            print("Чтобы посмотреть описание персонажей, нажмите C, \nчтобы посмотреть концовки, нажмите E.") 
            gg =str(input())
            if gg == "C":
                    print("Введите имя персонажа.")
                    geroi = personagi(input())
                    print(geroi)
            elif gg == "E":
                print("Введите номер концовки.")
                number = suzet(int(input()))
                print(number)
            else: break
        break        