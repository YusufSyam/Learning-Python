def palindromTanpaSpasi(stringMentah):
    stringMentah= stringMentah.replace(" ","").upper()
    stringMentah= stringMentah[0:int((len(stringMentah))/2)]
    return stringMentah+(stringMentah[::-1])[1:len(stringMentah)]

stringMentah= input()
print("#"+hex(len(stringMentah)*len(stringMentah))[2:len(stringMentah)]+ palindromTanpaSpasi(stringMentah)+oct(len(stringMentah))[2:len(stringMentah)]+ ("?" if ((hex(len(stringMentah)*len(stringMentah))[2]).isalpha()) else "!"))

