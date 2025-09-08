import sympy

def main():
    print("\n【多項式の展開】")
    formula = input("展開する式を入力（ √2 は、sqrt(2) のように表記すること）：")

    try:
        answer = sympy.expand(formula)
        print(f"\n計算結果：{answer}")

    except Exception as e:
        print(f"予期せぬエラーが発生しました：{e}")
        print("プログラムを終了します。")

if __name__ == "__main__":
    main()