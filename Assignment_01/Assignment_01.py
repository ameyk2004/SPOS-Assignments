optab = {
    "STOP" : ["IS", 0],
    "ADD" : ["IS", 1],
    "SUB" : ["IS", 2],
    "MULT" : ["IS", 3],
    "MOVER" : ["IS", 4],
    "MOVEM" : ["IS", 5],
    "COMP" : ["IS", 6],
    "BC" : ["IS", 7],
    "DIV" : ["IS", 8],
    "READ" : ["IS", 9],
    "PRINT" : ["IS", 10],

    "START" : ["AD", 1],
    "END" : ["AD", 1],
    "ORIGIN" : ["AD", 1],
    "EQU" : ["AD", 1],
    "LTORG" : ["AD", 1],

    "DC" : ["DL", 1],
    "DS" : ["DL", 1],
}

register_codes = {
    "AREG" : 1,
    "BREG" : 2,
    "CREG" : 3,
    "DREG" : 4,
}

cond_codes = {
    "LT" : 1,
    "LE" : 2,
    "EQ" : 3,
    "GT" : 4,
    "GE" : 5,
    "ANY" : 6,

}

ic_code = []
location_counter = 0
source_lines = []

symbol_table = []
literal_table = []
pool_table = ["#1"]

def read_file():
    global source_lines
    file_loc = "Assignment_01/testcase01.asm"
    source_file_content = ""

    with open(file_loc, "r") as file:
        source_file_content = file.read()

    lines = source_file_content.split("\n")
    source_lines = (line.split() for line in lines)


def tokenize_line(line):
    label = ""
    opcode = ""
    operand1 = ""
    operand2 = ""

    if (len(line) == 1) and line[0] in (optab.keys()):
        opcode = line[0]

    elif (len(line) == 1):
        label = line[0]

    if (len(line) == 2) and line[0] in (optab.keys()):
        opcode = line[0]
        operand1 = line[1]

    elif (len(line) == 2):
        label = line[0]
        opcode = line[1]

    if (len(line) == 3) and line[0] in (optab.keys()):
        opcode = line[0]
        operand1 = line[1]
        operand2 = line[2]


    elif (len(line) == 3):
        label = line[0]
        opcode = line[1]
        operand1 = line[2]

    if (len(line) == 4):
        label = line[0]
        opcode = line[1]
        operand1 = line[2]
        operand2 = line[3]

    return label, opcode, operand1, operand2

def get_symbol_position(symbol):
    for i in range(len(symbol_table)):
        if symbol_table[i][0] == symbol:
            return i+1
    return -1

def get_literal_position(literal):
    current_pool = pool_table[len(pool_table) -1]
    for i in range(len(pool_table)):
        if pool_table[i][0] == literal and pool_table[i][0] == current_pool:
            return i+1
        
    return -1


def insert_into_symbol_table(symbol, lc=None, forward_ref=True):
    position = get_symbol_position(symbol)

    if lc == None:
        lc = location_counter

    if forward_ref:
        if position == -1:
            symbol_table.append([symbol, -1])

    else:
        if position == -1:
            symbol_table.append([symbol, lc])

        else:
            symbol_table[position -1][1] = symbol

def insert_into_literal_table(literal):
    position = get_literal_position(literal)

    if position == -1:
        current_pool = pool_table[(pool_table-1)]
        literal_table.append([literal, -1, current_pool])


def increment_location_counter(val=1):
    global location_counter
    location_counter = location_counter + val

def set_location_counter(val=1):
    global location_counter
    location_counter = val

def get_symbol_location_counter(symbol):
    index = get_symbol_position(symbol) -1

    if index < 0:
        return -1
    else:
        return symbol_table[index][1]

def get_operand_str(operand):

    if operand == "":
        return ""
    
    operand_type, operand_val = parse_operand(operand)

    if operand_type == "REG" or operand_type == "COND":
        return f"({operand_val})"
    else:
        return f"({operand_type}, {operand_val})"
    
def get_constant_value(operand):
    is_constant = False
    operand_val = 0

    if operand == "":
        is_constant = False

    elif operand.isnumeric():
        is_constant = True
        operand_val = int(operand)

    elif '+' in operand:
        op_tokens = operand.split('+')
        symbol = op_tokens[0]
        offset = int(op_tokens[1])
        symbol_lc = get_symbol_location_counter(symbol)
        operand_val = symbol_lc + offset

    elif '-' in operand:
        op_tokens = operand.split('-')
        symbol = op_tokens[0]
        offset = int(op_tokens[1])
        symbol_lc = get_symbol_location_counter(symbol)
        operand_val = symbol_lc - offset

    return is_constant, operand_val

def parse_operand(operand):
    operand_type = ""
    operand_val = ""

    #L,REG, COND, CON SYM

    if operand[0] == "=":
        operand_type = "L"
        literal = operand[1:]
        insert_into_literal_table()
        operand_val = get_literal_position(literal)

    elif operand in register_codes.keys():
        operand_type = "REG"
        operand_val = register_codes.get(operand)

    elif operand in cond_codes.keys():
        operand_type = "COND"
        operand_val = cond_codes.get(operand)

    elif get_constant_value(operand)[0] == True:
        operand_type = "C"
        operand_val = get_constant_value(operand)[1]

    else:
        operand_type = "S"
        insert_into_symbol_table(operand)
        operand_val = get_symbol_position(operand)

    return operand_type, operand_val

def handle_imperative_statement(label, opcode, operand1, operand2):
    global ic_code
    _, opcode_ic = optab.get(opcode)
    output_line = f"(IS, {opcode_ic})"
    output_line += get_operand_str(operand1)
    output_line += get_operand_str(operand2)
    ic_code.append(output_line)
    increment_location_counter()

def print_ic():
    print("\nIC Table")
    for i in range(0, len(ic_code)):
        print(ic_code[i])

def print_symbol_table():
    print("\n\nSymbol Table")
    for i in range(0, len(symbol_table)):
        print(f"{i+1}\t{symbol_table[i][0]}\t{symbol_table[i][1]}")

def print_literal_table():
    print("\nLiteral Table")
    pool = "#1"
    i = 1
    for literal_entry in literal_table:
        if literal_entry[2] != pool:
            pool = literal_entry[2]
            print()
        print(f"{i}\t{literal_entry[0]}\t{literal_entry[1]}")
        i+= 1

def print_pool_table():
    print("\n\nPool Table")
    for i in range(0, len(pool_table)-1):
        print(pool_table[i])

def main():

    read_file()

    for line in source_lines:
        global location_counter

        if location_counter == 1:
            print(line)

        print(line)
        lable, opcode, operand1, operand2 = tokenize_line(line)

        print("Label : ", lable)
        print("Opcode : ", opcode)
        print("Operand 1 : ", operand1)
        print("Operand 2 : ", operand2)
        print("\n")

        if lable != "":
            insert_into_symbol_table(lable)

        if opcode != "":

            opcode_type, _ = optab.get(opcode)

            if opcode_type == "IS":
                handle_imperative_statement(lable, opcode, operand1, operand2)
         
    print_ic()
    # Print Symbol Table
    print_symbol_table()
    # Print Literal Table
    print_literal_table()
    # Print Pool Table
    print_pool_table()
    

if __name__ == "__main__":
    main()

