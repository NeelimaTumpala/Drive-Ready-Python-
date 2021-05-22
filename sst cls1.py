"""

n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")

output:

2
even
3
odd

"""
"""
t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        print("even")
    else:
        print("odd")
        


output:

2
3
odd
2
even

"""

"""

n=int(input())
if n==0:
    print("zero")
if n>0:
    print("positive")
if n<0:
    print("negative")


output:

0
zero

2
positive

-2
negative

"""
"""
n,m=map(int,input().split())
for i in range(n,m+1):
    print(i,end=" ")

output:

0 10
0 1 2 3 4 5 6 7 8 9 10
"""
"""

n,m=map(int,input().split())
for i in range(n,m-1,-1):
    print(i,end=" ")

output:

10 0
10 9 8 7 6 5 4 3 2 1 0

"""
"""
n,m=map(int,input().split())
i=n
while i<=m:
    print(i,end=" ")
    i+=1

output:

0 10
0 1 2 3 4 5 6 7 8 9 10 
"""

"""
n,m=map(int,input().split())
i=n
while i>=m:
    print(i,end=" ")
    i-=1

output:
10 0
10 9 8 7 6 5 4 3 2 1 0

"""
"""


n,m=map(int,input().split()) #10 0
i=n #10
while i>=m: #10>0
    if i%3==0:
        i-=1
        continue
    print(i,end=" ")
    i-=1

output:
10 0
10 8 7 5 4 2 1

"""
"""
n,m=map(int,input().split()) 
i=n 
while i<=m: 
    if i%3==0:
        i+=1
        continue
    print(i,end=" ")
    i+=1


output:

0 10
1 2 4 5 7 8 10

"""
"""

n,m=map(int,input().split())
for i in range(n,m+1):
    if i%3==0:
        i+=1
        continue
    print(i,end=" ")


output;

0 10
1 2 4 5 7 8 10

"""

"""
n,m=map(int,input().split())
for i in range(n,m+1):
    print(i,end=" ")
    if i%4==0 and i!=4:
        break

output;

1 10
1 2 3 4 5 6 7 8

"""
"""


n,m=map(int,input().split())
for i in range(n,m+1):
    print(i,end=" ")
    if i%4==0:
        break


output;

1 10
1 2 3 4

"""
