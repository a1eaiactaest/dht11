import time
from typing import List, TypeVar

WOItem = TypeVar('WOItem', int, float, str)


class WO:
    """
    Weather Object
    """

    def __init__(self, *args: str) -> None:
        self.args = args

        self.millis = args[0]
        self.id = args[1]
        self.pres = args[2]
        self.gas_res = args[3]
        self.air_te = args[4]
        self.air_hu = args[5]
        self.gnd_te = args[6]
        self.gnd_hu = args[7]

    def valid(self) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        return str(self.args)

    def __getitem__(self, key: int) -> WOItem:
        return self.args[key]


if __name__ == "__main__":
    dat = ['1647986911252', '103', '1009.00',
           '120.00', '20.00', '52.00', '2.00', '87.00']
    x = WO(*dat)
