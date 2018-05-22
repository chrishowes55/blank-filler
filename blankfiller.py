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
                    print("if if")
                    answer = input(thing.rstrip("\n").strip() + " ") 
            else:
                print("else")
                answer = ";;;"
            if answer != ";;;":
                print("Ansy")
                correct = True
                print(lines[currentline].split("@"))
                for j in range(0, len(answer)):
                    if len(answer) < len(answerlines[currentline].split("@")[k]):
                        print("Wrong")
                        correct = False
                        break
                    if answerlines[currentline].split("@")[k][j] != answer[j]:
                        print("Wrong")
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
