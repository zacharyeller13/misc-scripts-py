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

    nums = input("input list of numbers (space separated): ")
    target = float(input("Input target num: "))

    l = nums.split()
    l = sorted([float(i) for i in l])
    print(l)

    find_sum(l, target)
