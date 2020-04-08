objects =  [{'RXBC_CHROME_FOG': 100.0},{'RXBC_LAMP': 100.0},{'RXBC_WHITE_MIRROR': 99.97},{'RXBC_3_CHROME_GRILL': 99.95},
{'RXBC_INDC': 99.84},{'RXBC_WHITE_OS_HND': 98.93}]

result = []
for obj in objects:
    for val in obj:
        print()
        result.append(val +"~" +str(obj[val]))

data = {"output" : result}
print(data)
