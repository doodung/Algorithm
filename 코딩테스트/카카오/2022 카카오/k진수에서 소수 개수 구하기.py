import math
# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2,int(math.sqrt(x))+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    answer = 0
    L=[]
    change_n = ''
    while n > 0:
        n, mod = divmod(n, k)
        change_n += str(mod)
    change_n=change_n[::-1]
    L=change_n.split('0')
    for l in L:
        if l!='' and l!='1':
            if is_prime_number(int(l)):
                answer+=1
    return answer