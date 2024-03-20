class circularfirstinfirstout():
    def __init__(self, targetLength):
        self.buffer = []
        self.pointer = 0
        self.targetLength = targetLength
    def add(self, value):
        if self.targetLength > 0:
            self.buffer.append(value)
            self.targetLength -= 1
        else:
            self.buffer[self.pointer] = value
            self.pointer += 1
            if self.pointer == len(self.buffer):
                self.pointer = 0
        print(self.buffer)
    def read(self, distance=None):
        modulePointer = self.pointer
        output = []
        if distance == None:
            distance = len(self.buffer)
        output.append(self.buffer[modulePointer])
        modulePointer += 1
        if modulePointer == len(self.buffer):
            modulePointer = 0
        distance = distance - 1
        if distance == 0:
            return output