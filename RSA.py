import random
import math
from time import sleep
# https://qiita.com/Euglenach/items/130472ad8c13d33ec7d9
# 上記サイトよりprimeを借用


def CheckEven(n):  # 偶数かどうかを判定。偶数だったらTrue
    if n & 1 == 0:
        return True
    else:
        return False


def CheckPrime(n):  # 素数かどうか判定。素数だったらTrue
    if n == 2:
        return True
    if n <= 1 or CheckEven(n):
        return False

    d = (n - 1) >> 1
    while CheckEven(n):
        d >>= 1

    for i in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = pow(y, 2, n)
            t <<= 1

        if y != n - 1 and CheckEven(t):
            return False

    return True


def get_random_prime(max):
    while True:
        num = random.randint(2, max)
        if CheckEven(num):
            num += 1
        if CheckPrime(num):
            break
    return num


def word2ascii(word):
    word = str(word)
    num_lis = []
    for s in word:
        num_lis.append(ord(s))
    return num_lis


def get_relatively_prime(num, max_num=400000):
    while True:
        k = random.randint(2, max_num)
        if math.gcd(k, num) == 1:
            return k


def get_secret_key(num, l):
    for i in range(l + 1):
        if i * num % l == 1:
            return i


def make_encript(asciied_word_lis, max_num=1000):
    p = get_random_prime(max_num)
    q = get_random_prime(max_num)
    while p == q:
        q = get_random_prime(max_num)
    n = p * q
    l = (p - 1) * (q - 1)
    k_1 = get_relatively_prime(l)
    k_2 = get_secret_key(k_1, l)
    print(l, k_1, k_2)
    enc_lis = []
    for s in asciied_word_lis:
        enc = pow(s, k_1, n)
        enc_lis.append(enc)
    return enc_lis, k_1, k_2, n


def make_plane_text(enc_lis, k, n):
    plane_lis = []
    for e in enc_lis:
        plane = chr(pow(e, k, n))
        plane_lis.append(plane)
    return ''.join(plane_lis)


if __name__ == "__main__":
    asciied_word = word2ascii("cat is not dog")
    print(asciied_word)
    enc, k_1, k_2, n = make_encript(asciied_word)
    print(enc, k_1, k_2, n)
    print(make_plane_text(enc, k_2, n))
