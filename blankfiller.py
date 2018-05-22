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

filename = input("Hello! Please enter the name of the file that you would like to use: ")
file = open("files/hardware.txt", "r")
answerfile = open("files/hardwareAnswers.txt", "r")
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
