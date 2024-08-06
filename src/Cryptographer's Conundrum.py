input1 = input()
def days(input1):
    dict1 = {'P': 0, 'E': 0, 'R': 0}
    count = 0

    for i in range(0, len(input1), 3):
        dict1['P'] += 1 if input1[i] != 'P' else 0
        dict1['E'] += 1 if input1[i+1] != 'E' else 0
        dict1['R'] += 1 if input1[i+2] != 'R' else 0

    count = sum(dict1.values())
    return count

print(days(input1))
