swimming = float(input("please enter time for swimming "))
cycling = float(input("please enter time for cycling "))
running = float(input("please enter time running "))
total_time = 0
total_time = swimming + cycling + running

if total_time <=100:
    award = "Provincial Colours"
elif total_time >=101:
    award = "Provincial Half Colours"
elif total_time >=106:
    award = "Provincial Scroll"
elif total_time >=111:
    award = "No award"
print(f"Your total time is {total_time} and you get {award}")
