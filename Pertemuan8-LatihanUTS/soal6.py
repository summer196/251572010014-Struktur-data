input_str = "Algoritma"
stack = []

for karakter in input_str:
    stack.append(karakter)

terbalik = ""
while stack:
    terbalik += stack.pop()

print("Original", input_str)
print("Terbalik", terbalik)