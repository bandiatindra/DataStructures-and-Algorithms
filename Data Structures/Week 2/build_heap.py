# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps

    swaps = []
    def SiftDown(size, i):
    
        max_index = i
        left_index  = 2*i+1
        right_index = 2*i+2

        if left_index <size and data[left_index] < data[max_index]:
            max_index = left_index

        if right_index < size and data[right_index] < data[max_index]:
            max_index = right_index

        if i != max_index:
            temp = data[i]
            data[i] = data[max_index]
            data[max_index] = temp            
            swaps.append([i,max_index])
            SiftDown(size, max_index)
             

    size = len(data)
    
    for i in range(int(size/2)-1,-1,-1):
        SiftDown(size, i)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
