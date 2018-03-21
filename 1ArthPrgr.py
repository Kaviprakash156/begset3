def sumOfArthPrg( A, D, N) :
    sum = 0
    i = 0
    while i < N :
        sum = sum + A
        A = A + D
        i = i + 1
    return sum
N = int(input("Enter the N:\n"))
A = int(input("Enter the A:\n"))
D = int(input("Enter the D:\n"))
print (sumOfArthPrg(A, D, N))
