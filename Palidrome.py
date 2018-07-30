string = "ratatar"
string1 = "this should be false"

#Basic solution

reverse = []

reverse += string
reverse = reverse[::-1]

if string == "".join(reverse):
    print("Basic - true")
else:
    print("Basic - false")

#Intermediate
print("intermediate - true") if string == "".join(string[::-1]) else print("intermediate - false")

#Advance  -- will also only include letters not spaces or symbols
import re
comp = [0 , len(string)-1]
ret = "True"


while comp[0] < comp[1]:
    match = re.search('[a-zA-Z]', string[comp[0]])
    while match is None:
        comp[0] += 1
        match = re.search('[a-zA-Z]', string[comp[0]])

    match = re.search('[a-zA-Z]', string[comp[1]])
    while match is None:
        comp[1] -= 1
        match = re.search('[a-zA-Z]', string[comp[1]])

    if string[comp[0]] == string[comp[1]]:
        comp[0] += 1
        comp[1] -= 1
    else: #if this was a function I would return false here, and return true where print statement is
        comp[1] = -1
        ret = "False"

print("advanced - " + ret)
