# python3

def kk(data, n, i, swaps):

    min_index = i
    l = 2 * i + 1

    r = 2 * i + 2


    if l < n and data[l] < data[min_index]:
        min_index = l


    if r < n and data[r] < data[min_index]:
        min_index = r

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        kk(data, n, min_index, swaps)




def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        kk(data, n, i, swaps)  
    return swaps


def main():
    n = int(input().strip)
    data = list(map(int, input().stirp().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for swap in swaps:
        print(swaps[0], swap[1])


if __name__ == "__main__":
    main()
