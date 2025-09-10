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

            try:
                num_variables = int(num_input)

                if num_variables not in [1, 2, 3]:
                    # ValueErrorを意図的に発生させて、まとめて捕捉
                    raise ValueError

            except ValueError:
                print("入力内容が正しくありません。半角数字 1～3 で入力し直してください。")
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

                if isinstance(solution, list):
                    # 複数解がリストのリストで返されるケース（単一未知数）
                    if all(isinstance(s, (tuple, list)) for s in solution):

                        # 各タプル/リストから値を取り出し、リストに格納
                        flat_solutions = [s[0] for s in solution]
                        print(f"{variables[0]} = {', '.join(map(str, flat_solutions))}")

                    # 複数解がリストで返されるケース（単一未知数）
                    elif all(not isinstance(s, (tuple, list, dict)) for s in solution):
                        print(f"{variables[0]} = {', '.join(map(str, solution))}")

                    # 複数解が辞書形式のリストで返されるケース（複数未知数）
                    else:
                        for sol_dict in solution:
                            solution_str = ", ".join(f"{var} = {sol_dict[var]}" for var in variables)
                            print(solution_str)

                elif isinstance(solution, dict):
                    solution_str = ", ".join(f"{var} = {solution[var]}" for var in variables)
                    print(solution_str)

            else:
                print("解は見つかりませんでした。")
            break

        except (ValueError, sympy.SympifyError):
            print("入力が数式として無効であるため、正しく演算を行えませんでした。")
            print("プログラムを終了します。")
            break

if __name__ == "__main__":
    main()