tuple_already_processed = [(0,0,0)]*0
main_loop = 0
use_tuples = False
i_loop = 0

def is_tuple_already_inserted(x,y):
    if not use_tuples:
        return (False,0)
    for i in tuple_already_processed:
        if (i[0] == x) and (i[1] == y):
            return (True,i[2])
    return (False,0)

def insert_new_tuple(x,y,times):
    if not use_tuples:
        return
    tuple_already_processed.append((x,y,times))

def decompose_in_sum_two_terms(x, y):
    global main_loop
    main_loop += 1
    if x<y:
        (is_tuple_inserted, times) = is_tuple_already_inserted(x,y)
        if is_tuple_inserted:
            return times
        else:
            n_terms  = decompose_in_sum_two_terms(x+1,y-(x+1))
            n_terms += decompose_in_sum_two_terms(x+1,y-1)
            n_terms += 1
            print(i_loop ,main_loop, x, y, n_terms)
            insert_new_tuple(x,y,n_terms)
            return n_terms
    else:
        return 0

def solution(n):
    return decompose_in_sum_two_terms(1,n-1)

def main():
    global use_tuples
    global main_loop
    global i_loop
    index = []
    loops_with_tuples = []
    loops_without_tuples = []
    for i_loop in range(50, 55):
        main_loop = 0
        tuple_already_processed.clear()
        use_tuples = True
        solution(i_loop)
        loops_with_tuples.append(main_loop)
        main_loop = 0
        tuple_already_processed.clear()
        use_tuples = False
        solution(i_loop)
        loops_without_tuples.append(main_loop)
        index.append(i_loop)

    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("")
    for i in range(0, len(index)):
        print(index[i], loops_with_tuples[i], loops_without_tuples[i])

if __name__ == "__main__":
    main()    