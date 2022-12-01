import math

def solv_puzzle(filename, num_elves):
    with open(filename, "r") as file:
        lines = file.readlines()
    top_cals = [0]*num_elves
    cals = 0
    for line in lines:
        if not line.strip():
            top_cals = replace(top_cals, cals)
            cals = 0
        else:
            cals += int(line)
    top_cals = replace(top_cals, cals) #one last check for final input
    return sum(top_cals)

def replace(top, e):
    smallest = top[0]
    for t in top:
        if t < smallest:
            smallest = t
    if e > smallest:
        list.remove(top, smallest)
        list.append(top, e)
    return top



def main():
    print(solv_puzzle("input-real.txt", 1))
    print(solv_puzzle("input-real.txt", 3))
    

if __name__ == "__main__":
    main()
