def combo_find(C, S):
    C.sort()

    def rec(pool, s):
        if s == 0:
            return [[]]
        if s < 0:
            return []
        i, result = 0, []
        while i < len(pool):
            current = pool[i]
            for sub in rec(pool[i + 1:], s - current):
                result.append([current] + sub)
            while i < len(pool) and pool[i] == current:
                i += 1
        return result

    return rec(C, S)
candidates = list(map(int, input("Введите числа через запятую: ").split(',')))
target = int(input("Введите целевую сумму: "))

combinations = combo_find(candidates, target)
print("Подходящие комбинации:", combinations)
