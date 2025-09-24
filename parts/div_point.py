import sympy

def main():
    print("\n座標上の2点 A, B を結ぶ線分 AB を分割する点を求める")
    op = input("P：内分点　M：中点　Q：外分点　　求める点を半角英字で入力：")

    if op not in ["P", "p", "M", "m", "Q", "q"]:
        print("【エラー】無効な選択肢です。プログラムを終了します。")
        return

    x1, y1 = map(sympy.sympify, input("A の x 座標, y 座標を、半角スペース区切りで入力：").split())
    x2, y2 = map(sympy.sympify, input("B の x 座標, y 座標を、半角スペース区切りで入力：").split())

    # 内分点
    if (op == "P") or (op == "p"):
        m, n = map(sympy.sympify, input("内分比率 m:n を、半角スペース区切りで入力：").split())

        px = (n * x1 + m * x2) / (m + n)
        py = (n * y1 + m * y2) / (m + n)
        simplified_px = sympy.simplify(px)
        simplified_py = sympy.simplify(py)

        print(f"\n内分点 P の座標は、({simplified_px}, {simplified_py})")

    # 中点
    elif (op == "M") or (op == "m"):

        mx = sympy.simplify((x1 + x2) / 2)
        my = sympy.simplify((y1 + y2) / 2)

        slope = sympy.simplify((y2 - y1) / (x2 - x1))
        vertical_slope = -1 / slope
        b = my - vertical_slope * mx

        if b > 0:
            b_str = " + " + str(b)
        elif b == 0:
            b_str = ""
        else:
            b_str = " - " + str(-b)

        answer = f"y = {vertical_slope}x{b_str}"

        print(f"\n中点 M の座標は ({mx}, {my})")
        print(f"線分 AB の垂直二等分線は、{answer}")

    # 外分点
    elif (op == "Q") or (op == "q"):
        m, n = map(sympy.sympify, input("外分比率 m:n を、半角スペース区切りで入力：").split())

        qx = (-n * x1 + m * x2) / (m - n)
        qy = (-n * y1 + m * y2) / (m - n)
        simplified_qx = sympy.simplify(qx)
        simplified_qy = sympy.simplify(qy)

        print(f"\n外分点 Q の座標は、({simplified_qx}, {simplified_qy})")


if __name__ == "__main__":
    main()