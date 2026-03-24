def main(n):
    if(n==0):
        print(f"Fibonacci series up to {n}th term.")
    else:
        second_last = 0
        last = 1
        print(f"Fibonacci series up to {n}th term.")
        print(f"{second_last} {last}", end=" ")
        i = 2
        while(i<=n):
            cur = second_last + last
            second_last = last
            last = cur
            print(cur, end=" ")
            i+=1

if __name__=="__main__":
    print("Enter the number of terms in Fibonacci series: ", end="")
    n = int(input())
    main(n)