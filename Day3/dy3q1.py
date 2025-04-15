#input data = [1,2,3, [1,2,3,[3,4],2]]
#output data=[1, 2, 3, 1, 2, 3, 3, 4, 2]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item)) 
        else:
            result.append(item)
    return result
    
input_list = [1, 2, 3, [1, 2, 3, [3, 4], 2]]
flattened = flatten(input_list)
print(flattened)
    
    