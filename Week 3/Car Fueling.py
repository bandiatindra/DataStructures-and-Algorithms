import sys

def get_minimum_refills(distance,tank,n,stops):

    curr_fill = 0
    num_refill = 0
    stops.append(distance)
    stops.insert(0,0)

    while curr_fill <= n :
        last_refill = curr_fill

        while (curr_fill <= n and (stops[curr_fill + 1] - stops[last_refill]) <= tank):
            curr_fill = curr_fill + 1
        if curr_fill == last_refill :
            return -1
        if curr_fill <= n:
            num_refill = num_refill + 1
    return num_refill


if __name__ == "__main__":
    d, m, n, *stops = map(int, sys.stdin.read().split())
    
    min_refills = get_minimum_refills(d,m,n,stops)
    print(min_refills)