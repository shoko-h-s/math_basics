import sympy

def main():
    print("\n確率変数 X が二項分布 B(n, p) に従うときの分析")

    # ユーザー入力が正しいか検証
    while True:
        try:
            n, p = map(sympy.sympify, input("n, p の値を半角スペース区切りで入力： ").split())

            # 検証用に、具体的な数値としても扱えるようにする
            n_val = float(n)
            p_val = float(p)

            if not n_val.is_integer() or n_val <= 0:
                raise ValueError("\n【エラー】試行回数 n は正の整数で指定してください。")

            if not (0 <= p_val <= 1):
                raise ValueError("\n【エラー】 成功確率 p は 0 ～ 1 の範囲で指定してください。")

            # すべての検証を通過したらループを抜ける
            break

        except (ValueError, IndexError) as e:
            print(f"入力エラー: {e}")

        except Exception as e:
            print(f"予期せぬエラーが発生しました: {e}")

    # 事象が起こらない確率
    q = 1 - p

    # 期待値・分散・標準偏差を計算
    e = n * p
    v = n * p * q
    s = sympy.sqrt(v)

    print("\n【分析結果】")
    print(f"\n期待値： {e}")
    print(f"分散： {v}")
    print(f"標準偏差： {s}")

if __name__ == "__main__":
    main()