#Question 2)
def analyze_string(s):
    if s :
        print("The length of string is : ",len(s))
        print("The reverse of string is : ",s[: : -1])
        count = 0
        for i in range(len(s)):
            if i in ("a","e","i","o","u") :
                count+=1
        print("The number of vowels in the string are : ",count)
        print("Characters of string with their positive and negative index are : ")
        for i in range(len(s)):
            print("Positive index of ",s[i], " is :",i," Negative index is : ",i - len(s))
    else :
        print("String is empty!")
s = input("Enter a string : ")
analyze_string(s)

#Question 3)

def manage_marks():
    try:
        s1 = int(input("Enter the marks of sub1 : "))
        s2 = int(input("Enter the marks of sub2 : "))
        s3 = int(input("Enter the marks of sub3 : "))
        s4 = int(input("Enter the marks of sub4 : "))
        s5 = int(input("Enter the marks of sub5 : "))
        sub_list = [s1,s2,s3,s4,s5]
    except ValueError:
        print("Enter a valid number !")
        avg = (s1+s2+s3+s4+s5)/5
        high = max(sub_list)
        low = min(sub_list)
        print("Average marks : ",avg)
        print("Highest marks : ",high)
        print("Lowest marks : ",low)
        print("Printing sorted list in descending order : ",sub_list.sort(reverse=True))
manage_marks()

#Question 4)
class Student :
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no =roll_no
    def add_mark(self,mark) :
        self.marks_list= mark
    def get_average(self):
        sum=0
        for i in range(len(marks_list)):
            sum += self.marks_list[i]
        avg = sum/5
        return avg
    def display_info(self):
        print("Student name : ",self.name)
        print("Roll no : ",self.roll_no)
        print("Marks of five subjects : ",self.marks_list)
        print("Average :  ",self.get_average())
def main():
    name = input("Enter name : ")
    roll_no = int(input("Enter roll_no : "))
    try :
        s1 = int(input("Enter marks of sub1 :"))
        s2 = int(input("Enter marks of sub2 :"))
        s3 = int(input("Enter marks of sub3 :"))
        s4 = int(input("Enter marks of sub4 :"))
        s5 = int(input("Enter marks of sub5 :"))
    except ValueError:
        print("Marks should be integer value !")
    marks_list = [s1,s2,s3,s4,s5]
    stud = Student("Mansi",54,)
    stud.add_mark(marks_list)
    stud.get_average()
    stud.display_info()

#Question 5)

def student_database():
    students = {}
    
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add student")
        print("2. Search student by roll number") 
        print("3. Display all students")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice 1-4: "))
        except ValueError:
            print("Invalid input! Please enter a number 1-4.")
            continue
        if choice == 1:
            try:
                roll_no = int(input("Enter roll number: "))
                name = input("Enter name: ").strip()
                age = int(input("Enter age: "))
                city = input("Enter city: ").strip()
                
                if not name or not city:
                    print("Name and city cannot be empty.")
                    continue
                    
                if age <= 0:
                    print("Age must be positive.")
                    continue
                
                students.update({roll_no: {"name": name, "age": age, "city": city}})
                print("Student", name, "added successfully.")
                
            except ValueError:
                print("Roll number and age must be numbers.")


        elif choice == 2:
            try:
                roll_no = int(input("Enter roll number to search: "))
                student = students.get(roll_no)
                
                if student:
                    print("\nRoll No:", roll_no)
                    print("Name:", student['name'])
                    print("Age:", student['age'])
                    print("City:", student['city'])
                else:
                    print("Student not found.")
                    
            except ValueError:
                print("Roll number must be a number.")
        elif choice == 3:
            if not students:
                print("No students in database.")
            else:
                print("\n--- All Students ---")
                for roll_no, info in students.items():
                    print("Roll:", roll_no, ", Name:", info['name'], ", Age:", info['age'], ", City:", info['city'])
                    
        elif choice == 4:
            print("Exiting Student Database. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter 1-4.")

# Call the function to run it
student_database()

#Question 6)

import random
import math
def unique_numbers_program():
    unique_nums = set()
    print("Enter 10 numbers : ")
    for i in range(10):
        try:
            num = float(input("Enter number : ",str(i+1)+ " : "))
            unique_nums.add(num)
        except ValueError:
        print("Invalid Input!please enter a number : ")            
        continue


    








