inputStr = list(map(int,str(input()).split("+")))

inputStr.sort()

resultStr = "+".join(map(str, inputStr))
print(resultStr)