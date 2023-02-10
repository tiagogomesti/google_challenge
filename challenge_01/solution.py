def is_this_id_already_checked(id, checked_ids_array):
    for i in range(0, len(checked_ids_array)):
        if id == checked_ids_array[i]:
            return True
    return False

def read_tasks_id(data_array, reference_index):
    id_indexes = []

    for i in range(reference_index,len(data_array)):
        if data_array[reference_index] == data_array[i]:
            id_indexes.append(i)
    return id_indexes

def remove_id(data_array, ids_places_array):
    for i in range(0, len(ids_places_array)):
        data_array.pop(ids_places_array[i])
        if i+1 < len(ids_places_array):
            for j in range(i+1, len(ids_places_array)):
                ids_places_array[j] -= 1

def mark_id_as_checked(checked_ids_array, id):
    checked_ids_array.append(id)
    checked_ids_array.sort()


def solution(data, n): 
    checked_ids_array = []
    i = 0
    while True:
        id = data[i]
        if is_this_id_already_checked(id, checked_ids_array) == False:
            ids_places_array = read_tasks_id(data, i)
            if len(ids_places_array) > n:
                remove_id(data, ids_places_array)
                mark_id_as_checked(checked_ids_array, id)
                if (len(data) == 0) or (i == len(data)):
                    break
            else:
                mark_id_as_checked(checked_ids_array, id) 
                i += 1
                if i == len(data):
                    break
    return(data)


def main():
    # TODO: Avaliar futuramente se é necessário barrar análise com mais de 100 elementos
    print("Hello World!")
    print(solution([1, 2, 3], 0))
    print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))

if __name__ == "__main__":
    main()