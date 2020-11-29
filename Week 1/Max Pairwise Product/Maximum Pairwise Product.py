
def max_pairwise_product(a, lst):    
    
    max_elem = max(lst)
    new_lst = lst.copy() # Dont just assign a list to another list.. If you make changes to new list, those afect first list too. 
    new_lst.remove(max_elem) 

    if len(lst) - 1 == len(new_lst):
        second_max_elem = max(new_lst)
    else:
        second_max_elem = max_elem
    return (max_elem * second_max_elem)



if __name__ == '__main__':
    a = int (input())
    lst = [int(x) for x in input().split()]
    print (max_pairwise_product(a,lst))






