with open('reg_form.txt', 'w+') as f:
  class_size = int(input("Please enter the number of students in your class: "))
  f.write("Student Attenance Form" + "\n")
  for i in range(0,class_size):
    student_id = input("Please enter the next student id: ")
    f.write(student_id+"........" + "\n")