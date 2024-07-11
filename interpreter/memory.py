class Memory(object):
    def __init__(self, size: int = 1024, addr: int = 0) -> None:
        self.SIZE = size
        self.ADDR = addr
        self.data = [0] * size

    def validate_address(self, addr: int) -> int:
        offset = addr - self.ADDR
        if not 0 <= offset < self.SIZE:
            raise IndexError(f'Invalid memory access to 0x{addr:08x}')
        return offset

    def validate_value(self, val: int) -> int:
        if val >> 8:
            raise ValueError(f'Invalid memory write with value {val}')
        return val

    def __getitem__(self, addr: int) -> int:
        return self.data[self.validate_address(addr)]

    def __setitem__(self, addr: int, val: int) -> None:
        self.data[self.validate_address(addr)] = self.validate_value(val)


if __name__ == '__main__':
    # basic read/write
    mem = Memory(addr=32, size=32)
    for i in range(32, 32+32):
        mem[i] = i
    print(mem[32])
    print(mem[33])
    print(mem[34])

    # invalid address
    try:
        print(mem[128])
    except IndexError as e:
        print(f'{e}')
        pass

    # invalid value
    try:
        mem[50] = 1 << 10
    except ValueError as e:
        print(e)
        pass
