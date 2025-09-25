import sympy

def main():
    print("\n【三角比の値を調べる】")
    op = int(input("角度の入力方式を選択　　1：度数法　2：弧度法（ラジアン）："))

    if op == 1:
        angle = int(input("三角比の値を調べる角度 θ を度数法で入力："))
        angle_rad = angle * (sympy.pi / 180)
        print(f"\nラジアンへの変換：{angle}° = {angle_rad}")
    else:
        angle_rad = input("三角比の値を調べる角度 θ を弧度法（ラジアン）で入力（π は pi に置き換えて入力）：")

    print(f"\nsin({angle_rad}) = {sympy.sin(angle_rad)}")
    print(f"cos({angle_rad}) = {sympy.cos(angle_rad)}")
    print(f"tan({angle_rad}) = {sympy.tan(angle_rad)}")

if __name__ == "__main__":
    main()