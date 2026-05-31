S = 0.0

for i in range(1, 51):
    numerador = 2 * i - 1
    termo = numerador / i
    S = S + termo

print(f"{S:.10f}")