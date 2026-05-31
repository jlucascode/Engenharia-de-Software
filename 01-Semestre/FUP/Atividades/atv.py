x1 = float(input(""))
x2 = float(input(""))
y1, y2 = funcao(x1, x2)
print(f"{y1:.2f}")
print(f"{y2:.2f}")

def funcao(x1, x2):
        """Calcula a área e o perímetro de um retângulo.

        Entradas:
            x1: comprimento (float)
            x2: largura (float)

        Retorna:
            (area, perimetro)
        """
        area = x1 * x2
        perimetro = 2 * (x1 + x2)
        return area, perimetro


if __name__ == "__main__":
        try:
                x1 = float(input())
                x2 = float(input())
        except ValueError:
                print("Entrada inválida. Digite números (ex: 1 ou 1.0).")
                raise SystemExit(1)

        area, perimetro = funcao(x1, x2)
        print(f"{area:.2f}")
        print(f"{perimetro:.2f}")

x1 = float(input(""))
x2 = float(input(""))
y1, y2 = funcao(x1, x2)
print(f"{y1:.2f}")
print(f"{y2:.2f}")

def funcao(x1, x2):
    y1 = (x1 + x2) ** 2
    y2 = (x1 - x2) ** 2
    return y1, y2