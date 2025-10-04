import sympy


def main():
    print("\n【確率分布表を用いた分析】")
    x_list = list(map(sympy.sympify, input("それぞれの確率変数 X を半角スペース区切りで入力： ").split()))
    p_list = list(map(sympy.sympify, input("それぞれの確率 P を半角スペース区切りで入力： ").split()))

    try:
        # データ数の一致確認
        num_x = len(x_list)
        num_p = len(p_list)

        if (num_x == 0) or (num_p == 0):
            print("\n【エラー】データが入力されていません。プログラムを終了します。")
            return

        if num_x != num_p:
            print(f"\n【エラー】入力されたデータ数が一致しません（確認変数 X: {num_x}, 確率 P: {num_p}）。")
            print("プログラムを終了します。")
            return

        # 確率が正しく入力されているか確認
        p_sum = sum(p_list)

        if p_sum != sympy.Integer(1):
            print(f"\n【エラー】確率 P の合計が 1 になりません。合計値: {p_sum} (期待値 {p_sum.evalf()})")
            print("プログラムを終了します。")
            return

        # 期待値
        m = 0

        for i in range(num_x):
            m += x_list[i] * p_list[i]

        print("\n【分析結果】")
        print(f"期待値： m = {m}")

        # if isinstance(m, sympy.Rational):
        #     print(f"（分数形式: {m.p}/{m.q}）")

        # 分散・標準偏差
        v = 0

        for j in range(num_x):
            v += p_list[j] * (x_list[j] - m) ** 2

        print(f"分散： v = {v}")
        print(f"標準偏差： σ = {sympy.sqrt(v)}")

    except sympy.SympifyError as e:
        print(f"\n【エラー】入力形式が不正です。SymPyが解釈できる数学的な式（例: 4, sqrt(2), 1/2）を入力してください: {e}")
    except Exception as e:
        print(f"\n【エラー】予期せぬエラーが発生しました: {e}")


if __name__ == "__main__":
    main()