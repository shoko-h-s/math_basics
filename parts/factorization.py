import sympy

def main():
    print("\n【因数分解】")
    user_input = input("因数分解を行う式を入力：")

    try:
        expr = sympy.sympify(user_input)
        answer = sympy.factor(expr)
        print(f"\n計算結果：{answer}")

    except (sympy.SympifyError, NameError):
        print("入力が数式として無効であるため、正しく演算を行えませんでした。プログラムを終了します。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました：{e}")
        print("プログラムを終了します。")

if __name__ == "__main__":
    main()