## 1.py
count = 0
for num in range(10, 100):
    a, b = divmod(num, 10)
    result = a * b
    result = (result // 10) * (result % 10)
    result = (result // 10) + (result % 10)
    if result == 8:
        count += 1
print(count)

## 2.py
def func(start, target):
    def helper(a, b):
        if a + b == start:
            return 1
        if a + b > start:
            return 0
        return helper(a + b, b) + helper(a, a + b)

    return helper(*target)

print(func(88, (1, 1)))

## 3.py
def func(start, target):
    seen = set()

    def helper(current):
        if current == target:
            return 1
        if current > target or current in seen:
            return 0
        seen.add(current)
        return helper(current + 2) + helper(int(str(current) + "2"))

    return helper(start)

print(func(2, 900))

## 4.py
def func(start, target):
    if start == target:
        return 1
    if start > target:
        return 0
    return func(start + 1, target) + func(int(str(start) + "1"), target)

print(func(1, 555))

## 6.py
def func(start, target, seen=None):
    if seen is None:
        seen = set()
    if start >= target:
        return 0
    if start % 2 == 0:
        seen.add(start)
    func(start + 3, target, seen)
    func(start * 3, target, seen)
    return len(seen)

print(func(3, 100))

## 7.py
def func(start, target):
    if start == target:
        return 1
    if start > target:
        return 0
    return func(start + 1, target) + func(start * 2, target)

print(func(1, 16))

## 8.py
def func(start, target, has_11=False, has_25=False):
    if start == target:
        return 1 if has_11 and has_25 else 0
    if start > target:
        return 0
    return func(start + 1, target, has_11 or start == 11, has_25 or start == 25) + func(start * 2, target, has_11 or start == 11, has_25 or start == 25)

print(func(2, 50))

## 9.py
def func(start, target, has_25=False):
    if start == target:
        return 1 if not has_25 else 0
    if start > target:
        return 0
    return func(start + 1, target, has_25 or start == 25) + func(2 * start + 1, target, has_25 or start == 25)

print(func(1, 31))

## 10.py
def func(start, target):
    if start == target:
        return 1
    if start > target:
        return 0
    if start % 2 == 0:
        return func(start + 1, target) + func(int(start * 1.5), target)
    return func(start + 1, target)

print(func(2, 22))

## 11.py
def func(start, target, steps):
    if steps == 0:
        return 1 if start == target else 0
    if start > target:
        return 0
    return (func(start + 1, target, steps - 1) +
            func(start + 2, target, steps - 1) +
            func(start * 2, target, steps - 1))

print(func(1, 20, 6))

## 12.py
def func(start, target, steps):
    if steps == 0:
        return 1 if start == target else 0
    if start > target:
        return 0
    return (func(start + 1, target, steps - 1) +
            func(start + 2, target, steps - 1) +
            func(start + 3, target, steps - 1))

print(func(3, 22, 7))

## 13.py
def func(start, target, steps):
    if steps == 0:
        return 1 if start == target else 0
    if start > target:
        return 0
    return (func(start + 1, target, steps - 1) +
            func(start + 3, target, steps - 1) +
            func(start * 2, target, steps - 1))

print(func(2, 25, 7))

## 14.py
def func(start, target, steps):
    if steps == 0:
        return 1 if start == target else 0
    if start > target:
        return 0
    return (func(start + 1, target, steps - 1) +
            func(start * 2, target, steps - 1) +
            func(start * 3, target, steps - 1))

print(func(1, 34, 8))

## 15.py
def func(start, steps, results):
    if steps == 0:
        results.add(start)
        return
    func(start * 2, steps - 1, results)
    func(start * 2 + 1, steps - 1, results)

results = set()
func(1, 15, results)
print(len(results))