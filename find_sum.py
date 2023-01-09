def find_sum(numbers: list[float], target: float, partial=[]):
    s = sum(partial)

    if s == target:
        print(f"sum({partial})={target}")
    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        find_sum(remaining, target, partial +[n])

if __name__ == "__main__":

    l = "5 5 5 5 5 25 50 75 100".split()
    l = [float(i) for i in l]
    print(l)

    find_sum(l, 75)
