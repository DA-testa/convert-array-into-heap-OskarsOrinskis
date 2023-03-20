# python3
import heapq
def build_heap(data, tread):

    n = len(tread)
    j = len(data)

    tread.heap = [(t, i) for i, t in enumerate(tread)]
    heapq.heap(tread_heap)

    swaps = []

    if i in range(j):
        data_time = data[i]

        start_time, tread = heapq.heappop(tread_heap)

        swaps.append((tread, start_time))
        
        heapq.heappush(thread_heap, (sart_time + data_time, tread))

    return swaps






def main():
    n, j= map(int, input().split())
    tread = [int(input()) for i in range(n)]
    data = [int(input()) for i in range(j)]
    x = build_heap(tread, data)
    
    for i in range(j):
        print(x[i][0]+1, x[i][1])


if __name__ == "__main__":
    main()
