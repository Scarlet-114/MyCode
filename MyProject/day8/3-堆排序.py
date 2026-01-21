
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

    def heap_sort(self):
        arr_len=len(self.arr)
        #把堆调整为大根堆
        for i in range(arr_len//2-1, -1, -1):
            self.adjust_heap(i, len(self.arr))

        #排序
        while(arr_len>1):
            #交换堆顶和堆底元素
            self.arr[0], self.arr[arr_len-1] = self.arr[arr_len-1], self.arr[0]
            arr_len = arr_len - 1
            # 调整堆顶
            self.adjust_heap(0, arr_len)




    def adjust_heap(self, pos, arr_len):
        father  = pos
        son = 2*father + 1
        while son<arr_len:
            if son+1 < arr_len and self.arr[son] < self.arr[son+1]:
                son = son+1
            if self.arr[father] < self.arr[son]:
                self.arr[father], self.arr[son] = self.arr[son], self.arr[father]
                father = son
                son = 2*father + 1
            else:
                break


if __name__ == '__main__':
    sort1 = Sort(10)
    sort1.heap_sort()
    print(sort1.arr)