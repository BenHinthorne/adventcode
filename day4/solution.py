## day 4

def readfile(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return lines

def prep_pairs(lines):
    res = []
    for l in lines:
        split = str.split(l, ",")
        pair = (make_list(split[0]), make_list(split[1]))
        res.append(pair)
    return res

def make_list(s):
    min = int(str.split(s, "-")[0])
    max = int(str.split(s, "-")[1])
    res = []
    for i in range(min, max+1):
        res.append(i)
    return res

def is_full_overlap(pair):
    return all(elem in pair[0] for elem in pair[1]) or all(elem in pair[1] for elem in pair[0])

def is_any_overlap(pair):
    return  any(elem in pair[0] for elem in pair[1])


def solv_puzzle(filename):
    input = readfile(filename)
    pairs = prep_pairs(input)
    total_full = 0
    total_any = 0
    for p in pairs:
        if is_full_overlap(p):
            total_full += 1
            total_any += 1
        elif is_any_overlap(p):
            total_any += 1
    return total_full, total_any
    
def main():
    print(solv_puzzle("input-test.txt"))
    print(solv_puzzle("input-real.txt"))

if __name__ == "__main__":
    main()
