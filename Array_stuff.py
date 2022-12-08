class Array:
    def __init__(self, n=0):
        self.array_list = [0 for i in range(n)]
        self.length = n

    def set(self, index, item):
        self.array_list[index] = item

    def get(self, index):
        return self.array_list[index]

    def find(self, item):
        for i in self.array_list:
            if i == item:
                return item

    def max(self):
        max = self.array_list[0]
        for num in self.array_list:
            if num > max:
                max = num
        return max


    def min(self):
        min = self.array_list[0]
        for num in self.array_list:
            if num < min:
                num = min
        return min

    def sum(self):
        count = 0
        for num in self.array_list:
            count+=num
        return count

    def sort(self):
        index = 0
        for number in self.array_list:







