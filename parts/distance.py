import sympy

def p2():
    print("\n【2点 A, B 間の距離を求める】")
    a, b = map(int, input("A の x 座標, y 座標を、半角スペース区切りで入力：").split())
    c, d = map(int, input("B の x 座標, y 座標を、半角スペース区切りで入力：").split())

    tmp = (c - a)**2 + (d - b)**2
    answer = sympy.sqrt(tmp)

    print(f"\n計算結果：{answer}")


def pl():
    print("\n点(x0, y0) と、直線ax + by + c = 0 の距離を求める")

    # 入力値をシンボリックな表現で扱う
    x0, y0 = map(sympy.sympify, input("点の x 座標, y 座標を、半角スペース区切りで入力：").split())
    a, b, c = map(sympy.sympify, input("a, b, c の値を、半角スペース区切りで入力：").split())

    num1 = abs(a * x0 + b * y0 + c)
    num2 = sympy.sqrt(a**2 + b**2)

    # 無理数はそのままの形で保持される
    answer = num1 / num2

    simplified_answer = sympy.simplify(answer)

    print(f"\n計算結果：{simplified_answer}")

    # 浮動小数点数での近似値が必要な場合用
    # print(f"近似値: {simplified_answer.evalf()}")


def ll():
    print("\n平行な2直線 ax + by + c = 0 と ax + by + d = 0 の距離を求める")
    a, b, c, d = map(sympy.sympify, input("a, b, c, d の値を、半角スペース区切りで入力：").split())

    num1 = abs(d - c)
    num2 = sympy.sqrt(a**2 + b**2)

    answer = num1 / num2
    simplified_answer = sympy.simplify(answer)

    print(f"\n計算結果：{simplified_answer}")
