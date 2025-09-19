import statistics

def main():
    print("【基本統計量を求める】代表値（平均値、中央値、最頻値）")
    data = list(map(float, input("各値を半角スペース区切りで入力：").split()))

    mean_value = statistics.mean(data)
    median_value = statistics.median(data)
    mode_value = statistics.multimode(data)

    print("\n【代表値】")
    print(f"平均値：{mean_value}")
    print(f"中央値：{median_value}")
    print(f"最頻値：{mode_value}")


if __name__ == "__main__":
    main()