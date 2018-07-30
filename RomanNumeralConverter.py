

def RomanNumeralToDecimal(str):
    Numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    Decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    dec = 0
    iterator = 0
    place = 0

    while iterator < len(Numerals) and place < len(str):
        if Numerals[iterator] == str[place:(place + len(Numerals[iterator]))]:
            dec += Decimal[iterator]
            place += len(Numerals[iterator])
        else:
            iterator += 1

    return dec

print(RomanNumeralToDecimal("MCMDCDCXCLXLXIXVIVI"))