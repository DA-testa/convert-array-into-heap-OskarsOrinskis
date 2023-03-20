# python3
import queue
def build_heap(data, n, j):

    tread = queue.PriorityQueue()

    for i in range(n)

        treads.put((0, i))

    swaps = []

    for i in range(j):
        
        data_time = data[i]
    
        start_time, tread = trads.get()

        swaps.append((tread, start_time))

        treads.put((sart_time + data_time, tread))

    return swaps

   





def main():
    n, j = map(int, input().split())
    data = list(map(int, input().split()))
    x = build_heap(n, j, data)
    
    for i in range(j):
        print(x[i][0], x[i][1])


if __name__ == "__main__":
    main()
