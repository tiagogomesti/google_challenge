def ap_sum_terms(a1, r, n_terms):
    an = a1 + (n_terms-1)*r
    return n_terms*(a1+an)/2

def check_tuple(x, y, sum):
    i = 0
    result = 0
    a1 = x
    r = y - x
    while result < sum:
        result = ap_sum_terms(a1, r, i)
        i += 1

    if result == sum:
        return True
    else:
        return False

def solution(n):
    if n<3:
        return None

    x = 1
    y = n-1
    n_terms = 0

    while x<y:
        if check_tuple(x, y, n):
            n_terms += 1
            # print(x,y)
        x += 1
        y -= 1

    return n_terms



def main():
    # print(3, solution(3))
    # print(4, solution(4))
    # print(5, solution(5))
    # print(6, solution(6))
    # print(7, solution(7))
    # print(8, solution(8))
    # print(9, solution(9))
    # print(9, solution(50))

    for i in range(0, 15):
        print(i, solution(i))
        

    # print(solution(200))
    # print(solution(200) == 487067745)
    # print(solution(3) == 1)

if __name__ == "__main__":
    main()    