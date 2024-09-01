
file = open("input", "r")
content = file.read()
#print(content)
file.close()

charnum = 0
pointer = 0
charmode = False

temparray = []
tempstring = ""
tempstring2 = ""
symbol = 0
charset = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \n,.\'\":;(){}[]=+-*/<>`!?|~%#@$&_"
varlist = []
funclist = []
add_string = "\033[36m"
Econtent = ""

for i in range(256):
    varlist.append("")
for I in range(32):
    funclist.append(['',''])
#print(funclist)

def error1():
    print("\033[31mValue Error Encountered at symbol #", symbol, ". process terminated")
    quit()

def error2():
    print("\033[31mType Error Encountered at symbol #", symbol, ". process terminated")
    quit()

def error3():
    print("\033[31mAttempt to assign character outside character value range Encountered at symbol #", symbol, ". process terminated")
    quit()


def function(symbol, pointer):
    pass


while charnum < len(content):
    if content[charnum] == "{":
        charnum += 1
        symbol += 1
        while content[charnum] != "}":
            charnum +=1
    elif content[charnum] == "}":
        charnum += 1
        symbol += 1
    elif content[charnum] == "(":
        charnum += 1
        symbol += 1
        charmode = True
    elif content[charnum] == ")":
        charnum += 1
        symbol += 1
        charmode = False
    elif content[charnum] == "+":
        pointer += 1
        charnum += 1
        symbol += 1
    elif content[charnum] == ">":
        pointer += 10
        charnum += 1
        symbol += 1
    elif content[charnum] == "-":
        pointer -= 1
        charnum += 1
        symbol += 1
    elif content[charnum] == "<":
        pointer -= 10
        charnum += 1
        symbol += 1
    elif content[charnum] == "/":
        charnum += 1
        symbol += 1
        if charmode == True:
            if 1 <= pointer <= len(charset):
                char = charset[pointer - 1]
            else:
                error3()
            temparray.append(char)
            tempstring = "".join(temparray)
        elif charmode == False:
            tempstring = "".join(temparray)
            temparray.append(varlist[pointer])
            print("variablised")
            print("t", tempstring)
    elif content[charnum] == "\\":
        charnum += 1
        symbol += 1
        tempstring2 = varlist[pointer]
        print("*", tempstring2)
        print("#", tempstring)
        print("v", varlist[pointer])
    elif content[charnum] == "@":
        charnum += 1
        symbol += 1
        if pointer == 1:
            print(tempstring)
        if pointer == 2:
            tempstring = ""
            print("clear")
        if pointer == 3:
            tempstring2 = ""
            print("clear2")
        if pointer == 4:
            try:
                tempstring.isdigit()
                tempstring2.isdigit()
                int(tempstring)
                int(tempstring2)
                print("inty")
            except ValueError:
                error1()
        if pointer == 5:
            try:
                if type(tempstring, tempstring2) == int:
                    ans = (tempstring) + (tempstring2)
            except TypeError:
                error2()
            print(tempstring)
            print(tempstring2)
            print("a =", ans)
        if pointer == 6:
            try:
                ans = int(tempstring) - int(tempstring2)
            except ValueError:
                error1()
            print(tempstring)
            print(tempstring2)
            print("a =", ans)
        if pointer == 7:
            try:
                ans = int(tempstring) * int(tempstring2)
            except ValueError:
                error1()
            print(tempstring)
            print(tempstring2)
            print("a =", ans)
        try:
            # Convert tempstring and tempstring2 to floats
            operand1 = float(tempstring)
            operand2 = float(tempstring2)

            # Perform the division operation
            ans = operand1 / operand2
        except ValueError:
            error1()
        except ZeroDivisionError:
            print("\033[31mError: Division by zero is not allowed.")
            quit()

        print("a =", ans)
        if pointer >= 8:
            varlist[pointer] = tempstring
            print("append", ":", tempstring)
            print("vv", varlist[pointer])
    else:
        charnum += 1
        #print("*")
