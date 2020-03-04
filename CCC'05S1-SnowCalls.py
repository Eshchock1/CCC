letterDict = {
  "A": 2,
"B": 2,
"C": 2,
"D": 3,
"E": 3,
"F": 3,
"G": 4,
"H": 4,
"I": 4,
"J": 5,
"K": 5,
"L": 5,
"M": 6,
"N": 6,
"O": 6,
"P": 7,
"Q": 7,
"R": 7,
"S": 7,
"T": 8,
"U": 8,
"V": 8,
"W": 9,
"X": 9,
"Y": 9,
"Z": 9,
}
phoneNumbers = []
phoneNumberI = int(input())

for i in range(phoneNumberI):
    phoneNumber = input()
    dashlessNumber = ""
    for n in range(len(phoneNumber)):
        if phoneNumber[n] != "-":
            dashlessNumber += phoneNumber[n]
    phoneNumbers.append(dashlessNumber[0:10])

for i in range(phoneNumberI):
    currentNumber = phoneNumbers[i]
    formattedNumber = ""
    for n in range(len(currentNumber)):
        character = currentNumber[n]
        if n == 3:
            formattedNumber += "-"
        if n == 6:
            formattedNumber += "-"
        if character in letterDict:
            formattedNumber += str(letterDict[character])
        else:
            formattedNumber += str(character)
    print(formattedNumber)