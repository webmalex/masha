a = [
    [0,0,0,0],
    [0,1,1,0],
    [1,1,0,0],
    [0,1,0,0],
    [1,0,1,0],
    [1,1,1,0],
    [2,2,2,1],
    [2,2,1,0],
    [3,2,4,1],
    [3,2,0,0],
    [10000,3,3,1],
    [10001,3,3,0],
    [30001,1,1,0],
    [30000,1,1,1],
    [3,2,8,0],
    [3,2,1,0]
]
for t in a:
    n,m,k,p = t
    r = 1 if 0 < k < n*m < 30001 and ((k >= n and not k % n) or (k >= m and not k % m)) else 0
    print(r==p,n,m,k,p,'->', r)

# n,m,k = [int(input()) for x in range(3)]
# print('YES' if 0 < k < n*m < 30001 and ((k >= n and not k % n) or (k >= m and not k % m)) else 'NO')
