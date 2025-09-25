import sympy

def main():
    print("\n【三角方程式を解く】")
    left_side_str = input("方程式の左辺を入力 (例: cos(3*x)): ")
    right_side_str = input("方程式の右辺を入力 (例: 1/sqrt(2)): ")

    x = sympy.Symbol("x")

    try:
        left_side = sympy.sympify(left_side_str)
        right_side = sympy.sympify(right_side_str)

        # 方程式を「左辺 - 右辺 = 0」の形に変換
        equation = left_side - right_side

        # 解の範囲を定義
        domain_interval = sympy.Interval(0, sympy.pi, right_open=True)

        # solvesetで実数解の集合を求め、domain_intervalとの共通部分を計算
        solutions = sympy.solveset(equation, x, domain=sympy.Reals).intersection(domain_interval)
        # solutions = sympy.solve(equation)

        print(f"\n解：{solutions}")

    except Exception as e:
        print("\n入力された式を解析できませんでした。プログラムを終了します。")


if __name__ == "__main__":
    main()