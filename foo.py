class handler:
    def awu(self):
        self.data[0] += 1
        return 'miao'
    
    data = [1, 2, 3]

class B(handler):
    def ying(self):
        self.data[1] += 1
        print('ying')