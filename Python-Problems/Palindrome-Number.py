## Check a Number is Palindrome

num = int(input("Enter a Number: "))

temp = num
rev = 0

while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

if(temp == rev):
    print("The Number is a palindrome")
else:
    print("Not a palindrome")

    
