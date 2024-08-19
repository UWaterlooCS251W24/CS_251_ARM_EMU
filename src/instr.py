
class Instr_Info:
    def __init__(self, instr, args):
        self.instr = instr
        self.args = args

class Instr:
    ADD = "ADD"
    SUB = "SUB"

    LDUR = "LDUR"
    STUR = "STUR"

    ADDI = "ADDI"
    SUBI = "SUBI"

    B = "B"

    CBZ = "CBZ"
    CBNZ = "CBNZ"

    INSTRS = [
        ADD, SUB, LDUR, STUR, ADDI, SUBI, B, CBZ, CBNZ
    ]

    R_TYPE = [ ADD, SUB ]
    D_TYPE = [ LDUR, STUR ]
    I_TYPE = [ ADDI, SUBI ]
    B_TYPE = [ B ]
    CB_TYPE = [ CBZ, CBNZ ]

    def extract(instr_str):
        orig = instr_str
        index = instr_str.find(';')
        if index != -1:
            instr_str = instr_str[:index]
        index = instr_str.find('@')
        if index != -1:
            instr_str = instr_str[:index]

        if not instr_str.isupper():
            print("Error: Instruction must be uppercase: " + orig)
            instr_str = instr_str.upper()

        instr = instr_str.split()[0]
        args = instr_str[len(instr):]

        if instr_str.find(',') != -1:
            print("Error: No commas allowed in instruction: " + orig)
            args = args.replace(',', ' ')

        args = args.replace('[', ' ')
        args = args.replace(']', ' ')

        args = args.split()
        args = list(filter(lambda x: x != '', args))

        return Instr_Info(instr, args)


