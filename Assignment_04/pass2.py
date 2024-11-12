
folder_name = "Assignment_04/testcase"

mnt = []
mdt = []
kpdt = []
src = []
apt = []

output_lines = []

def read_src():
    global folder_name, src
    # M1 10 20 &B=CREG
    # M1 100 200 300 &V=AREG &U=BREG
    src_content = ""

    with open(f"{folder_name}/src.txt", "r") as file:
        src_content = file.read()

    src = [line.split() for line in src_content.split("\n")]


def read_mnt():
    global folder_name, mnt
    # M1 2 2 1 1 1
    # M1 3 2 6 3 5
    mnt_content = ""

    with open(f"{folder_name}/MNT.txt", "r") as file:
        mnt_content = file.read()

    mnt = [line.split() for line in mnt_content.split("\n")]

def read_mdt():
    global folder_name, mdt
 
    mdt_content = ""

    with open(f"{folder_name}/MDT.txt", "r") as file:
        mdt_content = file.read()

    mdt = [line.split() for line in mdt_content.split("\n")]

def read_kpdt():
    global folder_name, kpdt
 
    kpdt_content = ""

    with open(f"{folder_name}/KPDT.txt", "r") as file:
        kpdt_content = file.read()

    kpdt = [line.split() for line in kpdt_content.split("\n")]

def is_valid_call(line):
    global mnt
    kp = 0
    pp = 0
    macro_name = line[0]

    for i in range(1, len(line)):
        if '=' in line[i]:
            kp+=1
        else:
            pp+=1

    for mnt_entry in mnt:

        if (mnt_entry[0] == macro_name) and (pp == int(mnt_entry[1])) and (kp <= int(mnt_entry[2])):
            return True, mnt_entry

    return False, None

def get_arguments(line, mnt_entry):
    parameters = []
    #add positional params

    for i in range(1,len(line)):
        if '=' not in line[i]:
            parameters.append(line[i])

    #copy keyword params
    kp = mnt_entry[2]
    kpdt_start = int(mnt_entry[4]) - 1
    keyword_params = []

    for j in range(int(kp)):
        kpdt_entry = kpdt[kpdt_start+j][:]
        keyword_params.append(kpdt_entry)


    for i in range(1, len(line)):
        if '=' in line[i]:
            token = line[i].split('=')
            for j in range(len(keyword_params)):
                if token[0] == keyword_params[j][0]:
                    keyword_params[j][1] = token[1]


    #add values to keyword params
            
    for i in range(0, len(keyword_params)):
        if keyword_params[i][1] != '_':
            parameters.append(keyword_params[i][1])
        else:
            raise Exception(f"Argument not provided for parameter {keyword_params[i][0]}")

    return parameters

def expand_macro_call(mdt_start):
    global mdt,apt
    i = mdt_start
    mdt_entry = mdt[i]
    while 'MEND' not in mdt_entry:
        output_line = ""
        for j in range(len(mdt_entry)):
            if '(' in mdt_entry[j]:
                parameter_token = mdt_entry[j].strip('(').strip(')').split(',')
                index = int(parameter_token[1].strip()) - 1
                output_line += f" {apt[index]}"
            else:
                output_line += f"{mdt_entry[j]}"

        output_lines.append(output_line)



        i+=1
        mdt_entry = mdt[i]

def main():
    global output_lines, src, mnt, mdt, kpdt, apt
    read_src()
    read_mnt()
    read_kpdt()
    read_mdt()

    for line in src:
        
        valid, mnt_entry = is_valid_call(line)

        if valid:
            apt = get_arguments(line, mnt_entry)
            mdt_start = int(mnt_entry[3])- 1
            expand_macro_call(mdt_start)
        else:
            output_line = ' '.join(line)
            output_lines.append(output_line)

    for line in output_lines:
        print(line)

if __name__ == "__main__":
    main()