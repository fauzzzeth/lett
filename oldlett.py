#This is a very old version of Lett. Download LETT! from releases to get the newest.

#                                                            ┌▄─┐      ┌▄───────┐┌▄───────┐┌▄───────┐┌▄─┐
#                                                            │▓▓│      │·▓┌─────┘└──┐·▓┌──┘└──┐·▓┌──┘│▓▒│
#                                                            │▒.│      │▒▒└──┐      │▒▒│      │▒▒│   │·░│
#                                                            │░░│      ├░░┌──┘      │░░│      │░░│   └──┘
#                                                            │══└─────┐├══└─────┐   │══│      │══│   ┌▄─┐
#                                                            └────────┘└────────┘   └──┘      └──┘   └──┘
#                                                                                       -Made by Fauzzeth




rank = None
import random
import os
import time
import msvcrt
import art
import pybase64 #type: ignore
from pystyle import *
logo = "┌▄─┐      ┌▄───────┐┌▄───────┐┌▄───────┐┌▄─┐\n│▓▓│      │·▓┌─────┘└──┐·▓┌──┘└──┐·▓┌──┘│▓▒│\n│▒.│      │▒▒└──┐      │▒▒│      │▒▒│   │·░│\n│░░│      ├░░┌──┘      │░░│      │░░│   └──┘\n│══└─────┐├══└─────┐   │══│      │══│   ┌▄─┐\n└────────┘└────────┘   └──┘      └──┘   └──┘"
charlist = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#char = msvcrt.getch().decode()
def sprint(text):
    global delay
    global rank
    interval = 0.01
    for char in text:
        print(char, end='', flush=True)
        time.sleep(interval)
    print()
sprint("This is a very old version of Lett. Download LETT! from releases to get the newest.")
time.sleep(2)
def bullshit64enc(data):
    print("Encoding...")
    data = pybase64.b64encode(data.encode())
    print("_____________________\n", data, "\n_____________________")
    os.system("cls")
    return str(data)
def bullshit64dec(data):
    print("Decoding...")
    data = data.removeprefix("b'")
    data = data.removesuffix("'")
    data = str(pybase64.b64decode(data, validate=True))
    data = data.removeprefix("b'")
    data = data.removesuffix("'")
    data = data.replace("\\n", "\n")
    print("_____________________\n", data, "\n_____________________")
    os.system("cls")
    return str(data)


def game(times, timepr):
    os.system("cls")
    global countt
    global crating
    global rating
    total = times
    correct = 0
    if times == 1337:
        db.close()
        os.remove("Lett.db")
        return 0
    marv = 0
    perf = 0
    good = 0
    great = 0
    okay = 0
    miss = 0

    while times != 0:
        times -= 1


        chartopress = random.choice(charlist)

        print(art.text2art(chartopress))

        start_time = time.perf_counter_ns()
        charpressed = msvcrt.getch().decode()

        end_time = time.perf_counter_ns()
        time_taken = (end_time - start_time)/1_000_000_000

        os.system("cls")
        if time_taken < timepr and chartopress == charpressed:
            if time_taken <= timepr / 5:
                correct += 1.0
                print("MARVELOUS!")
                marv += 1

            elif time_taken <= timepr / 4:
                correct += 0.95
                print("Perfect!")
                perf += 1

            elif time_taken <= timepr / 3:
                correct += 0.90
                print("Great!")
                great += 1

            elif time_taken <= timepr / 2:
                correct += 0.85
                print("Good!")
                good += 1

            else:
                correct += 0.8
                print("Okay!")
                okay += 1
        elif time_taken > timepr:
            print("Miss!")
            miss += 1
        elif chartopress != charpressed:
            print("Miss!")
            miss += 1
    
    # Calculate accuracy as a percentage of correct characters
    if total > 0:
        accuracy = (correct / total) * 100
        passed = True
    else:
        accuracy = 0
    
    if accuracy < 50:
        passed = False

    if accuracy > 50:
        grade = "D"
        if accuracy > 70:
            grade = "C"
            if accuracy > 80:
                grade = "B"
                if accuracy > 90:
                    grade = "A"
                    if accuracy > 95:
                        grade = "S"
                        if accuracy > 97.5:
                            grade = "S+"
                            if accuracy > 99:
                                grade = "S++" 
                                if accuracy > 99.9:
                                    grade = "X"
    elif accuracy < 50:
        grade = "F"
    else: grade = "WTF"
    countt += 1
    #game fully made by fauzzeth
    difficulty = round((total/25) * ((2.6-timepr)*100) * 10)
    gamehistory.append(grating)
    acchis.append(round(accuracy, 2))
    if passed == True: grating = round(difficulty * (accuracy/100))
    else: grating = 0
    if countt < 10:
        sprint("Difficulty, rating, and accuracy will be available as soon as you complete 10 games!")
    else:
        sprint(f"Difficulty: {difficulty}")
        sprint(f"Game rating: {grating}")
        sprint(f"Player rating: {crating}")
        sprint(f"Accuracy: {accuracy:.2f}%")
        sprint("_____________________")
        sprint(f"Marvelous - {marv}")
        sprint(f"Perfect - {perf}")
        sprint(f"Great - {great}")
        sprint(f"Good - {good}")
        sprint(f"Okay - {okay}")
        sprint(f"Miss - {miss}")
    print("_____________________")
    print(f"Grade: {grade}")

