

#program should create a half diamon pattern using "*" and a singular for loop and if else statements

stars=1 #variable name stars that is valued at 1

for i in range(10): #for loop that iterates 10 times
    if i<4: # if the interations are less than 4 the program should start priniting ou tthe first half of the pattern by adding more * to stars
        print(('*'*stars))
        stars=stars+1
    else: #this else statement creates the second half of the pattern by removing * from stars
        print(('*'*stars))
        stars=stars-1


#the below comments are some of my failed attempts because the above code is the only way I have found that prints both halfs of the pattern
#I tried using -= to do the opposite of the first half of the pattern but that just retuned an error 
"""stars = ""
for i in range(10):
    stars += "*"
    print(stars)
    if i < 1:
        stars -= "*"
        print(stars)"""


        
"""stars = ''

for i in range(10):
    if i<5:
        stars += '*'
        print(stars)"""