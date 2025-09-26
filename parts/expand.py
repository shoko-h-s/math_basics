import sympy

def main():
    print("\n【基礎的な数学計算】このプログラムでは簡単な数学演算（加減乗除・分数の計算・有理化・多項式の展開等）が行えます。")
    print("\n計算式を入力する際は、以下の入力例を参考にしてください。")
    print("無理数：√2 → sqrt(2)")
    print("対数：log 2 4 → log(4,2)\n")

    user_input = input("計算式を入力： ")

    try:
        expr = sympy.sympify(user_input)

        # 多項式の展開
        expanded_expr = sympy.expand(expr)

        # 展開した結果を simplify でさらに簡略化
        answer = sympy.simplify(expanded_expr)

        print(f"\n計算結果：{answer}")

    except Exception as e:
        print(f"予期せぬエラーが発生しました：{e}")
        print("プログラムを終了します。")

if __name__ == "__main__":
    main()