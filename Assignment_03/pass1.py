
MNT = []
MDT = []
KPDT = []
PNT = []

source_code = []
source_code_file_loc  = "Assignment_03/testcase.asm"

output_lines = []

def read_file():
    global source_code
    source_code_content = ""

    with open(source_code_file_loc, "r") as file:
        source_code_content = file.read()

    source_code = [line.split() for line in source_code_content.split("\n")]

def analyze_macro_definition_card(macro_definition_card):
    global MNT
    macro_name = macro_definition_card[0]
    pp = 0
    kp = 0
    MDTP = len(MDT) + 1
    KPDTP = len(KPDT) + 1
    PNTP = len(PNT) + 1

    for i in range(1, len(macro_definition_card)):
        token = macro_definition_card[i]
        if '=' in token:
            parameter_tokens = token.split('=')
            param = parameter_tokens[0]
            default = parameter_tokens[1] if len(parameter_tokens) == 2 else '_'
            kp+=1
            PNT.append(param)
            KPDT.append([param, default])

        else:
            param = token
            pp+=1
            PNT.append(param)

    MNT.append([macro_name, pp, kp, MDTP, KPDTP, PNTP])

def substitute_indexes_forparam(line_tokens):
    global MDT
    global output_lines
    mnt_definition = MNT[len(MNT)-1 ]
    total_params = mnt_definition[1] + mnt_definition[2]
    pnt_start = int(mnt_definition[5]) - 1

    output_line = ""

    for i in range(len(line_tokens)):
        token = line_tokens[i]

        if '&' in token:
            index = -1
            for j in range(total_params):
                if token == PNT[pnt_start + j]:
                    index = j+1
                    break

            output_line += f" (P, {index})"
        else:
            output_line += f" {token}"

    output_line = output_line.strip()
    MDT.append(output_line)
    output_lines.append(output_line)

    
def main():
    global source_code
    global source_code
    read_file()

    line_number = 0

    while line_number < len(source_code):

        line_tokens = source_code[line_number]

        if 'MACRO' in line_tokens:
            line_number+=1

            macro_definition_card = source_code[line_number]
            analyze_macro_definition_card(macro_definition_card)

            line_number +=1

            while True:
                line_tokens = source_code[line_number]
                
                substitute_indexes_forparam(line_tokens)

                if 'MEND' in line_tokens:
                    break

                line_number+=1

        line_number+=1

    for line in PNT:
        print(line)

if __name__ == "__main__":
    main()