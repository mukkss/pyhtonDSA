def pattern1(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
    pass
def pattern2(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    pass
def pattern3(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    pass
def pattern4(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
    pass
def pattern5(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*",end=" ")
        print()
    pass
def pattern6(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j,end=" ")
        print()
    pass
def pattern7(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*",end=" ")
        print()
    pass
def main():
    n = int(input())
    pattern7(n)

if __name__ == "__main__":
    main()