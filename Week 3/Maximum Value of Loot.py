# Uses python3
import sys

def get_optimal_value(n, capacity, weights, values):

    unit_price = [0 for i in range(n)] 
    price_weights = []
    unit_price_sort = []
    weight_sort = []
    for i in range(n):
        unit_price[i] = values[i]/weights[i]
        price_weights.append((weights[i],unit_price[i]))

    #Sort weights based on unit price
    price_weights_sort = sorted(price_weights,
                         key = lambda x: x[1], 
                         reverse = True) #Sorted creates a new list, sort modified the original list.
    
    #Get sorted weights & unit price in separate lists, os that they can be modified iteratively.
    for tup in  price_weights_sort:
        unit_price_sort.append(tup[1])
        weight_sort.append(tup[0])

  
    wt_arr = [0 for i in range(n)] 
    val = 0

    for i in range(n):
        if capacity == 0:
            return val

        a = min(capacity, weight_sort[i])
        val = val + a*unit_price_sort[i]
        capacity = capacity - a
        weight_sort[i] = weight_sort[i] - a
        wt_arr[i] = wt_arr[i] + a

    return val

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2] # Subsetting every alternate value ot gt the array for values
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.4f}".format(opt_value))
   
