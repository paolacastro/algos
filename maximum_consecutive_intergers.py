array = [-3,4,-1,2,1,-5]

def find_max_consecutive_numbers(array):
    l = len(array)
    end = l -1
    j = 0
    i = 1
    max_sum = array[0]
    max_array = array[0:1]
    for j in range(0,l):
        while i != l + 1:
            to_compare = array[j:i]
            #print to_compare
            to_compare_sum = sum(to_compare)
            if to_compare_sum > max_sum:
                max_sum = to_compare_sum
                max_array = to_compare
            i += 1
        i = j+1
    return max_array, max_sum
def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        print x
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print max_ending_here, max_so_far
    return max_so_far

            
print find_max_consecutive_numbers(array)
print max_subarray(array)


