swimming = float(input("please enter time for swimming "))
cycling = float(input("please enter time for cycling "))
running = float(input("please enter time running "))
total_time = round(swimming + cycling + running)

if total_time <=100:
    award = "Provincial Colours"
elif (total_time >=101) and (total_time <=105):
    award = "Provincial Half Colours"
elif (total_time >=106) and (total_time<=110):
    award = "Provincial Scroll"
elif total_time >=111:
    award = "No award"
print(f"Your total time is {total_time} and you get {award}")
