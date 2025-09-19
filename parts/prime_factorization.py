import collections

def main():
    while True:
        try:
            print("\n素数判定を行い、素数でない場合は素因数分解を行う。")
            user_input = int(input("判定を行う数値を入力："))
            break
        except ValueError:
            print("無効な入力です。整数を入力してください。")

    # 以下、処理部分
    prime_factors = []   # 素因数を格納
    tmp = user_input

    while tmp % 2 == 0:
        prime_factors.append(2)
        tmp //= 2

    f = 3

    while f * f <= tmp:
        if tmp % f == 0:
            prime_factors.append(f)
            tmp //= f
        else:
            f += 2

    if tmp != 1:
        prime_factors.append(tmp)

    dict_prime_factors = collections.Counter(prime_factors)


    prime_text = ""
    cnt = 1
    total = 1

    for key, value in dict_prime_factors.items():
        # 素因数分解の結果を見やすくする
        prime_text += str(key) + "^" + str(value) + " "

        # 約数の個数を求める
        cnt *= value + 1
        total_i = 0

        for i in range(value + 1):
            total_i += key ** i

        total *= total_i

    # 約数の個数が2、約数の総和が元の数+1であれば、素数である
    if (cnt == 2) and (total == user_input + 1):
        print(f"\n{user_input}は素数です。")
    else:
        print(f"\n{user_input}は素数ではありません。")
        print(f"素因数分解の結果：{prime_text}")
        print(f"約数の個数：{cnt}")
        print(f"約数の総和：{total}")


if __name__ == "__main__":
    main()