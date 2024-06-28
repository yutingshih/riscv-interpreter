from instruction import decode
from register import Register


def dump_regfile(regfile: list[Register], verbose: bool = False) -> str:
    info = ''
    for idx, reg in enumerate(regfile):
        info += f'{idx:02d}: '
        info += f'{reg}'
        info += f'{'\t' if idx % 8 < 7 else '\n'}'
    info += '-' * 126 + '\n'
    if verbose:
        print(info, end='')
    return info


def main():
    rf = [Register(32, 0) for _ in range(32)]
    dump_regfile(rf, True)

    while (cmd := input()) != 'halt':
        inst = decode(cmd)
        print(inst)
        inst(rf)
        dump_regfile(rf, True)


if __name__ == '__main__':
    main()
