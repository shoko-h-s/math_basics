def base_10():
    try:
        base = int(input("変換元の進数を入力（～16進数まで対応可）： "))
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
        # print(f"\n【変換結果】{num}（{base}進数） →  {decimal_value}（10進数）")

    except ValueError:
        print("無効な入力です。正しい形式で入力してください。")
