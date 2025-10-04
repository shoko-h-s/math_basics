import sympy


def main():
    print("\nベクトル a, b の大きさ・内積を求める")

    # 入力された成分の数 = ベクトルの次元
    a_input_str = input("ベクトル a の成分を半角スペース区切りで入力（例: 4 sqrt(2) 5）： ").split()
    b_input_str = input("ベクトル b の成分を半角スペース区切りで入力（例: 3 1/3 -1）： ").split()

    try:
        # ベクトルの次元を確認
        dim_a = len(a_input_str)
        dim_b = len(b_input_str)

        if dim_a == 0 or dim_b == 0:
            print("\n【エラー】ベクトル成分が入力されていません。")
            return

        if dim_a != dim_b:
            print(f"\n【エラー】ベクトルの次元が一致しません（a: {dim_a}次元, b: {dim_b}次元）。")
            print("内積を計算するには、同じ次元のベクトルを入力してください。")
            return

        # 各成分を SymPy の式に変換
        a_components = [sympy.sympify(comp) for comp in a_input_str]
        b_components = [sympy.sympify(comp) for comp in b_input_str]

        # SymPyのベクトル（Matrix）を作成
        # SymPyの Matrix はリストを渡すことで列ベクトル（N x 1行列）として作成される
        a = sympy.Matrix(a_components)
        b = sympy.Matrix(b_components)

        # 内積計算
        # SymPy の Matrix では、内積は転置行列との乗算として計算される
        dot_product = a.T * b
        # 結果は 1 x 1 の行列なので、要素を取り出す
        result = dot_product[0]

        # 大きさ計算（ノルム）
        a_magnitude = a.norm()
        b_magnitude = b.norm()

        print(f"\n【計算結果】")
        print(f"ベクトル a の大きさ： |a| = {a_magnitude}")
        print(f"ベクトル b の大きさ： |b| = {b_magnitude}")
        print(f"内積： a・b = {result}")

        # 必要に応じて、数値近似値も表示できる
        # print("\n【数値近似値】")
        # print(f"ベクトル a の大きさ： |a| ≈ {a_magnitude.evalf()}")
        # print(f"ベクトル b の大きさ： |b| ≈ {b_magnitude.evalf()}")
        # print(f"内積： a・b = {dot_result.evalf()}")

    except sympy.SympifyError as e:
        print(f"\n【エラー】入力形式が不正です。SymPyが解釈できる数学的な式（例: 4, sqrt(2), 1/2）を入力してください: {e}")
    except Exception as e:
        print(f"\n【エラー】予期せぬエラーが発生しました: {e}")


if __name__ == "__main__":
    main()