def find_sum(numbers: list[float], target: float, partial=[]) -> None:
    global unique_sums
    s = sum(partial)

    if s == target:
        # print(f"sum({partial})={target}")
        unique_sums.add(tuple(sorted(partial)))

    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        find_sum(remaining, target, partial +[n])

if __name__ == "__main__":

    nums = input("input list of numbers (space separated): ")
    target = float(input("Input target num: "))
    unique_sums = set()

    l = nums.split()
    l = [float(i) for i in l]
    print(l)

    find_sum(l, target)

    print("\nUnique Sums:")
    for item in unique_sums:
        print(item)
