import random,sys

def main():
    e= [ 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30,
            45 ] # answer = 590
    numbers = [3,8,2,5,1,4,7,6]
    #parse file
    array = []
    print sys.argv[1]
    myfile = sys.argv[1]
    with open(myfile) as ty:
        for line in  ty:
            array.append(int(line.strip()))
    #print array
    for item in array:
        assert (type(item)==int)
    print 'FIRST'
    qs = quicksort('first')
    my_array = qs.choose_pivot(array)
    print '    number of recursive calls: ', qs.recursive_calls
#    print 'SECOND'
#    qs = quicksort('second')
#    my_array = qs.choose_pivot(array)
#    print '    number of recursive calls: ', qs.recursive_calls
#    print 'MEDIAN'
#    qs = quicksort('median')
#    my_array = qs.choose_pivot(array)
#    print '    number of recursive calls: ', qs.recursive_calls
#
#
class quicksort():
    
    def __init__(self,method):
        self.recursive_calls = 0
        self.method = method
        pass 
    def choose_pivot(self, array):

        array_length = len(array)

        if array_length <= 1:
            return array
        else:
            #choose pivot
            #pivot = random.choice(array)
            #array[0] = pivot
#            if self.method == 'first':
#                pivot = array[0]
            #elif self.method == 'second':
            #pivot = array[-1]
            #put pivot at the beginning of array
            a = array[0]
            b = array[-1]
            c = array[array_length/2]
            mi = min(a,b,c)
            ma = max(a,b,c)
            for i in [a,b,c]:
                if i != mi or i != ma:
                    pivot = i
            pivot_index = array.index(pivot)
            array[pivot_index] = array[0]
            array[0] = pivot

            left,right = self.partition_around_pivot(array,pivot)
            sorted_left = self.choose_pivot(left)
            sorted_right = self.choose_pivot(right)
            sorted_left.append(pivot)
            sorted_array = sorted_left + sorted_right
            return sorted_array
        


    def partition_around_pivot(self, array, pivot):
        self.recursive_calls += len(array) - 1
        i = 1
        for j in xrange(1,len(array)):
            if array[j] < pivot:
                i_temp = array[i]
                j_temp = array[j]
                array[i] = j_temp
                array[j] = i_temp
                i +=1
        array[0] = array[i-1]
        array[i-1] = pivot 

        left = array[:i-1]
        right = array[i:]

        return left, right


if __name__ == '__main__':
    main()
