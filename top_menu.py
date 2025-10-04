from parts import expand
from parts import gcd_lcm
from parts import equation
from parts import factorization
from parts import prime_factorization
from parts import distance
from parts import solution_formula
from parts import square_completed
from parts import basic_statistics
from parts import fd_table
from parts import fpc
from parts import base_change
from parts import poly_div
from parts import div_point
from parts import triangle
from parts import tri_ratio
from parts import tri_equation
from parts import expo_equation
from parts import integrate
from parts import vector
from parts import probability

# キーはオプション番号、値は実行する関数または処理のタプル
math_tools = {
    1: ("基礎的な数学計算", expand.main),
    2: ("最大公約数・最小公倍数を求める", gcd_lcm.main),
    3: ("方程式を解く", equation.main),
    4: ("因数分解", factorization.main),
    5: ("素数判定と素因数分解", prime_factorization.main),
    6: ("二次方程式の解の公式", solution_formula.main),
    7: ("平方完成", square_completed.main),
    8: ("基本統計量を求める", basic_statistics.main),
    9: ("度数分布表から基本統計量を求める", fd_table.main),
    10: ("階乗（!）", fpc.factorial),
    11: ("順列（P）", fpc.perm),
    12: ("組み合わせ（C）", fpc.comb),
    13: ("重複組み合わせ（H）", fpc.h_comb),
    14: ("10進数 → M進数変換", base_change.base_m),
    15: ("M進数 → 10進数変換", base_change.base_10),
    16: ("M進数での四則演算", base_change.base_m_calc),
    17: ("多項式の割り算", poly_div.main),
    18: ("平面上の内分点・中点・外分点を求める", div_point.main),
    19: ("2点間の距離を求める", distance.p2),
    20: ("点と直線の距離を求める", distance.pl),
    21: ('平行な2直線間の距離', distance.ll),
    22: ("三角形の形状・面積を調べる", triangle.main),
    23: ("三角形の重心を求める", triangle.gravity_point),
    24: ("三角比の値を調べる", tri_ratio.main),
    25: ("三角方程式を解く", tri_equation.main),
    26: ("指数方程式・対数方程式を解く", expo_equation.main),
    27: ("積分を行う", integrate.main),
    28: ("2つのベクトルを成分から分析", vector.main),
    29: ("確率分布表を用いた分析", probability.main)
}

# メイン処理: ユーザーからオプション番号を選択させる
def menu_select():
    print("\n【数学計算ツール】")
    print("-----------------------------------------------------------------------------------------------------")
    # 辞書から動的にメニューを生成、4 個ごとに改行
    for key, value in math_tools.items():
        print(f"{key}：{value[0]}", end="　" if key % 4 != 0 else "\n")

    # 最後に改行が欠ける場合があるため、補完
    if len(math_tools) % 4 != 0:
        print()

    print("-----------------------------------------------------------------------------------------------------")

    # 正しいコードが入力されるまで、再入力を求め続ける
    while True:
        try:
            op_to_run = int(input("行う処理の番号を、上記のメニューより選んで入力："))
            if op_to_run in math_tools:
                return op_to_run
            else:
                print("その入力は無効です。正しい番号を半角数字で入力してください。")
                print("------------------------------------------------------------------------------")
        except ValueError:
            print("その入力は無効です。正しい番号を半角数字で入力してください。")
            print("------------------------------------------------------------------------------")


# プログラムの実行を管理する
def main():
    op_to_run = None
    while True:
        if op_to_run is None:
            op_to_run = menu_select()

        # 辞書から対応する関数を取得し、実行
        math_tools[op_to_run][1]()

        while True:
            # ユーザーに次の操作を尋ねる
            print("\n1: 値を変更して同じ処理を再度繰り返す　2: メニューに戻る　3: プログラムを終了する")

            try:
                answer = int(input("次に行う操作を選択してください："))
                # 同じ処理を再実行するために外側のループを継続
                if answer == 1:
                    break

                # 最初のメニューに戻るために op_to_run をリセット
                elif answer == 2:
                    op_to_run = None
                    break

                elif answer == 3:
                    print("\nSee you again!")
                    return  # プログラムを終了

                else:
                    print("その入力は無効です。半角数字 1～3 で入力してください。")
            except ValueError:
                print("その入力は無効です。半角数字 1～3 で入力してください。")


if __name__ == "__main__":
    main()