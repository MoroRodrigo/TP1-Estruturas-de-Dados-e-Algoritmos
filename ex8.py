def bubbleSort(self):
    left = 0
    right = self.__nItems - 1
    
    while left < right:
        for inner in range(left, right):
            if self.__a[inner] > self.__a[inner + 1]:
                self.swap(inner, inner + 1)
        
        right -= 1


        for inner in range(right, left, -1):
            if self.__a[inner] < self.__a[inner - 1]:
                self.swap(inner - 1, inner)

        left += 1
