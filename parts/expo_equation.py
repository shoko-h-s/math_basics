import sympy

def main():
    print("\n【指数方程式を解く】方程式を左辺, 右辺に分けてそれぞれ入力（入力例：sqrt(2)**x）")
    left_side_str = input("方程式の左辺を入力： ")
    right_side_str = input("方程式の右辺を入力： ")

    try:
        left_side = sympy.sympify(left_side_str)
        right_side = sympy.sympify(right_side_str)

        # 方程式を「左辺 - 右辺 = 0」の形に変換
        equation = left_side - right_side

        all_solutions = sympy.solve(equation)

        # 実数解のみを抽出
        real_solutions = [sol for sol in all_solutions if sol.is_real]

        print(f"\nx = {real_solutions}")

    except Exception as e:
        print("\n入力された式を解析できませんでした。プログラムを終了します。")


if __name__ == "__main__":
    main()