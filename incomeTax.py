income = int(input("Enter the Income per Annum: "))
s1 = income * 0
s2 = ((income-20000)*(10/100))
s3 = 20000 + ((income - 400000)*(20/100))
s4 = 60000 + ((income - 600000)*(40/100))
if income < 200000:
    it=s1
    print(it)
elif income < 400000 and income > 200000:
    it=s2
    print(it)
elif income < 600000 and income > 400000:
    it=s3
    print(it)
else:
    it = s4
    print(it)  