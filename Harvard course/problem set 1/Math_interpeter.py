expression = input("Expression: ")

x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z

print(f"{answer:.1f}")