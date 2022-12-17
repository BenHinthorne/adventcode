## day 5

def readfile(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return lines

def prep_input(lines):
    crates = []
    instructions = []
    switch = False
    for l in lines:
        if not l.strip():
            switch = True
            continue
        if switch:
            instructions.append(l)
        else:
            crates.append(l)
    return prep_crates(crates), prep_instructions(instructions)

def prep_instructions(raw):
    insts = []
    for r in raw:
        ## Some super hacky way to get only the numbers out
        inst = r.replace("move","").replace("from","").replace("to","").replace("  "," ").strip().split(" ")
        #[amt, start_i, end_i]    
        insts.append(inst) 
    return insts     
        

def prep_crates(raw):
    num_cols = raw[-1]
    num_cols = num_cols.strip().replace(" ","")
    num_cols = int(num_cols[-1])
    #print(num_cols)
    new_raw = raw[:-1]
    rows = []
    for r in new_raw:
        ## Some hacky way to represent the rows
        row = r.replace(" ", "-")
        #print(row)
        #rows.append(r.replace(" ", "-"))
        start = 1
        nr = ""
        for i in range(num_cols):
            nr += row[start]
            start += 4
        #rows.append(r.replace("   ", "-").replace(" ", "").replace("]","").replace("[",""))
        #print(nr)
        rows.append(nr)
        #ret.append(r.strip().replace("[","").replace("]","").replace(" ",""))
    # flip rows to columns
    # front is top of stack, back is end of stack
    #print(rows)
    cols = []
    for i in range(num_cols):
        cols.append([])
    #print(cols)
    for r in rows:
        for i in range(len(r)):
            if r[i] != "-":
                cols[i].append(r[i])
    return cols

def move(start_i, end_i, state):
    #if len(state[start_i]) == 0:
     #   return state # nothing to move
    # save c
    #print("BEFORE")
    #print(state[start_i])
    #print(state[end_i])
    c = state[start_i][0]
    # pop c from the starting col
    state[start_i] = state[start_i][1:]
    # push c to the start of end_i
    state[end_i] = [c] + state[end_i]
    #print("AFTER")
    #print(state[start_i])
    #print(state[end_i])
    return state

def move_part2(num_c, start_i, end_i, state):
    # save start crates
    cs = state[start_i][:num_c]
    # pop crates from starting col
    state[start_i] = state[start_i][num_c:]
    # push crates to ending colum 
    state[end_i] = cs + state[end_i]
    return state

def move_all_part2(state, insts):
    for i in insts:
        #print(state)
        state = move_part2(int(i[0]), int(i[1])-1, int(i[2])-1, state)
    return state


def move_all(state, insts):
    for i in insts:
        moves = int(i[0])
        for j in range(moves):
            state = move(int(i[1])-1, int(i[2])-1, state)
    return state

def get_answer(final_state):
    a = ""
    for c in final_state:
        a += c[0]
    return a
def solv_puzzle(filename):
    c, i = prep_input(readfile(filename))
    #print(c)
    #print(c[0:5])
    #print(i[0:5])
    final_state = move_all_part2(c, i)
    ans = get_answer(final_state)
    return ans

    
def main():
    print(solv_puzzle("input-test.txt"))
    print(solv_puzzle("input-real.txt"))

if __name__ == "__main__":
    main()
