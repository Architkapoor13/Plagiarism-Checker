def shingling(file_name, k):
    global file
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print(f"{file_name} is not found")
        return False
    shingles = []
    lines = file.readlines()
    for line in lines:
        j = 0
        for i in list(range(len(line) - k + 1)):
            sliced_string = line[j:j + k]
            if sliced_string not in shingles:
                shingles.append(sliced_string)
            j += 1
    file.close()
    return shingles

def equalornot(list1, list2):
    l1 = len(list1)
    l2 = len(list2)
    common = 0
    if l1 <= l2:
        for string in list1:
           if string in list2:
               common += 1
    else:
        for string in list2:
            if string in list1:
                common += 1
    total = len(list1) + len(list2) - common
    return common/total * 100

if __name__ == '__main__':
    file1 = input("Enter the name/path of the file1: ")
    file2 = input("Enter the name/path of the file2: ")
    k = int(input("Enter the value of k: "))
    shingles_file1 = shingling(file1, k)
    if not shingles_file1:
        exit(0)
    shingles_file2 = shingling(file2, k)
    if not shingles_file2:
        exit(0)
    # print(shingles_file1) commenting this out to not to print shingles
    # print(shingles_file2) commenting this out to not to print shingles
    print(f"{equalornot(shingles_file1, shingles_file2)}%")