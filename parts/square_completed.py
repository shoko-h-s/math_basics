import sympy
from fractions import Fraction

def main():
    print("\n【平方完成】")
    print("y = ax^2 + bx + c を、グラフを書きやすい形に変形する。")

    try:
        # 入力をeval()で評価し、分数にも対応
        a_str, b_str, c_str = input("a, b, c の値を、半角スペース区切りで入力（分数可）：").split()
        a = Fraction(a_str)
        b = Fraction(b_str)
        c = Fraction(c_str)

        # a, b, cを sympy.Rational に変換して正確に計算
        a_rational = sympy.Rational(a)
        b_rational = sympy.Rational(b)
        c_rational = sympy.Rational(c)

        # 傾きを求める
        if a_rational == 1:
            slope = ""
        elif a_rational == -1:
            slope = "-"
        else:
            slope = a_rational

        # 頂点の x 座標を求める
        x_coordinate = -b_rational / (2 * a_rational)

        # 求めた x 座標を代入し、頂点の y 座標を求める
        y_coordinate = a_rational * x_coordinate ** 2 + b_rational * x_coordinate + c_rational

        # 出力の整形
        if x_coordinate.is_zero:
            x_coordinate_str = "x^2"
        elif x_coordinate > 0:
            x_coordinate_str = f"(x - {x_coordinate})^2"
        else:
            x_coordinate_str = f"(x + {-x_coordinate})^2"

        if y_coordinate.is_zero:
            y_coordinate_str = ""
        elif y_coordinate > 0:
            y_coordinate_str = f" + {y_coordinate}"
        else:
            y_coordinate_str = f" - {-y_coordinate}"

        print(f"平方完成を行うと、y = {slope}{x_coordinate_str}{y_coordinate_str}")
        print(f"このグラフの頂点の座標は ({x_coordinate}, {y_coordinate})")

    except ZeroDivisionError:
        print("a に 0 は入力できません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        print("プログラムを終了します。")


if __name__ == "__main__":
    main()