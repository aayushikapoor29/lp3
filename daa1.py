#recursive

def fibor(n):
    if n<=1:
        return n
    return(fibor(n-1) + fibor(n-2))



# iterative process
def fiboi(n):
    a = 0
    b = 1
    if n<= 0:
        return []
    elif n==1:
        return [0]
    
    series =[0,1]
    for i in range(2,n):
        a, b = b, a+b
        series.append(b)
    return series

num = int(input("Enter the number of terms: "))
l = []
print("Fibonacci series using recursive process:")
for i in range(num):
    l.append(fibor(i))
print(l)    

print("\nFibonacci series using iterative process:")
print(fiboi(num))