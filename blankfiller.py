def calculatediff(line, answerline, timeround):
    total = 0
    array = []
    empty = ""
    equal = True
    for i in range(0, len(line)):
        if not line[i] == answerline[i]:
            equal = False
            empty += answerline[i]
        else:
            if not equal:
                equal = True
                array.append(empty)
                empty = ""
    if len(array) >= timeround:
        return len(array[timeround-1])
    return 80

def hardmode(file, answerfile):
    lines = file.readlines()
    answerlines = answerfile.readlines()
    for i in range(0, len(lines)):
        total = 0
        currentline = i
        for k in range(0, len(lines[currentline].split("_"))):
            thing = lines[currentline].split("_")[k]
            total += 1
            if thing != "":
                if len(lines[currentline].split("_")) >= k + 2:
                    if lines[currentline].split("_")[k+2] == "":
                        answer = input(thing.rstrip("\n").strip() + " ") 
                else:
                    answer = ";;;"
                if answer != ";;;":
                    correct = True
                    for j in range(0, calculatediff(lines[currentline], answerlines[currentline], total)):
                        if calculatediff(lines[currentline], answerlines[currentline], total)-1 >= len(answer):
                            print("Wrong")
                            correct = False
                            break
                        if answerlines[currentline][len(thing)+j] != answer[j]:
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