def refreshPool(rating):
    if rating == 0:
        return 0
    elif rating >= 1 and rating < 500:
        return 1
    elif rating >= 500 and rating < 1000:
        return 2
    elif rating >= 1000 and rating < 2000:
        return 3
    elif rating >= 2000 and rating < 3000:
        return 4
    elif rating >= 3000 and rating < 3500:
        return 5
    elif rating >= 3500 and rating < 5000:
        return 6
    elif rating >= 5000 and rating < 6899:
        return 7
    elif rating >= 6900:
        return 8
    else:
        print("Error! Rank set to 0 temporarily.")
        return 0

def writesave():
    try:
        global db
        db.close()
        os.remove("Lett.db")
    except Exception as e:
        print('IGNORE')
        print(e)

    db = open("Lett.db", 'a')
    db.write(bullshit64enc(f"""name = "{name}"
gamehistory = {gamehistory}
countt = {countt}
acchis = {acchis}"""))

try:
    db = open("Lett.db", 'r')
    exec(bullshit64dec(db.read()))
    print("_____________________\n#Your information", name, gamehistory, countt, acchis, sep="\n#",)
    print("_____________________")
except Exception as e:
    print("IGNORE\n", e)
    print("_____________________")
    print("Hi! Choose your name.")
    name = input(">>")
    gamehistory = []
    countt = 0
    acchis = []
    writesave()
