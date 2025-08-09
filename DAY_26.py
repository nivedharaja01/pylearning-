##LISTS COMPHREHENSION
  ##new_list = [new_item for item in list]

numbers = [1,2,3]
new_numbers = [ n + 1 for n in numbers]
print(new_numbers)

name = "Nivedha"
new_name = [ letter for letter in name]
print(new_name)

range_list = [num*2 for num in range(1,5)]
print (range_list)

## CONDITIONAL LIST COMPREHENSION 
    ##new_list = [new_item for item in list if test]

names = ['Amaiya','Ani','Rena','Radhi','Arjun','Guna','Vijay','Rocky','Teju']
short_names = [name for name in names if len(name)<5]
print(short_names)

long_names = [name.upper() for name in names if len(name)> 4]
print(long_names)

##DICTIONARY COMPHREHENSION 
   ##NEW_DICT = {NEW_KEY : NEW_VALUE FOR ITEM IN LIST}

names = ['Amaiya','Kamal','Ani','Rena','Radhi','Arjun','Guna','Vijay','Rocky','Teju']
import random 
student_score = {student:random.randint(10,100)for student in names}
print(student_score)

##New_dict = {new_key:new_value for (key,value) in dictionary.tems()if }

passed_students = {student:score for (student,score) in student_score.items()if score >= 60 }
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split() }
print(result)
#.split() turns the sentence into a list of words.

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)

#looping through the DataFrame 

import pandas 

student_dict = {
               "student":["Amaiya","Kamal","Ani","Rena"],
               "score": [55,66,77,88]
}
student_DF = pandas.DataFrame(student_dict)
print(student_DF)

##loop through rows of a dataframe

for (index,row) in student_DF.iterrows():
    if row.student == "Amaiya":
        print(row.score)

