#exp short for expression

exp = input("Expression: ")
x, y, z = exp.split(" ")

x = float(x)
z = float(z)

if y == "+":
    ans = x + z

elif y == "-":
    ans = x - z

elif y == "*":
    ans = x * z

elif y == "/":
    ans = x / z

print(round(ans, 1))
