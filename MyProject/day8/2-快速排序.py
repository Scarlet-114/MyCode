
import random
class Sort:
    def __init__(self,n):
        '''
        :param n:排序的数的数量
        '''
        self.arr=[0]*n
        self.random_data()
    def random_data(self):
        for i in range(len(self.arr)):
            self.arr[i]=random.randint(1, 99)

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)

    def partition(self, left, right):
        k=i=left
        for i in range(left, right):
            if self.arr[i]<self.arr[right]:
                self.arr[i],self.arr[k]=self.arr[k],self.arr[i]
                k+=1
        self.arr[k],self.arr[right]=self.arr[right],self.arr[k]
        return k

if __name__=='__main__':
    n = 10
    sort_list = Sort(n)
    sort_list.quick_sort(0,n-1)
    print(sort_list.arr)