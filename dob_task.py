f = open('DOB.txt', 'r+')


lines = f.readlines()

print("Name")
for line in lines:
    temp = line.strip()
    temp = temp.split()
    name = " ".join(temp[0:2])
    print(name)

print("Date of Birth")
for line in lines:
    temp = line.strip()
    temp = temp.split()
    dob = " ".join(temp[2:])

    print(dob)

    
f.close()