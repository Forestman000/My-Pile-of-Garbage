
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
add_string = "\033[36m"
Econtent = ""

for i in range(256):
    varlist.append("")

def error1():
    print("\033[31mValue Error Found at symbol #", symbol, ". process terminated")
    quit()


while charnum < len(content):
    if content[charnum] == "(":
        charnum += 1
        symbol += 1
        charmode = True
    if content[charnum] == ")":
        charnum += 1
        symbol += 1
        charmode = False
    if content[charnum] == "+":
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
                char = '?'
            temparray.append(char)
            tempstring = "".join(temparray)
        elif charmode == False:
            tempstring = "".join(temparray)
            temparray.append(varlist[pointer])
            print("variablised")
            print("t", tempstring)
    elif content[charnum] == "|":
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
                int(tempstring)
            except ValueError:
                error1()
        if pointer == 5:
            ans = int(tempstring) + int(tempstring2)
            print(tempstring)
            print(tempstring2)
            print("a =", ans)
        if pointer == 6:
            ans = int(tempstring) - int(tempstring2)
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
        if pointer >= 8:
            varlist[pointer] = tempstring
            print("append", ":", tempstring)
            print("vv", varlist[pointer])
    else:
        charnum += 1
        #print("*")
