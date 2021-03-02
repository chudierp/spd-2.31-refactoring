# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

def print_stat():
    '''Prints Statistics'''
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
        
    mean = calculate_mean(grade_list)
    sd = calculate_std(grade_list, mean)

    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')
    
    return grade_list 

print_stat()
