# python3

def kk(data, n, i, swaps):

    n = len(data)
    min_index = i
    l = 2 * i + 1

    r = 2 * i + 2


    if l < n and data[l] < data[min_index]:
        min_index = 1


    if r < n and data[r] < data[min_index]:
        min_index = r

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        kk(data, min_index, swaps)




def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        kk(data, n, i, swaps)
        
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)



