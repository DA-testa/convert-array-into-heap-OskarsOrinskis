# python3

def kk(data, e, k, swaps):

    root = ss
    while(2 * root + 1) <= k:
    l = 2 * i + 1

    swap = root


    if data[swap] > data[l]:
        swap = l


    if l+1 <= k and data[swap] > data[l+1]:
        swap = l+1

    if swap != root:
        data[root], data[swap] = data[swap], data[root]
        swaps.append((root, swap))
        root = swap
    else:
        return




def build_heap(data):
    swaps = []

    n = len(data)

    for n in range((n-2) // 2, -1, -1):
        kk(data, e, n-1, swaps)
    for k in range(n-1, 0, -1):
        data[k], data[0] = data[0],  data[k]
        swaps.append((k, 0))
        kk(data, 0, k-1, swaps)  
    return swaps


def main():
    text = input()
    if text[0] == 'I':
        n = int(input())
        data = list(map(int, input().split()))

    elid text[0] == 'F':

        with open(f"testes/{input()}", "r") as file:
            

            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
