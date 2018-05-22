import random

def easymode(file, answerfile):
    lines = file.readlines()
    answerlines = answerfile.readlines()
    for i in range(0, len(lines)):
        total = 0
        currentline = i
        for k in range(0, len(lines[currentline].split("@"))):
            answer = ""
            thing = lines[currentline].split("@")[k]
            total += 1
            if thing[-1] == "_":
                print(lines[currentline].split("@")[k-1].rstrip("\n").strip() + " ")
                i = 1
                options = []
                real = False
                for l in range(0, 3):
                    rand = random.randint(0, 300)
                    if  real == False:
                        if rand < 100:
                            real = True
                            options.append(answerlines[currentline].split("@")[k])
                        elif l == 2:
                            real = True
                            options.append(answerlines[currentline].split("@")[k])
                    else:
                        while True:
                            smallerrand = random.randint(0, len(answerlines)-1)
                            if smallerrand != currentline:
                                muchsmallerrand = random.randint(0, len(lines[smallerrand].split("@"))-1)
                                if lines[smallerrand].split("@")[muchsmallerrand][-1] == "_":
                                    break
                        options.append(answerlines[smallerrand].split("@")[muchsmallerrand])
                if len(options) < 3:
                    for z in range(0, 3 - len(options)):
                        if z != currentline:
                            options.append(answerlines[z].split("@")[k])
                        else:
                            options.append("Biscuits")
                print(options)
                for option in options:
                    print(str(i) + "). " + option)
                    i += 1
                target = "not an int"
                while True:
                    while not type(target) is int:
                        try:
                            target = int(input("Which would you like to choose"))
                        except ValueError as e:
                            print("This input must be a number")
                    if target >0 and target < 4:
                        break
                    else:
                        print("Bad input :-(")
                if options[target-1] == answerlines[currentline].split("@")[k]:
                    print("You were right!")
                else:
                    print("You were wrong :-(")
            else:
                if thing != "" and len(lines[currentline].split("@")) == k + 1:
                    print(thing.rstrip("\n").strip())
            

def mediummode(file, answerfile):
    lines = file.readlines()
    answerlines = answerfile.readlines()
    for i in range(0, len(lines)):
        total = 0
        currentline = i
        for k in range(0, len(lines[currentline].split("@"))):
            answer = ""
            thing = lines[currentline].split("@")[k]
            total += 1
            if thing[-1] == "_":
                    answer = input(lines[currentline].split("@")[k-1].rstrip("\n").strip() + " " + answerlines[currentline].split("@")[k].rstrip("\n").strip()[0]) 
            else:
                if thing != "" and len(lines[currentline].split("@")) == k + 1:
                    print(thing.rstrip("\n").strip())
                answer = ";;;"
            if answer != ";;;":
                correct = True
                for j in range(1, len(answer)):
                    if len(answer) < len(answerlines[currentline].split("@")[k])-1:
                        print("You were wrong :-(")
                        correct = False
                        break
                    if answerlines[currentline].split("@")[k][j] != answer[j-1]:
                        print("You were wrong :-(")
                        correct = False
                        break
                if correct:
                    print("You were right!")

def hardmode(file, answerfile):
    lines = file.readlines()
    answerlines = answerfile.readlines()
    for i in range(0, len(lines)):
        total = 0
        currentline = i
        for k in range(0, len(lines[currentline].split("@"))):
            answer = ""
            thing = lines[currentline].split("@")[k]
            total += 1
            if thing[-1] == "_":
                    answer = input(lines[currentline].split("@")[k-1].rstrip("\n").strip() + " ") 
            else:
                if thing != "" and len(lines[currentline].split("@")) == k + 1:
                    print(thing.rstrip("\n").strip())
                answer = ";;;"
            if answer != ";;;":
                correct = True
                for j in range(0, len(answer)):
                    if len(answer) < len(answerlines[currentline].split("@")[k]):
                        print("You were wrong :-(")
                        correct = False
                        break
                    if answerlines[currentline].split("@")[k][j] != answer[j]:
                        print("You were wrong :-(")
                        correct = False
                        break
                if correct:
                    print("You were right!")
try:
    filename = input("Hello! Please enter the name of the file that you would like to use: ")
    file = open("files/" + filename + ".txt", "r")
    answerfile = open("files/" + filename + "Answers.txt", "r")
    while True:
        difficulty = int(input("What level of difficulty would you like? (1-3)"))
        if difficulty == 1:
            easymode(file, answerfile)
            break
        elif difficulty == 2:
            mediummode(file, answerfile)
            break
        elif difficulty == 3:
            hardmode(file, answerfile)
            break
except ValueError as e:
    print("You gave a bad input... please restart")
