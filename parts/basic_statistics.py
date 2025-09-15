import statistics

def main():
    print("【基本統計量を求める】代表値（平均値、中央値、最頻値）")
    print("\nデータの入力形式を選択してください。")
    op = int(input("1：すべての要素を直接入力　2：度数分布表のデータを入力："))


    if op == 1:
        data = list(map(float, input("各値を半角スペース区切りで入力：").split()))
        mean_value = statistics.mean(data)
        median_value = statistics.median(data)
        mode_value = statistics.multimode(data)


    elif op == 2:
        class_value = list(map(float, input("\n階級値を半角スペース区切りで入力：").split()))
        frequency = list(map(int, input("度数を階級値に対応した順番で、半角スペース区切りで入力：").split()))

        num = sum(frequency)

        # 平均値
        total = 0

        for i in range(len(class_value)):
            total += class_value[i] * frequency[i]

        mean_value = total / num

        # 中央値
        median_point = num // 2
        data = []

        for i in range(len(class_value)):
            for j in range(frequency[i]):
                data.append(class_value[i])

            if len(data) > median_point:
                median_value = class_value[i]
                break

            # データが偶数かつ中央の2つの値の階級値が異なる場合
            if len(data) == median_point:
                median_value = (class_value[i] + class_value[i+1])/2
                break

        # 最頻値
        max_class_value = max(frequency)
        max_index = frequency.index(max_class_value)
        mode_value = class_value[max_index]


    print("\n【代表値】")
    print(f"平均値：{mean_value}")
    print(f"中央値：{median_value}")
    print(f"最頻値：{mode_value}")


if __name__ == "__main__":
    main()