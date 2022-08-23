# 2022.08.22.(화)
# [ 알고리즘 ]
# n ~ m 까지 합을 구하시오
def cal(n,m):
    return ((m)*(m+1) - n*(n-1))//2

print(cal(1,10))

#n,m = map(int, input().split())