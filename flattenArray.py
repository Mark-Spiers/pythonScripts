uglyArray = [[1,2,[3,5]],4]

def flattenArray(arr):
    flat = []

    for item in arr:
        if isinstance(item, list):
            flat.extend(flattenArray(item))
        else:
            flat.append(item)

    return flat



print(flattenArray(uglyArray))