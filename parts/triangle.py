import sympy
from fractions import Fraction

def main():
    op = int(input("\n解く三角形について、現在わかっている情報を選択　1：各辺の長さ　2：各頂点の座標："))

    # 辺の長さを入力 → 整理
    if op == 1:
        ab, bc, ca = map(sympy.sympify, input("辺 AB, BC, CA の長さを、半角スペース区切りで入力：").split())
    else:
        ax, ay = map(sympy.sympify, input("A の x 座標, y 座標を、半角スペース区切りで入力：").split())
        bx, by = map(sympy.sympify, input("B の x 座標, y 座標を、半角スペース区切りで入力：").split())
        cx, cy = map(sympy.sympify, input("C の x 座標, y 座標を、半角スペース区切りで入力：").split())
        ab = sympy.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
        bc = sympy.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
        ca = sympy.sqrt((ax - cx) ** 2 + (ay - cy) ** 2)
    print()

    # 三角形を解く
    if (ab == bc) and (bc == ca):
        print("△ABCは、正三角形")
    elif ab == bc:
        print("△ABCは、AB = BC の二等辺三角形")
    elif bc == ca:
        print("△ABCは、BC = CA の二等辺三角形")
    elif ca == ab:
        print("△ABCは、CA = AB の二等辺三角形")

    if bc**2 == ca**2 + ab**2:
        print("△ABCは、∠A = 90°の直角三角形")
    elif ca**2 == ab**2 + bc**2:
        print("△ABCは、∠B = 90°の直角三角形")
    elif ab**2 == bc**2 + ca**2:
        print("△ABCは、∠C = 90°の直角三角形")

    # ヘロンの公式で面積を求める
    s = (ab + bc + ca) / 2
    area = sympy.sqrt(s * (s - ab) * (s - bc) * (s - ca))

    simplified_area = sympy.simplify(area)

    print(f"\n三角形の面積は、{simplified_area}")

def gravity_point():
    print("\n△ABC の重心 G の座標を求める")
    x1, y1 = map(int, input("A の x 座標, y 座標を、半角スペース区切りで入力：").split())
    x2, y2 = map(int, input("B の x 座標, y 座標を、半角スペース区切りで入力：").split())
    x3, y3 = map(int, input("C の x 座標, y 座標を、半角スペース区切りで入力：").split())

    gx = Fraction(x1 + x2 + x3, 3)
    gy = Fraction(y1 + y2 + y3, 3)

    print(f"\n重心 G の座標は、({gx}, {gy})")