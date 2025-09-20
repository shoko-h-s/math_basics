import math

# 階乗
def factorial():
    n = int(input("\n階乗を求める数値を入力："))
    print(math.factorial(n))

# 順列
def perm():
    n, k = map(int, input("\n順列 P の前後の数値を、半角スペース区切りで入力：").split())
    print(math.perm(n, k))

# 組み合わせ
def comb():
    n, k = map(int, input("\n組み合わせ C の前後の数値を、半角スペース区切りで入力：").split())
    print(math.comb(n, k))

# 重複組み合わせ
def h_comb():
    n, r = map(int, input("\n重複組み合わせ H の前後の数値を、半角スペース区切りで入力：").split())
    front_c = n + r - 1
    print(math.comb(front_c, r))