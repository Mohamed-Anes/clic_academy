# In[]
import json
import re

with open('niv1_conjg - Copy.json', 'r', encoding="utf-8") as file:
    # Load JSON data
    data = json.load(file)
    # print(data)

out = {}

i = 0
for key, item in data.items():

    # mot = re.sub(r'[^ابتثجحخدذرزسشصضطظعغفقكلمنهويىآإؤء]', '', key)
    # item = re.sub(r'[^ابتثجحخدذرزسشصضطظعغفقكلمنهويىآإؤء]', '', item)

    print(key, "\n\n\n")


# In[]

with open('temp.txt', 'w', encoding="utf-8") as file:
    for key, item in data.items():
        file.write(key + ' : \n')
        print(type(item))
        if type(item) == type(list()):
            print(len(item))
            for i in item:
                file.write('[' + str(i.split()) + ']' + '\n')
        else:
            file.write(str(item))
        file.write('\n----------\n')


# In[]
print(type(list()))

# %%
