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
        

    








