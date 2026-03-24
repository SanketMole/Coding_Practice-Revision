def pali(num):
    dup = num 
    rev = 0
    while(num > 0):
        ld = num % 10
        rev = (rev * 10) + ld 
        num = num // 10 
    return dup == rev 
if __name__=="__main__":
    n = int(input("Enter a number: "))
    if(pali(n)):
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")

        