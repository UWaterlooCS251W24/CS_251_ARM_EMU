
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
        instr_str = instr_str.strip()
        index = instr_str.find(';')
        if index != -1:
            instr_str = instr_str[:index]
        index = instr_str.find('@')
        if index != -1:
            instr_str = instr_str[:index]

        instr_str = instr_str.upper()

        instr = instr_str.split(' ')[0]
        args = instr_str[len(instr):]

        args = args.replace(',', ' ')

        args = args.replace('[', ' ')
        args = args.replace(']', ' ')

        args = args.replace('\t', ' ')
        args = args.replace('\v', ' ')
        args = args.replace('\n', ' ')
        args = args.replace('\r', ' ')
        args = args.replace('\f', ' ')

        args = args.split(' ')
        args = list(filter(lambda x: x != '', args))

        return Instr_Info(instr, args)


