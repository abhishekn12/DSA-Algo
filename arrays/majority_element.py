"""
Sample Input 1:
2
5
2 3 9 2 2
4
8 5 1 9 

Sample Output 1:
2
-1
"""
----------------------------------------------------------------------------------
from collections import Counter

arr = [1,2,3,2,2,2]

a=Counter(arr)
size= len(arr)
m = {} 
for i in range(size): 
    if arr[i] in m: 
        m[arr[i]] += 1
    else: 
        m[arr[i]] = 1
count = 0
print(m)
for key in m: 
    print(m[key], end = " ")
    if m[key] > size / 2: 
        count = 1
        print(key) 
        break
if(count == 0): 
    print("-1")
    
--------------------------------------------------------------------------

from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a=Counter(a)
    a1=max(a.values())
    if a1>n/2:
        print(a.most_common(1)[0][0])
    else:
        print(-1)