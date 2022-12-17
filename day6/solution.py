## day 4

def readfile(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return lines

# check if a string has only unique chars
def is_marker(cs):
    un = True
    for c in cs:
        if num_ocs(c, cs) > 1:
            un = False
    return un
# count occurances of char in string
def num_ocs(c, cs):
    num_ocs = 0
    for x in cs:
        if x == c:
            num_ocs += 1
    return num_ocs

def find_marker(s):
    marker = -1
    for i in range(len(s)):
        if i + 14 > len(s):
            print("Oh no reached end before found")
            return -1
        if is_marker(s[i:(i+14)]):
            marker = i + 14
            break
    return marker

        

def solv_puzzle(filename):
    lines = readfile(filename)
    input = lines[0]
    print(len(input))
    marker = find_marker(input)
    return marker
    
def main():
    print(solv_puzzle("input-test.txt"))
    print(solv_puzzle("input-test-2.txt"))
    print(solv_puzzle("input-real.txt"))

if __name__ == "__main__":
    main()
