def analyze_string(s):
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

analyze_string("Mansi")

