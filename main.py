import sys

def main ():
    
    choice = 0
    
    while choice != 1 or choice != 2 or choice != 3:
        print('Alternating the Use of Addition and subtraction on Binary Strings')
        print('-----------------------------------------------------------------')
        print('')
        print('This program uses a DFA to add two given binary strings together')
        print('while alternating between addition and subtraction of the weights')
        print('when encontering a 1. Finally the resulting binary string will be')
        print('displayed. This program is based off the dragon curve problem.')
        print('')
        print('1.Alternating')
        print('2.Addition')
        print('3.Subtraction')
        print('4.Quit')
        choice = int(sys.stdin.readline())
        if choice == 4:
            exit()
        if choice == 1:
            while choice == 1:
                print('')
                print('Give first binary string')
                w1 = str(input())
                #print(w1)
                print('Give second binary string')
                w2 = str(input())
                #print(w2)
                print('')
                print(Run_DFA(w1, w2))
                print('')
                print('Would you like to run again?')
                print('1.Yes')
                print('2.No')
                sel = int(sys.stdin.readline())
                if sel != 1:
                    choice = 4
        elif choice == 2:
            while choice == 2:
                print('')
                print('Give first binary string')
                w1 = str(input())
                #print(w1)
                print('Give second binary string')
                w2 = str(input())
                #print(w2)
                print('')
                print(Addition_DFA(w1, w2))
                print('')
                print('Would you like to run again?')
                print('1.Yes')
                print('2.No')
                sel = int(sys.stdin.readline())
                if sel == 1:
                    choice = 2
                else:
                    choice = 4
        elif choice == 3:
            while choice == 3:
                print('')
                print('Give first binary string')
                w1 = str(input())
                #print(w1)
                print('Give second binary string')
                w2 = str(input())
                #print(w2)
                print('')
                print(Subtraction_DFA(w1, w2))
                print('')
                print('Would you like to run again?')
                print('1.Yes')
                print('2.No')
                sel = int(sys.stdin.readline())
                if sel == 1:
                    choice = 3
                else:
                    choice = 4

def Run_DFA (w1, w2):
    output = ""
    DFA = [[0,1,2,4],
           [1,0,3,2],
           [2,3,0,1],
           [3,2,1,0],
           [4,2,1,0]]
    position_value = [[0,1,1,0],
                      [0,-1,1,0],
                      [0,1,-1,0],
                      [0,-1,-1,-1],
                      [1,-1,-1,1]]
    while len(w1) < len(w2):
        w1 = "0" + w1
    while len(w2) < len(w1):
        w2 = "0" + w2
    w1 = "0" + w1
    w2 = "0" + w2
    top = -1
    bottom = -1

    state = 0
    for idx in range(0, len(w1)):
        value = 0
        idx += 1
        print("state = " + str(state)) 
        if w1[len(w1)-idx] == "1" and w2[len(w2)-idx] == "0":
            value = 1
            if top == -1:
                top = idx
        elif w1[len(w1)-idx] == "0" and w2[len(w2)-idx] == "1":
            value = 2
            if bottom == -1:
                bottom = idx
        elif w1[len(w1)-idx] == "1" and w2[len(w2)-idx] == "1":
            value = 3
            if top == -1:
                top = idx
            if bottom == -1:
                bottom = idx
        tmp = str(position_value[state][value])
        #print("value = " + tmp)
        if tmp == "-1":
            output = "1" + output
            #print ("Hit")
            #print(output)
            sub = "1"
            if value == 1:
                for i in range(0,top):
                    sub += "0"
                top = -1
            elif value == 2:
                for i in range(0,bottom):
                    sub += "0"
                bottom = -1
            elif value == 3:
                if top != -1 and bottom == -1:
                    for i in range(0,top):
                        sub += "0"
                    top = -1
                elif top == -1 and bottom != -1:
                    for i in range(0,bottom):
                        sub += "0"
                    bottom = -1
                else:
                    if top < bottom:
                        for i in range(0,bottom):
                            sub += "0"
                        sub += "1"
                        for i in range(0,top):
                            sub += "0"
                    elif bottom < top:
                        for i in range(0,top):
                            sub += "0"
                        sub += "1"
                        for i in range(0,bottom):
                            sub += "0"
                    else:
                        for i in range(0,top):
                            sub += "0"
                    top = -1
                    bottom = -1

            #print(sub)
            output = Subtraction_DFA(output, sub)
            output = output[1:]
        else:
            output = tmp + output
        state = DFA[state][value]

    return output

def Addition_DFA (w1, w2):
    output = ""
    DFA = [[0,0,0,1],
           [1,1,1,0]]
    position_value = [[0,1,1,0],
                      [1,0,0,1]]
    while len(w1) < len(w2):
        w1 = "0" + w1
    while len(w2) < len(w1):
        w2 = "0" + w2
    w1 = "0" + w1
    w2 = "0" + w2

    state = 0
    for idx in range(0, len(w1)):
        value = 0
        idx += 1
        if w1[len(w1)-idx] == "1" and w2[len(w2)-idx] == "0":
            value = 1
        elif w1[len(w1)-idx] == "0" and w2[len(w2)-idx] == "1":
            value = 2
        elif w1[len(w1)-idx] == "1" and w2[len(w2)-idx] == "1":
            value = 3

        output = str(position_value[state][value]) + output
        state = DFA[state][value]

    return output

def Subtraction_DFA (w1, w2):
    output = ""
    DFA = [[0,0,1,0],
           [1,0,1,1]]
    position_value = [[0,1,1,0],
                      [1,0,0,1]]
    while len(w1) < len(w2):
        w1 = "0" + w1
    while len(w2) < len(w1):
        w2 = "0" + w2
    w1 = "0" + w1
    w2 = "0" + w2

    state = 0
    for idx in range(0, len(w1)):
        value = 0
        idx += 1
        if w1[len(w1)-idx] == "1" and w2[len(w2)-idx] == "0":
            value = 1
        elif w1[len(w1)-idx] == "0" and w2[len(w2)-idx] == "1":
            value = 2
        elif w1[len(w1)-idx] == "1" and w2[len(w2)-idx] == "1":
            value = 3

        output = str(position_value[state][value]) + output
        state = DFA[state][value]

    return output


main()
