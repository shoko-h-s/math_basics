import sympy


def main():
    while True:
        try:
            print("\n【方程式を解く】")

            # ユーザーに解く方程式の未知数の数を尋ねる
            num_input = input("解く方程式の未知数の数を入力： ")

            if num_input.strip() == '':
                print("入力が空です。プログラムを終了します。\n")
                return

            try:
                num_variables = int(num_input)

                if num_variables <= 0:
                    # ValueErrorを意図的に発生させて、まとめて捕捉
                    raise ValueError

            except ValueError:
                print("入力内容が正しくありません。1 以上の半角数字で入力し直してください。")
                continue

            equations = []
            all_symbols = set()

            # 未知数の数に応じて、方程式の入力回数を制御
            for i in range(num_variables):
                # 未知数が1つの場合はメッセージを変更
                prompt = "方程式の情報を入力\n左辺： " if num_variables == 1 else f"方程式 {i + 1} の情報を入力\n左辺： "
                left_side_str = input(prompt)
                right_side_str = input("右辺： ")
                print()

                # 入力が空の場合はループを抜ける
                if not left_side_str.strip() or not right_side_str.strip():
                    print("入力が空です。プログラムを終了します。\n")
                    return

                try:
                    # 入力された文字列からSymPyの式オブジェクトに変換
                    left_side = sympy.sympify(left_side_str)
                    right_side = sympy.sympify(right_side_str)

                    # 方程式を「左辺 - 右辺 = 0」の形に変換
                    equation = left_side - right_side
                    equations.append(equation)

                    # 変数を収集
                    all_symbols.update(equation.free_symbols)

                except sympy.SympifyError:
                    print("入力が数式として無効です。プログラムを終了します。\n")
                    return

            # 変数をソートしてリストに変換（アルファベット順など）
            variables = sorted(list(all_symbols), key=lambda x: str(x))

            # 検出された変数の数が指定した未知数の数と一致するか確認
            if len(variables) != num_variables:
                print(
                    f"入力された方程式で検出された変数の数（{len(variables)}）が、指定した未知数の数（{num_variables}）と一致しません。")
                print("プログラムを終了します。")
                break

            # 方程式を解く
            solution = sympy.solve(equations, variables)

            if solution:
                print("【解】")

                # 解が辞書形式のリスト（複数未知数の複数解）で返された場合
                if isinstance(solution, list) and all(isinstance(s, dict) for s in solution):
                    for sol_dict in solution:
                        solution_str = ", ".join(f"{var} = {sol_dict[var]}" for var in variables)
                        print(solution_str)

                # 解がタプルのリスト（複数未知数の複数解）で返された場合
                elif isinstance(solution, list) and all(isinstance(s, (tuple, list)) for s in solution):
                    for sol_tuple in solution:
                        # 変数名と解の値を zip で組み合わせて文字列を生成
                        solution_str = ", ".join(f"{var} = {val}" for var, val in zip(variables, sol_tuple))
                        print(solution_str)

                # 解が単一の辞書で返された場合（複数未知数の単一解）
                elif isinstance(solution, dict):
                    solution_str = ", ".join(f"{var} = {solution[var]}" for var in variables)
                    print(solution_str)

                # その他の単一未知数の複数解
                elif isinstance(solution, list):
                    # リスト内の要素がさらにタプル/リストの場合（例: [[x1], [x2], ...]）
                    if all(isinstance(s, (tuple, list)) for s in solution):
                        flat_solutions = [s[0] for s in solution]
                        print(f"{variables[0]} = {', '.join(map(str, flat_solutions))}")
                    # リスト内の要素が直接解の値の場合（例: [x1, x2, ...]）
                    else:
                        print(f"{variables[0]} = {', '.join(map(str, solution))}")

            else:
                print("解は見つかりませんでした。")

            # 成功した場合はループを抜ける
            break

        except (ValueError, sympy.SympifyError):
            print("入力が数式として無効であるため、正しく演算を行えませんでした。")
            print("プログラムを終了します。")
            break
        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")
            print("プログラムを終了します。")
            break


if __name__ == '__main__':
    main()