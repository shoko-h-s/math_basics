from fractions import Fraction

def main():
    print("\n座標上の2点 A, B を結ぶ線分 AB を分割する点を求める")
    op = input("P：内分点　M：中点　Q：外分点　　求める点を半角英字で入力：")
    x1, y1 = map(int, input("A の x 座標, y 座標を、半角スペース区切りで入力：").split())
    x2, y2 = map(int, input("B の x 座標, y 座標を、半角スペース区切りで入力：").split())

    # 内分点
    if (op == "P") or (op == "p"):
        m, n = map(int, input("内分比率 m:n を、半角スペース区切りで入力：").split())

        px = Fraction(n * x1 + m * x2, m + n)
        py = Fraction(n * y1 + m * y2, m + n)

        print(f"\n内分点 P の座標は、({px}, {py})")

    # 中点
    elif (op == "M") or (op == "m"):
        mx = Fraction(x1 + x2, 2)
        my = Fraction(y1 + y2, 2)

        # mx = (x1 + x2) / 2
        # my = (y1 + y2) / 2

        print(f"\n中点 M の座標は、({mx}, {my})")

    # 外分点
    elif (op == "Q") or (op == "q"):
        m, n = map(int, input("外分比率 m:n を、半角スペース区切りで入力：").split())

        qx = Fraction(-n * x1 + m * x2, m - n)
        qy = Fraction(-n * y1 + m * y2, m - n)

        print(f"\n外分点 Q の座標は、({qx}, {qy})")

    else:
        print("【エラー】無効な選択肢です。プログラムを終了します。")


if __name__ == "__main__":
    main()