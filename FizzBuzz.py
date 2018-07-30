
def Fizzbuzz(arr):
    for i in range(1, 100):
        out = ""

        for x in arr:
            if i % x[0] == 0:
                out += x[1]

        if out == "":
            print(i)
        else:
            print(out)



array = [[3, "Fizz"], [5, "Buzz"]]

Fizzbuzz(array)