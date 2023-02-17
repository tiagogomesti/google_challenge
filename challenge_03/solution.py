def convert_to_descending_order(string):
    sorted_chars = sorted(string, reverse=True)
    sorted_string = ''.join(sorted_chars)
    return sorted_string
    

def convert_to_ascending_order(string):
    sorted_chars = sorted(string, reverse=False)
    sorted_string = ''.join(sorted_chars)
    return sorted_string

def to_string(n,base):
    conversion_string = "0123456789ABCDEF"
    if n < base:
        return conversion_string[n]
    else:
        return to_string(n//base,base) + conversion_string[n % base]

def subtract(n1, n2, base, k):
    result = int(n1,base) - int(n2,base)
    str = to_string(result, base).zfill(k)
    return str

def ids_array_contains(ids_array, id):
    for i in ids_array:
        if i==id:
            return True
    
    return False

def add_to_array_contains(ids_array ,z):
    ids_array.append(z)

def last_id_array(ids_array):
    if len(ids_array) == 0:
        return None
    else:
        return ids_array[len(ids_array) - 1]
    
def get_cycle_len(ids_array, id):
    return len(ids_array) - ids_array.index(id)
    

def solution(n, b):
    k = len(n)
    ids_array = [n]
    
    while True:
        last_id = last_id_array(ids_array)
        x = convert_to_descending_order(last_id)
        y = convert_to_ascending_order(last_id)
        z = subtract(x, y, b, k)
        if z == last_id:
            return 1 
        elif not ids_array_contains(ids_array, z):
            add_to_array_contains(ids_array, z)
        else:
            cycle_len = get_cycle_len(ids_array, z)
            return cycle_len

def main():
    print(solution('1211', 10) == 1)
    print(solution('210022', 3) == 3)

if __name__ == "__main__":
    main()    