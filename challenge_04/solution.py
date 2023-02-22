def decompose_in_sum_two_terms(number, start_number):
    if start_number > number:
        return 0

    n_items = 0
    x = start_number
    y = number - start_number

    while(x < y):
        x += 1
        y -= 1
        n_items += 1

    return n_items

def solution(n):
    return decompose_in_sum_two_terms(n, 1)


def main():
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(7))
    print(solution(8))
    print(solution(9))
    # print(solution(200) == 487067745)
    # print(solution(3) == 1)

if __name__ == "__main__":
    main()    