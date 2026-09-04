def lits_to_dict(keys, values):
    result = dict(zip(keys,values))
    return result

keys = ["name", "age", "city"]
values = ["Shoaib", 25, "Mumbai"]

print(lits_to_dict(keys, values))

def list_to_dict(keys, values):
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result

keys = ["name", "age", "city"]
values = ["Shoaib", 25, "Mumbai"]

print(list_to_dict(keys, values))