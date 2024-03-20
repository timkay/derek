import linked_list

class linkedListFIFO(linked_list.linkedListController):
    def __init__(self, targetLength):
        super().__init__()
        self.remaining = targetLength
        self.setup = False
    def add(self, value):
        if self.setup:
            if self.remaining == 0:
                self.shift()
            self.append(value)
            self.head.print()
        else:
            self.sentinel.add(value)
            self.setup = True