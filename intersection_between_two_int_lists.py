a = [1,2,3,4]
b = [-1,0,1,2]

for i_a, i in enumerate(a):
    for j_b,j  in enumerate(b):
        if i == j:
            i_a += 1
            j_b += 1
            print i,j
            break

intersection = True

#while intersection:
#    if a[i_a] == b[j_b]:
#        print a[i_a],b[j_b]
#        i_a += 1
#        j_b += 1
#    else:
#        intersection = False

