import numpy as np
new = " "
list = ["string", "cat", "ball", "toys", "mittens"]
grades = [98, 55, 67, 20, 100, 59, 73, 81]

def cats():
    for x in list:
        print(x, end = " ")

def school():
    for pupil in grades:
        print(pupil, end = " ")

str_grades = [str(grade) for grade in grades]#makes each value in the list a string
string_grades = str(grades) #makes list into string
np_grades = np.array(str_grades) #didn't work
np_list = np.array(list) #didn't work

new = str_grades + list
newer = sorted([ne.upper() for ne in new])
print(newer)