# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)

    for i in range(n // 2, -1, -1):

        min_index = i
        l = 2 * i + 1

        if l < n and data[l] < data[min_index]:
            min_index = 1
        r = 2 * i + 2

        if r < n and data[r] < data[min_index]:
            min_index = r

        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            swaps += build_heap(data[min_index:])

    return swaps


def main():
    
    input_str = input().strip()
    input_str = input_str.replace('I', '').replace('F', '')
    n = int(input_str) if input_str else 0
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
