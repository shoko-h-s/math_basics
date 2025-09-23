import sympy

def main():
    print("\n【多項式の割り算】")
    f = input("割られる式を入力：")
    g = input("割る式を入力：")

    answer_fg, mod_fg = sympy.div(f, g)

    print(f"商：{answer_fg}、 あまり：{mod_fg}")

if __name__ == "__main__":
    main()