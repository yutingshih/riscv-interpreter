class Instruction(object):
    cnt = 0
    def __init__(self, op: callable, args: dict[str, int]) -> None:
        self.op = op
        self.args = args
        self.pc = Instruction.cnt
        Instruction.cnt += 1

    def __call__(self, regfile) -> None:
        self.op(regfile, **self.args)

    def __repr__(self) -> str:
        return f'{self.op} {self.args}'


class RV32I(object):
    @classmethod
    def addi(cls, rf, rd, rs1, imm) -> None:
        rf[rd].value = rf[rs1].value + imm

    @classmethod
    def add(cls, rf, rd, rs1, rs2) -> None:
        rf[rd].value = rf[rs1].value + rf[rs2].value


def decode(inst: str) -> Instruction:
    inst = inst.replace(',', '').replace('x', '').split()
    match inst[0].upper():
        case 'ADDI':
            res = Instruction(
                RV32I.addi,
                {
                    'rd': int(inst[1]),
                    'rs1': int(inst[2]),
                    'imm': int(inst[3]),
                },
            )
        case 'ADD':
            res = Instruction(
                RV32I.add,
                {
                    'rd': int(inst[1]),
                    'rs1': int(inst[2]),
                    'rs2': int(inst[3]),
                },
            )
        case _:
            raise ValueError(f'Unsupported operator "{inst[0]}" in line {Instruction.cnt}')
    return res


if __name__ == '__main__':
    inst = Instruction(RV32I.addi, {'rd': 1, 'rs1': 1, 'imm': 0xffffffff})
    print(inst)
    inst = Instruction(RV32I.add, {'rd': 1, 'rs1': 1, 'rs2': 2})
    print(inst)
