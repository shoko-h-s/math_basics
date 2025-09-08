# 最大公約数
# ユークリッドの互除法を再帰的に実装
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# 最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

def main():
    while True:
        try:
            print("\n【最大公約数・最小公倍数を求める】")
            user_input = input("最大公約数・最小公倍数を求めたい2数を、半角スペース区切りで入力：")
            nums = user_input.split()

            # 入力された数が2つでない場合、ValueError を発生させる
            if len(nums) != 2:
                raise ValueError("入力は2つの数である必要があります。")

            a = int(nums[0])
            b = int(nums[1])

            # 負の値・0が入力された場合を考慮し、絶対値に変換する
            a_abs = abs(a)
            b_abs = abs(b)

            print()
            print(f"最大公約数：{gcd(a_abs, b_abs)}")
            print(f"最小公倍数：{lcm(a_abs, b_abs)}")

            break

        except ValueError as e:
            print("入力を2つの数値として認識できなかったため、正しく演算を行えませんでした。プログラムを終了します。")
            break

        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")
            print("プログラムを終了します。")
            break

if __name__ == "__main__":
    main()