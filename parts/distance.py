import sympy

def main():
    print("\n【2点 A, B 間の距離を求める】")
    a, b = map(int, input("A の x 座標, y 座標を、半角スペース区切りで入力：").split())
    c, d = map(int, input("B の x 座標, y 座標を、半角スペース区切りで入力：").split())

    tmp = (c - a)**2 + (d - b)**2
    answer = sympy.sqrt(tmp)

    print(f"\n計算結果：{answer}")

if __name__ == "__main__":
    main()