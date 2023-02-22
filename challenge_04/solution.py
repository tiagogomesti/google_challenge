def decompose_in_sum_two_terms(start_number, number):
    if start_number > number:
        return 0

    n_items = 0
    x = start_number
    y = number - start_number

    while(x < y):
        print(x,y)
        n_items += decompose_in_sum_two_terms(x+1, y) + 1
        x += 1
        y -= 1

    return n_items

def solution(n):
    return decompose_in_sum_two_terms(1, n)


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