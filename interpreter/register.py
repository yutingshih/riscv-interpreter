from typing import Any


class Register(object):
    def __init__(self, bits: int = 32, init: int = 0) -> None:
        self._bits = bits
        self._value = init

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        if value >> self._bits:
            raise ValueError(f'Attempt to assign an invalid value {value} (0x{value:x}) to a {self._bits}-bit register')
        self._value = value

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Register):
            return self.value == other.value
        if isinstance(other, int):
            return self.value == other
        raise TypeError(f'Attempt to compare {type(self)} with an invalid type {type(other)}')

    def __repr__(self) -> str:
        return f'0x{self.value:08x}'


if __name__ == '__main__':
    # initialization
    reg1 = Register(32, 0xffff)
    reg2 = Register(32, 0xccc)
    print(f'{reg1 = }\n{reg2 = }')
    print(f'{reg1 == reg2}')
    print('======')

    # getter/setter
    reg2.value = reg1.value
    print(f'{reg1 = }\n{reg2 = }')
    print(f'{reg1 == reg2}')
    print('======')

    # set invalid value
    try:
        reg2.value = 1 << 33
    except ValueError as e:
        print(f'ValueError caught: {e}')
        pass

    # compare with invalid type
    try:
        reg2 == 0.5
    except TypeError as e:
        print(f'TypeError caught: {e}')
        pass
