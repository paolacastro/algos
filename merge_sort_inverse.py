#
import sys,os
def main():
        practice_list = [2,1,5,3,6,4]
        e= [ 37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30,
            45 ] # answer = 590
        d = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63,
             97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61,
             31, 85, 33, 54 ] #d_answer = 2372
        f = [ 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 ] # answer = 56
        A = [5,4,3,2,1]# answer = 10
        B = [1,3,5,2,4,6]# answer = 
        C = [1,2,3,4,5,6]# answer = 0
        D = [1,5,6,2,3,4]# answer = 6
        E = [2,1,3,5,4,6]# answer = 2
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
        # do the merge sorty thing
        merge_object = myclass()
        merged_list= merge_object.merge_sort(array)
        print merged_list
        print 'INVERSION TOTAL = ', merge_object.inverse_count
        #print 'finally',merged_list
        

class myclass():

    def __init__(self):
        self.inverse_count = 0

    
    def merge_sort(self,array):
        
        array_length = len(array)
        
        if array_length <= 1:
            return array
        else:
            n = len(array)
            left_array = array[:n/2]
            right_array = array[n/2:]
            left_array = self.merge_sort(left_array)
            right_array = self.merge_sort(right_array)
            sorted_list, inverse_count_local = self.inverse_sort_and_count(left_array, right_array)
            #inverse_count_local += inverse_count_local
            #print 'sorted_list: ', sorted_list
            print 'inverse_count_local: ', inverse_count_local
            self.inverse_count += inverse_count_local
            return sorted_list
        
    def inverse_sort_and_count(self,A,B):

        i,j = 0,0
        inverse_count_local = 0
        sorted_list = []
        #print 'A', A
        #print 'B', B
        
        while i < len(A) and j < len(B):
    #    for i in range(n):
            if A[i] < B[j]:
                sorted_list.append(A[i])
                i += 1
            else: # B[j] < A[i]
                sorted_list.append(B[j])
                # inverse count increases by all the left in A because they are sorted
                inverse_count_local += len(A[i:])
                j += 1

        if i!=len(A): # did not get to the end of A
            #print 'I went in here!' 

            #inverse_count_local +=len(A)-1
            
            for item_left in A[i:]:
                sorted_list.append(item_left)
        
        else: # did not get to the end of B
            for item_left in B[j:]:
                sorted_list.append(item_left)
        
        return sorted_list, inverse_count_local
main()
