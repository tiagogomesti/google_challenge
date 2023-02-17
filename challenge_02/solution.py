def solution(s):
    movement_to_right = []
    movement_to_left = []
    hallway_len = len(s)
    num_salutes = 0

    for i in range(0,hallway_len):
        if s[i] == '>':
            movement_to_right.append(i)
        elif s[i] == '<':
            movement_to_left.append(i)
    
    for i in movement_to_right:
        for j in movement_to_left:
            if i<j:
                num_salutes += 2

    return num_salutes

    # Your code here

def main():
    print(solution("<<>><"))
    print(solution(">----<"))

if __name__ == "__main__":
    main()