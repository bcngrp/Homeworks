adenine = 0
timin = 0
guanin = 0
cytosine = 0 
DNA = input("DNA Stringini giriniz : ")
for letter in DNA:
    if letter == "A" or letter == 'a':      
        adenine += 1
    elif letter == "T" or letter == 't':      
        timin += 1
    elif letter == "G" or letter == 'g':      
        guanin += 1
    elif letter == "C" or letter == 'c':      
        cytosine  += 1
print(adenine , " " , timin , " " , guanin ," ",cytosine)


