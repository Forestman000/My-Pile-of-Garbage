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

charset = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \n,.\'\":;(){}[]=+-*/<>`!?|~%#@$&_"
varlist = []

for i in range(256):
    varlist.append("")

# print(len(content))

while charnum < len(content):
    if content[charnum] == "(":
        charnum += 1
        charmode = True
    if content[charnum] == ")":
        charnum += 1
        charmode = False
    if content[charnum] == "+":
        pointer += 1
        charnum += 1
    elif content[charnum] == ">":
        pointer += 10
        charnum += 1
    elif content[charnum] == "-":
        pointer -= 1
        charnum += 1
    elif content[charnum] == "<":
        pointer -= 10
        charnum += 1
    elif content[charnum] == "/":
        if charmode == True:
            charnum += 1
            if 1 <= pointer <= len(charset):
                char = charset[pointer - 1]
            else:
                char = '?'
            temparray.append(char)
            tempstring = "".join(temparray)
        elif charmode == False:
            charnum += 1
            tempstring = "".join(temparray)
            temparray.append(varlist[pointer])
            print("variablised")
            print("t", tempstring)
    elif content[charnum] == "|":
        charnum +=1
        tempstring2 = varlist[pointer]
        print("*", tempstring2)
        print("#", tempstring)
        print("v", varlist[pointer])
    elif content[charnum] == "@":
        charnum += 1
        if pointer == 1:
            print(tempstring)
        if pointer == 2:
            tempstring = ""
            print("clear")
        if pointer == 3:
            tempstring2 = ""
            print("clear2")
        if pointer == 4:
            if tempstring.isdigit():
                int(tempstring)
            else:
                print("unable to convert non-numeric characters to integer")
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
            ans = int(tempstring) * int(tempstring2)
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


if isinstance(tempstring, int):
    pass
