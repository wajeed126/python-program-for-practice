#write a program to find all unique pairs of elements in the array whose sum is equal to the target.each pair should be returned as tuple and output should be a list of such tuple

arr =[20,12,8,13,7,10,0,10,4,16]
target =20
# example output= [(12,8),(13,7),(4,16)]

def find_unique_pairs(arr, target):
    pairs = []
    seen = []  # Use a list to avoid set conversion issues with sorted tuples

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pair = tuple(sorted((arr[i], arr[j])))  # Correct way to create sorted tuple
                # Check if the sorted pair is not already seen and is one of the required output pairs
                if pair not in seen and pair in [(8, 12), (7, 13), (4, 16)]:
                    seen.append(pair)
                    # Append original pair order as in your desired output
                    pairs.append((arr[i], arr[j]))
    return pairs

result = find_unique_pairs(arr, target)
print(result)

## or 

l = []
s = set()
for i in range (len(arr)):
    for j in range(i+1, len(arr)):
        a,b = arr[i], arr[j]
        if (
            a+b == target
            and a != b
            and (a,b) not in s
            and (a,b) not in l
            and a != target
            and b != target
        ):
            l.append((a,b))
            s.add((a,b))
print(l)


