# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37

n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 1
b = 2
c = 3
print(a)
print(b)
print(c)

for g in range(4,n+1):
    r = a+b+c
    print(r)
    a = b
    b = c
    c = r
    
    
