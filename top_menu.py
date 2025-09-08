from parts import calculator
from parts import gcd_lcm
from parts import equation
from parts import factorization
from parts import prime_factorization

# キーはオプション番号、値は実行する関数または処理のタプル
math_tools = {
    1: ("基礎的な数学計算", calculator.main),
    2: ("最大公約数・最小公倍数を求める", gcd_lcm.main),
    3: ("方程式を解く", equation.main),
    4: ("因数分解", factorization.main),
    5: ("素因数分解", prime_factorization.main)
}

# メイン処理: ユーザーからオプション番号を選択させる
def menu_select():
    print("【数学計算ツール】")
    print("-----------------------------------------------------------------------------------")
    # 辞書から動的にメニューを生成、5個ごとに改行
    for key, value in math_tools.items():
        print(f"{key}：{value[0]}", end="　" if key % 5 != 0 else "\n")

    # 最後に改行が欠ける場合があるため、補完
    if len(math_tools) % 5 != 0:
        print()

    print("-----------------------------------------------------------------------------------")

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
            print("\n1: 同じ処理を再度繰り返す　2: メニューに戻る　3: プログラムを終了する")

            try:
                answer = int(input("次に行う操作を選択してください："))
                # 同じ処理を再実行するために外側のループを継続
                if answer == 1:
                    # print()
                    break

                # 最初のメニューに戻るために op_to_run をリセット
                elif answer == 2:
                    print()
                    op_to_run = None
                    break

                elif answer == 3:
                    print()
                    print("See you again!")
                    return  # プログラムを終了

                else:
                    print("その入力は無効です。半角数字 1～3 で入力してください。")
            except ValueError:
                print("その入力は無効です。半角数字 1～3 で入力してください。")


if __name__ == "__main__":
    main()