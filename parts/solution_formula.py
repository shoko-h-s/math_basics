import sympy

def main():
    print("\n【二次方程式 ax^2 + bx + c = 0 の解の公式】")

    try:
        a, b, c = map(int, input("a, b, c の値を、半角スペース区切りで入力：").split())

        # 判別式
        d = b ** 2 - 4 * a * c

        x1 = (-b + sympy.sqrt(d)) / (2 * a)
        x2 = (-b - sympy.sqrt(d)) / (2 * a)

        print(f"\n【計算結果】x = {x1}, {x2}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        print("プログラムを終了します。")

if __name__ == "__main__":
    main()