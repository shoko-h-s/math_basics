import sympy

def i_integral():
    print("\n【不定積分】")
    var_str = input("変数を表す文字を入力（例: x, y, z）： ")
    symbol_var = sympy.Symbol(var_str)

    user_input = input(f"不定積分を行う関数式を入力（変数：{var_str}）： ")

    try:
        formula = sympy.sympify(user_input)
        answer = sympy.integrate(formula, symbol_var)

        print(f"\n計算結果：{answer} + C")

    except Exception as e:
        print(f"予期せぬエラーが発生しました：{e}")
        print("プログラムを終了します。")


def d_integral():
    print("\n【定積分】")
    var_str = input("変数を表す文字を入力（例: x, y, z）： ")
    symbol_var = sympy.Symbol(var_str)

    user_input = input(f"定積分を行う関数式を入力（変数：{var_str}）： ")
    a, b = map(sympy.sympify, input("値の始点と終点を半角スペース区切りで入力： ").split())

    try:
        formula = sympy.sympify(user_input)
        answer = sympy.integrate(formula, (symbol_var, a, b))

        print(f"\n計算結果：{answer}")

    except Exception as e:
        print(f"予期せぬエラーが発生しました：{e}")
        print("プログラムを終了します。")


def main():
    print()
    op = int(input("行う積分の種類を入力　　1：不定積分　2：定積分　　： "))

    if op == 1:
        i_integral()
    else:
        d_integral()


if __name__ == "__main__":
    main()
