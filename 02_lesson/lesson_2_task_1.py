lst = ['🍇', '🍑', '🍐', '🍊', '🍌', '🍎']

result = lst[:1] + lst[-1:] if lst else []
print(result)
