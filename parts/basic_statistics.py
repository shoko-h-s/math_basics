import statistics

def main():
    print("\n【基本統計量を求める】データ群の代表値、散布度を求める")

    try:
        data = list(map(float, input("データ群の各値を半角スペース区切りで入力：").split()))

    except ValueError:
        print("\n【エラー】入力内容が正しくありません。プログラムを終了します。")
        return

    # 代表値
    mean_value = statistics.mean(data)
    median_value = statistics.median(data)
    mode_value = statistics.multimode(data)
    min_value = min(data)
    max_value = max(data)


    # 散布度
    # 範囲（レンジ）
    range_value = max_value - min_value

    # 各値の偏差
    deviation_list = [d - mean_value for d in data]

    # 偏差2乗和
    sum_sd = 0

    for d in deviation_list:
        sum_sd += d ** 2

    # 分散
    var_value = sum_sd / len(data)

    # 標準偏差
    std = var_value ** 0.5

    print("\n【代表値】")
    print(f"平均値：{mean_value}")
    print(f"中央値：{median_value}")
    print(f"最頻値：{mode_value}")
    print(f"最小値：{min_value}")
    print(f"最大値：{max_value}")

    print("\n【散布度】")
    print(f"範囲（レンジ）：{range_value}")
    print(f"偏差2乗和：{sum_sd}")
    print(f"分散：{var_value}")
    print(f"標準偏差：{std}")


if __name__ == "__main__":
    main()