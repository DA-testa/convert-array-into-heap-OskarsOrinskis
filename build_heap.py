# python3
import heapq
def build_heap(n, j, data):
    treads = []
    for i in range(n):
        heapq.heappush(treads, (0, i))
    swaps = []

    for i in range(j):
        data_time = data[i]
        start_time, tread = heapq.heappop(treads)
        swaps.append((tread, start_time))
        heapq.heappush(treads, (sart_time + data_time, tread))
    return swaps

   





def main():
    try:
        n, j = map(int, input().split())
        data = list(map(int, input().split()))
    except ValueError:
        return
    
    x = build_heap(n, j, data)
    total = x[-1][1]
    print(total)
    for i in range(len(x)):
        print(x[i][0], x[i][1])

    print(total)

if __name__ == "__main__":
    main()
