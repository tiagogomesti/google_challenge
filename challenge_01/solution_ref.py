def solution_reference(data, n):
    if not data or len(data) == 0 or n <= 0:
        return None
    occurrences = {}
    for item in data:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    result = []
    for item in data:
        if occurrences[item] <= n:
            result.append(item)            
    return result