a, b = map(int, input().split());
result = [a, b][a <= b]
if a!=b:
    print(result)
else:
    print("Числа равны")