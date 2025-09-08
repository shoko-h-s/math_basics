import sympy

def main():
    print("\n【基礎的な数学計算】")
    user_input = input("計算式を入力（ √2 は、sqrt(2) のように表記すること）：")

    try:
        # 入力された文字列を sympy の数式に変換
        expression = sympy.sympify(user_input)

        # 数式を単純化するメソッド
        answer = sympy.simplify(expression)

        print(f"\n計算結果：{answer}")

    # sympy.SympifyError：入力が数式として無効な場合に発生
    # NameError：未定義の変数（例：a - b）が入力された場合に発生する
    except (sympy.SympifyError, NameError):
        print("入力が数式として無効であるため、正しく演算を行えませんでした。プログラムを終了します。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました：{e}")
        print("プログラムを終了します。")

if __name__ == "__main__":
    main()