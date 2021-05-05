class StringIterator:
    res = ""
    pointer, num = 0, 0
    ch = ' '
    def __init__(self, s: str):
        self.res = s
    def next(self) -> chr:
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.ch = self.res[self.pointer]
            self.pointer += 1
            while self.pointer<len(self.res) and self.res[self.pointer].isdigit:
                self.num = self.num * 10 + self.res[self.pointer] - '0'
                self.pointer += 1
        self.num -= 1
        return self.ch
    def hasNext(self) -> bool:
        return self.pointer != len(self.res) or self.num != 0
