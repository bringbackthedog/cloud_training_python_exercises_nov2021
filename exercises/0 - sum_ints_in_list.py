# Write a function that sums all the integers in a list. Return the sum. 
#
#  e.g. `sum_ints([2,4,6,8])` should return 20

def sum_ints(int_list):
    sum = 0 

    for i in int_list:
        sum += i

    return sum



int_list = [2,4,6,8]

print(sum_ints(int_list))

# OR
# 
# using standard libraries
print(sum(int_list))