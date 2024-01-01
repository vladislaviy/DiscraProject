import random as rand
from sympy import randprime


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def get_random_prime(a,b):
    return randprime(a,b)


def rsa():
    p=get_random_prime(500,1000)
    q=get_random_prime(500,1000)
    n=p*q
    f=(p-1)*(q-1)
    e=get_random_prime(1,f)
    _,_,d=egcd(f,e)
    # d-закрытый ключ
    # n,e - параметры открытого ключа
    return n, e, d

def cipher(n, e, m):
    return pow(m,e,n)

def decipher(n, d, c):
    return pow(c,d,n)

def cipher_text(n,e,text):
    ans=[]
    for i in text:
        ans.append(cipher(n,e,ord(i)))
    return ans

def decipher_text(n, d, text):
    ans=""
    for i in text:
        ans+=chr(decipher(n,d,i))
    return ans

n,e,d=rsa()

print(9)
c=cipher(n,e,9)
print(c)
print(decipher(n,d,c))
t="Happy New Year (｡◕‿‿◕｡)"
print(decipher_text(n,d,cipher_text(n,e,t)))
