

def CeasarCipher(str):
    strs = 'abcdefghijklmnopqrstuvwxyz'
    out = []
    for i in str:                     #iterate over the text not some list
        if i.strip() and i in strs:                 # if the char is not a space ""  
            out.append(strs[(strs.index(i) + 3) % 26])    
        else:
            out.append(i)           #if space the simply append it to data
    output = ''.join(out)
    return output


print(CeasarCipher("thistext"))
