tuple_already_processed = [(0,0,0)]*0

def is_tuple_already_inserted(x,y):
    for i in tuple_already_processed:
        if (i[0] == x) and (i[1] == y):
            return (True,i[2])
    return (False,0)

def insert_new_tuple(x,y,times):
    tuple_already_processed.append((x,y,times))

def decompose_in_sum_two_terms(x, y):
    if x<y:
        (is_tuple_inserted, times) = is_tuple_already_inserted(x,y)
        if is_tuple_inserted:
            return times
        else:
            n_terms  = decompose_in_sum_two_terms(x+1,y-(x+1))
            n_terms += decompose_in_sum_two_terms(x+1,y-1)
            n_terms += 1
            insert_new_tuple(x,y,n_terms)
            return n_terms
    else:
        return 0

def solution(n):
    return decompose_in_sum_two_terms(1,n-1)

import time

def main():
    print(solution(200) == 487067745)
    print(solution(3) == 1)

if __name__ == "__main__":
    main()    