import sys

def main ():
    
    choice = 0
    
    while choice != 1:
        print('Alternating the Use of Addition and subtraction on Binary Strings')
        print('-----------------------------------------------------------------')
        print('')
        print('This program uses a DFA to add two given binary strings together')
        print('while alternating between addition and subtraction of the weights')
        print('when encontering a 1. Finally the resulting binary string will be')
        print('displayed. This program is based off the dragon curve problem.')
        print('')
        print('1.Start')
        print('2.Quit')
        choice = int(sys.stdin.readline())
        if choice == 2:
            exit()
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
        choice = int(sys.stdin.readline())

def Run_DFA (w1, w2):
    dfa = [[0,1,2,3],
           [1,0,3,2],
           [2,3,0,1],
           [3,6,4,0],
           [4,0,5,8],
           [5,0,4,8],
           [6,7,0,8],
           [7,6,0,8]]
    prev = 0
    state = 0
    value = 0
    
    if len(w1) < len(w2):
        while(len(w1) < len(w2)):
            w1 = "0" + w1
    elif len(w2) < len(w1):
        while(len(w2) < len(w1)):
            w2 = "0" + w2

    idx = 0
    hold = -1
    output = ""
    gap = 0
    print(w1 + "    " + w2)
    print('')
    while idx < len(w1):
        gap += 1
        if(w1[idx] == "0" and w2[idx] == "0"):
            value = 0
        elif(w1[idx] == "1" and w2[idx] == "0"):
            value = 1
        elif(w1[idx] == "0" and w2[idx] == "1"):
            value = 2
        elif(w1[idx] == "1" and w2[idx] == "1"):
            value = 3

        return_state = dfa[state][value]
        print(return_state)
        if return_state != state or value == 1 or value == 2:
            prev = state
            state = return_state
            if(prev == 1 and state == 0):
                if hold !=0:
                    while gap > 1:
                        output += "1"
                        gap -= 1
                gap -=1
            elif(prev == 0 and state == 1):
                while gap > 1:
                    output += "0"
                    gap -= 1
                gap -= 1
                output += "1"
            elif(prev == 2 and state == 0):
                if hold != 0:
                    while gap > 1:
                        output += "1"
                        gap -= 1
                gap -= 1
            elif(prev == 0 and state == 2):
                while gap > 1:
                    output += "0"
                    gap -= 1
                output += "1"
                gap -= 1
            elif(prev == 1 and state == 3):
                while gap > 1:
                    output += "0"
                    gap -= 1
                output += "1"
                gap -= 1
            elif(prev == 3 and state == 2):
                tmp = output[:-1]
                tmp += "0"
                while gap > 0:
                    tmp += "1"
                    gap -= 1
                output = tmp
            elif(prev == 2 and state == 3):
                while gap > 1:
                    output += "0"
                    gap -= 1
                output += "1"
                gap -= 1
            elif(prev == 3 and state == 1):
                tmp = output[:-1]
                tmp += "0"
                while gap > 0:
                    tmp += "1"
                    gap -= 1
                output = tmp
            elif(prev == 3 and state == 4):
                tmp = output[:-1]
                tmp += "0"
                while gap > 0:
                    tmp += "1"
                    gap -= 1
                output = tmp
                print(output)
            elif(prev == 4 and state == 5):
                while gap > 0:
                    output += "0"
                    gap -= 1
            elif(prev == 4 and state == 0):
                tmp = output[:-1]
                tmp += "0"
                while gap > 0:
                    tmp += "1"
                    gap -= 1
                output = tmp
            elif(prev == 5 and state == 4):
                while gap > 0:
                    output += "0"
                    gap -= 1
            elif(prev == 5 and state == 0):
                while gap > 0:
                    output += "1"
                    gap -= 1
            elif(prev == 3 and state == 6):
                tmp = output[:-1]
                tmp += "0"
                while gap > 0:
                    tmp += "1"
                    gap -= 1
                output = tmp
                print(output)
            elif(prev == 6 and state == 7):
                while gap > 0:
                    output += "0"
                    gap -= 1
            elif(prev == 6 and state == 0):
                tmp = output[:-1]
                tmp += "0"
                while gap > 0:
                    tmp += "1"
                    gap -= 1
                output = tmp
            elif(prev == 7 and state == 6):
                while gap > 0:
                    output += "0"
                    gap -= 1
            elif(prev == 7 and state == 0):
                while gap > 0:
                    output += "1"
                    gap -= 1
        idx +=1

    if hold == 1:
        output += "1"
    while gap > 0:
        output += "0"
        gap -= 1

    return output

main()
