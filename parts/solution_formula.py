import sympy

def main():
    print("\n二次方程式 ax^2 + bx + c = 0 の実数解の個数を調べる。")

    try:
        a_str, b_str, c_str = input("a, b, c の値を、半角スペース区切りで入力（分数可）：").split()

        a = sympy.Rational(a_str)
        b = sympy.Rational(b_str)
        c = sympy.Rational(c_str)

        # 判別式
        d = b ** 2 - 4 * a * c

        x1 = (-b + sympy.sqrt(d)) / (2 * a)
        x2 = (-b - sympy.sqrt(d)) / (2 * a)

        if d > 0:
            print("\nこの方程式は、実数解を 2 つ持つ。")
            print(f"【計算結果】x = {x1}, {x2}")

        elif d == 0:
            print("\nこの方程式は、実数解を 1 つ持つ（重解となる）。")
            print(f"【計算結果】x = {x1}")
        else:
            print("この方程式は、実数解を持たない。")

    except ValueError:
        print(f"入力内容が正しくありません。プログラムを終了します。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")
        print("プログラムを終了します。")

if __name__ == "__main__":
    main()