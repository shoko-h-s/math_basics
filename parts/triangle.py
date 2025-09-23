from fractions import Fraction

def gravity_point():
    print("\n△ABC の重心 G の座標を求める")
    x1, y1 = map(int, input("A の x 座標, y 座標を、半角スペース区切りで入力：").split())
    x2, y2 = map(int, input("B の x 座標, y 座標を、半角スペース区切りで入力：").split())
    x3, y3 = map(int, input("C の x 座標, y 座標を、半角スペース区切りで入力：").split())

    gx = Fraction(x1 + x2 + x3, 3)
    gy = Fraction(y1 + y2 + y3, 3)

    print(f"\n重心 G の座標は、({gx}, {gy})")