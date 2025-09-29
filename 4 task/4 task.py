def solve_permutation_cipher():
    # Читаем входные данные построчно
    n, k = map(int, input().split())
    permutation = list(map(int, input().split()))
    encrypted_word = input()

    # Создаем обратную перестановку
    inverse_permutation = [0] * (n + 1)
    for i in range(n):
        inverse_permutation[permutation[i]] = i + 1

    # Применяем обратную перестановку k раз
    current_word = list(encrypted_word)

    for _ in range(k):
        new_word = [''] * n
        for i in range(n):
            new_word[i] = current_word[inverse_permutation[i + 1] - 1]
        current_word = new_word

    return ''.join(current_word)

# Решаем задачу
result = solve_permutation_cipher()
print(result)