import sympy

def main():
    print("\n二次元ベクトル a, b の内積を求める")
    a_input_str = input("a の x 成分、y 成分を半角スペース区切りで入力（例: 4 sqrt(2)）： ").split()
    b_input_str = input("b の x 成分、y 成分を半角スペース区切りで入力（例: 3 1/3）： ").split()

    try:
        a1 = sympy.sympify(a_input_str[0])
        a2 = sympy.sympify(a_input_str[1])
        b1 = sympy.sympify(b_input_str[0])
        b2 = sympy.sympify(b_input_str[1])

        # SymPyのベクトル（Matrix）を作成
        a = sympy.Matrix([a1, a2])
        b = sympy.Matrix([b1, b2])

        # 内積（ドット積）を計算
        # SymPy の Matrix では、内積は転置行列との乗算として計算される
        dot_product = a.T * b

        # 結果は 1 x 1 の行列なので、要素を取り出す
        result = dot_product[0]

        print(f"\n【計算結果】a・b = {result}")

        # 必要に応じて、数値近似値も表示できる
        # print(f"（数値近似値: {result.evalf()}）")

    except (IndexError, sympy.SympifyError) as e:
        print(f"\n【エラー】入力形式が不正です: {e}")
        print("SymPyが解釈できる数学的な式（例: 4, sqrt(2), 1/2, 2*sqrt(3)）を入力してください。")

if __name__ == "__main__":
    main()