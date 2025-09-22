def base_10():
    try:
        base = int(input("\n変換元の進数を入力（～16進数に対応可）： "))
        num = input("10進数に変換する値を入力：")

        # 入力値に小数部が含まれるか確認
        if '.' in num:
            integer_part, fractional_part = num.split('.')

            # 整数部の処理
            decimal_value = 0
            for i, digit in enumerate(reversed(integer_part.lower())):
                decimal_value += int(digit, base) * (base ** i)

            # 小数部の処理
            for i, digit in enumerate(fractional_part.lower()):
                decimal_value += int(digit, base) * (base ** -(i + 1))

        else:
            # 小数部がない場合は従来の処理
            decimal_value = int(num, base)

        print(f"\n10進数への変換結果：{decimal_value}")
        print(f"変換前の数：{num}（{base}進数）")

    except ValueError:
        print("無効な入力です。正しい形式で入力してください。")


def base_m():
    try:
        base = int(input("\n変換先の進数を入力（～9進数、および16進数に対応可）： "))
        num_str = input("変換する値を入力：")

        if '.' in num_str:
            integer_part_str, fractional_part_str = num_str.split('.')

            # 整数部の変換
            integer_part_dec = int(integer_part_str)
            if integer_part_dec == 0:
                integer_converted = "0"
            else:
                integer_converted = ""
                if base == 16:
                    integer_converted = hex(integer_part_dec).upper()[2:]
                elif 2 <= base <= 9:
                    while integer_part_dec > 0:
                        integer_converted += str(integer_part_dec % base)
                        integer_part_dec //= base
                    integer_converted = integer_converted[::-1]
                else:
                    print("対応外の進数です。プログラムを終了します。")
                    return

            # 小数部の変換
            fractional_part_dec = float("0." + fractional_part_str)
            fractional_converted = ""
            if 2 <= base <= 9 or base == 16:
                for _ in range(10):  # 精度を上げるため、10回繰り返す
                    fractional_part_dec *= base
                    integer_part = int(fractional_part_dec)
                    if base == 16:
                        fractional_converted += hex(integer_part)[2:].upper()
                    else:
                        fractional_converted += str(integer_part)
                    fractional_part_dec -= integer_part
                    if fractional_part_dec == 0:
                        break

            answer = str(integer_converted) + "." + str(fractional_converted)

            # 整数部と小数部を結合して表示
            # print(f"{integer_converted}.{fractional_converted}")

        else:
            # 小数部がない場合は従来の処理
            num = int(num_str)

            if base == 16:
                ans = hex(num).upper()
                answer = ans[2:]
                # print(ans[2:])

            elif 2 <= base <= 9:
                ans = ""
                while num > 0:
                    ans += str(num % base)
                    num //= base
                answer = ans[::-1]
                # print(answer)
            else:
                print("対応外の進数です。プログラムを終了します。")

        print(f"\n{base}進数への変換結果：{answer}")
        print(f"変換前の数：{num_str}（10進数）")


    except ValueError:
        print("無効な入力です。正しい形式で入力してください。")