print("Your rating, rank, average accuracy, grade, etc. are based on the last 10 games.")
time.sleep(1)
os.system("cls")
showlogo = True
time.sleep(1)
os.system("cls")
while True: 
    try:
        while True:
            if len(gamehistory) > 10: gamehistory.remove(gamehistory[0])
            else: break
        count = len(gamehistory)
        rawrating = 0
        for item in gamehistory:
            rawrating += item
        crating = round(rawrating/count)
    except Exception as e:
        crating = 0
        sprint("Error! Failed to load game history, rating set to 0.")
    try:
        while True:
            if len(acchis) > 10: acchis.remove(acchis[0])
            else: break
        count = len(acchis)
        rawacc = 0
        for item in acchis:
            rawacc += item
        avgacc = rawacc/count
        if avgacc > 50:
            gradeavg = "D"
            if random.randint(1, 250) == 1: gradeavg = "D. Well, yk... Not too bad, but still, maybe Minecraft?"
            if avgacc > 70:
                gradeavg = "C"
                if random.randint(1, 250) == 1: gradeavg = "C. Not perfect, but... nevermind."
                if avgacc > 80:
                    gradeavg = "B"
                    if random.randint(1, 250) == 1: gradeavg = "B. Well, that's nice, i'd say."
                    if avgacc > 90:
                        gradeavg = "A"
                        if random.randint(1, 250) == 1: gradeavg = "A. Awesome. I bet you're pretty good at this game."
                        if avgacc > 95:
                            gradeavg = "S"
                            if random.randint(1, 250) == 1: gradeavg = "S. Holy. Might wanna... Try S+?"
                            if avgacc > 97.5:
                                gradeavg = "S+"
                                if random.randint(1, 250) == 1: gradeavg = "S+. Mhm. You're unstoppable, aren't you?"
                                if avgacc > 99:
                                    gradeavg = "S++" 
                                    if random.randint(1, 250) == 1: gradeavg = "S++. Seriously?++ You're either playing on 200 elo or a top player."
                                    if avgacc > 99.9:
                                        gradeavg = "X"
                                        if random.randint(1, 250) == 1: gradeavg = "X. Inhumane."
        elif avgacc < 50:
            gradeavg = "F"
            if random.randint(1, 25) == 1: gradeavg = "F. Maybe... Try Minecraft?"
            
        else:
            gradeavg = "WTF"
    except Exception as e:
        avgacc = 0
        gradeavg = "Unavailable"
        sprint("Error! Failed to load accuracy history, avgacc set to 0.")
    rank = refreshPool(crating)
    if showlogo:
        showlogo = False
        for line in logo.splitlines():
            sprint(Center.XCenter(line))
        time.sleep(0.3)
    if rank == 8:
       sprint("Write custom for customized pool difficulty.\n") 
    sprint("_____________________")
    Cursor.ShowCursor()
    time.sleep(0.2)
    if countt < 10:
        rank = 0
        sprint(f"Hello {name}!\nPlay 10 games to see your rating, accuracy, rank and grade!")
    else:
        sprint(f"Hello {name}!\nRank - {rank}/7, Rating - {crating}\nYour average grade: {gradeavg}.\nAverage accuracy: {avgacc:.2f}%.\nPlayed {countt} games.\nPress enter to start, type save to save.")



    cmd = input(">>")

    #POOL


    
    if cmd == "save":
        print("Saving...")
        writesave()
    else:
        if rank == 0: # ? Elo
            howmuch = 10, 40
            howmuchtime = 0.5, 2
        elif rank == 1: # 1-500
            howmuch = 5, 25
            howmuchtime = 1.25, 2.5
        elif rank == 2: # 500-1000
            howmuch = 10, 35
            howmuchtime = 0.85, 1.75
        elif rank == 3: # 1000-2000
            howmuch = 10, 45
            howmuchtime = 0.75, 1.15
        elif rank == 4: # 2000-3000
            howmuch = 10, 47
            howmuchtime = 0.6, 1
        elif rank == 5: # 3000-3500
            howmuch = 15, 60
            howmuchtime = 0.5, 1
        elif rank == 6: # 3500-5000
            howmuch = 20, 70
            howmuchtime = 0.35, 0.75
        elif rank == 7: # 5000-6900 sss
            howmuch = 30, 75
            howmuchtime = 0.25, 0.6
        elif rank == 8: # 6900+
            if cmd == "custom":
                print("Write it like that: 10, 20 and 0.5, 2")
                howmuch = int(input("How much keys?>>"))
                howmuchtime = int(input("How much time to press?>>"))
            else:
                howmuch = 75, 150
                howmuchtime = 0.2, 0.4
        shitcounter = 0
        print("Trying to find a game with difficulty matching your rating...")
        while True:
            shitcounter+=1
            PoolResA = random.randint(*howmuch)
            PoolResB = random.uniform(*howmuchtime)
            difficulty = round((PoolResA/25) * ((2.6-PoolResB)*100) * 10)
            if difficulty < crating: ...
            else:
                PoolRes = PoolResA, PoolResB
                break
            print(f"Try {shitcounter}...")
        game(*PoolRes)
    
    #game(20, 1.5)