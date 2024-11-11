
symbol_table = []
literal_table = []
source_code = []

output_lines = []

testcase_folder = "Assignment_02/testcase"

def read_symbol_table() -> None:
    global symbol_table
    source_code_file = f"{testcase_folder}/symbol_table.txt"
    source_contents = ""

    with open(source_code_file, "r") as file:
        source_contents = file.read()

    source_code_list = source_contents.split('\n')
    for line in source_code_list:
        line_tokens = line.split(" ")
        symbol = line_tokens[0]
        lc = line_tokens[1]
        symbol_table.append([symbol, int(lc)])  


def read_literal_table():
    literal_table_content = ""

    with open(f"{testcase_folder}/literal_table.txt") as file:
        literal_table_content = file.read()

    literal_table_lines = literal_table_content.split("\n")

    for line in literal_table_lines:
        lit_token = line.split(" ")
        literal = lit_token[0]
        lc = lit_token[1]
        literal_table.append([literal,lc])

def read_source_code() -> None :
    global source_code
    source_code_file = f"{testcase_folder}/ic.txt"
    source_contents = ""

    with open(source_code_file, "r") as file:
        source_contents = file.read()
    
    source_code = [ line.split(")(") for line in source_contents.split("\n") ]
    
def parse_opcode(opcode):
    opcode_type = ""
    opcode_val = 0

    opcode_tokens = opcode.strip("(").strip(")").split(", ")
    print("Token ",opcode_tokens)
    opcode_type = opcode_tokens[0]
    opcode_val = int(opcode_tokens[1])

    return opcode_type, opcode_val

def parse_operand(operand):
    operand_type = ""
    operand_val = 0

    operand_tokens = operand.strip("(").strip(")").split(", ")

    if len(operand_tokens) == 1:
        operand_type = None
        operand_val = int(operand_tokens[0])

    else:
        operand_type = operand_tokens[0]
        operand_val = int(operand_tokens[1])


    return operand_type, operand_val

def parse_card(card):
    opcode_type = ""
    opcode_val = 0
    operand1_type = ""
    operand1_val = 0
    operand2_type = ""
    operand2_val = 0

    if len(card) == 1:
        opcode_type, opcode_val = parse_opcode(card[0])

    elif len(card) == 2:
        opcode_type, opcode_val = parse_opcode(card[0])
        operand_type, operand_val = parse_operand(card[1])
        if operand_type == None:
            operand1_type = operand_type
            operand1_val = operand_val
        else:
            operand2_type = operand_type
            operand2_val = operand_val

    elif len(card) == 3:
        opcode_type, opcode_val = parse_opcode(card[0])
        operand1_type, operand1_val = parse_operand(card[1])
        operand2_type, operand2_val = parse_operand(card[2])

    return opcode_type, opcode_val, operand1_type, operand1_val, operand2_type, operand2_val



def main():

    read_symbol_table()
    read_literal_table()
    read_source_code()

    global location_counter
    global literal_table
    global symbol_table
    location_counter = 0

    for line in symbol_table:
        print(line)

    print()

    for line in literal_table:
        print(line)

    for card in source_code:
        opcode_type, opcode_val, operand1_type, operand1_val, operand2_type, operand2_val = parse_card(card)
        
        print(f"\n{card}")
        print("Opcode Type : ", opcode_type)
        print("Opcode Val : ", opcode_val)
        print("Operand 1 Type : ", operand1_type)
        print("Operand 1 Val : ", operand1_val)
        print("Operand 2 Type : ", operand2_type)
        print("Operand 2 Val : ", operand2_val)

        if opcode_type == "AD" and (opcode_val == 1 or opcode_val == 3):
            location_counter = operand2_val

        if opcode_type == "IS":
            print(literal_table)
            if operand2_val !=0:
                if operand2_type == "S":
                    operand2_val = int(symbol_table[operand2_val-1][1])
                elif operand2_type == "L":
                    operand2_val = int(literal_table[operand2_val-1][1])

                output_line = f"{location_counter:03d}\t{opcode_val:02d}\t{operand1_val:02d}\t{operand2_val:03d}"
                output_lines.append(output_line)
                location_counter +=1

        if opcode_type == "DL":
            if opcode_val == 1:
                output_line = f"{location_counter:03d}\t00\t{operand1_val:02d}\t{operand2_val:03d}"
                output_lines.append(output_line)
                location_counter += 1
            else:
                output_line = f"{location_counter:03d}\t00\t00\t000"
                output_lines.append(output_line)
                location_counter += 1

        for output_line in output_lines:
            print(output_line)




        


if __name__ == "__main__":
    main()
