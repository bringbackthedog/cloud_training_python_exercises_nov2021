# See: https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/

# Get the largest number in an array.
# If a non int is passed, show appropriate error.
def get_largest(int_list):
    largest = int_list[0]

    try:
        for num in int_list:
            if(type(num) != int):
                raise TypeError('{} is not int'.format(num))

            if(num > largest):
                largest = num

    except TypeError as e:
        print(e)

    else:
        return largest
        # print(largest)


#
int_list = [5, 9, 8, 35, 64, 1, 6, 50]
largest = get_largest(int_list)

# print only if a value is returned ie no errors
if(largest):
    print(largest)


int_list_with_error = [5, 'a', 9, 8, 35, 64, 1, 6, 50]
largest_with_error = get_largest(int_list_with_error)

# print only if a value is returned ie no errors
if(largest_with_error):
    print(largest_with_error)