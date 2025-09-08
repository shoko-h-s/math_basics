import sympy

def main():
    while True:
        try:
            print("\n【方程式を解く】")

            # ユーザーに解く方程式の未知数の数を尋ねる
            num_input = input("解く方程式の未知数の数を入力してください (1～3): ")

            if num_input.strip() == '':
                print("入力が空です。プログラムを終了します。\n")
                return

            num_variables = int(num_input)
            if num_variables not in [1, 2, 3]:
                print("半角数字 1～3 で入力し直してください。")
                continue

            equations = []

            # 未知数の数に応じて、方程式の入力回数を制御
            for i in range(num_variables):
                # 未知数が1つの場合はメッセージを変更
                prompt = "方程式を入力してください（右辺を 0 とした状態で入力）: " if num_variables == 1 else f"方程式 {i + 1} を入力してください (右辺を 0 とした状態で入力): "
                eq_str = input(prompt)
                equations.append(eq_str)

            # 入力された文字列からSymPyの式オブジェクトに変換
            sym_equations = [sympy.sympify(eq) for eq in equations]

            # 自動で変数を検出
            variables_set = set()
            for eq in sym_equations:
                variables_set.update(eq.free_symbols)

            # 変数をソートしてリストに変換（アルファベット順など）
            variables = sorted(list(variables_set), key=lambda x: str(x))

            if len(variables) != num_variables:
                print(f"入力された方程式で検出された変数の数（{len(variables)}）が、指定した未知数の数（{num_variables}）と一致しません。")
                print("プログラムを終了します。")
                break

            # 方程式を解く
            solution = sympy.solve(sym_equations, variables)

            if solution:
                print("\n【解】")

                # 解がリストのリストまたは辞書形式で返されるため、形式を統一して表示
                if isinstance(solution, list) and all(isinstance(s, dict) for s in solution):
                    for sol_dict in solution:
                        for var in variables:
                            print(f"{var} = {sol_dict[var]}", end=" ")
                        print()

                elif isinstance(solution, dict):
                    for var in variables:
                        print(f"{var} = {solution[var]}")

                else:
                    # 未知数が1つの場合の戻り値形式に対応
                    for var, val in zip(variables, solution):
                        print(f"{var} = {val}")
            else:
                print("解は見つかりませんでした。")
            break

        except (ValueError, sympy.SympifyError):
            print("入力が数式として無効であるため、正しく演算を行えませんでした。プログラムを終了します。")
            break

if __name__ == "__main__":
    main()