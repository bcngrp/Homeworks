data = open("C:/Users/bican/Desktop/Proje/data.txt", "w")
data.write('Name: Wesley\n' 'Surname: Sneijder\n' 'Gender: Male\n' 'Username: Sneijder10\n' 'Job: Footballer\n')
data.close()
data = open("C:/Users/bican/Desktop/Proje/data.txt", "r")

a = (data.read().split("\n"))
a.pop()
print(a)

Informations = {}
for i in a:
    b = i.split(": ")
    Informations.update({b[0]:b[1]})
print(Informations)