import sympy

def main():
    print("\n【基礎的な数学計算】")
    print("このプログラムでは加減乗除・分数の計算・有理化・多項式の展開が行えます。")
    print("√2 は、sqrt(2) のように表記してください。")
    user_input = input("計算式を入力してください：")

    try:
        answer = sympy.expand(user_input)
        print(f"\n計算結果：{answer}")

    except Exception as e:
        print(f"予期せぬエラーが発生しました：{e}")
        print("プログラムを終了します。")

if __name__ == "__main__":
    main()