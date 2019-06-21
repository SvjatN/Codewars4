"""
Given an array of integers.
Return an array, where the first element is the count 
of positives numbers and the second element is sum of negative numbers.
If the input array is empty or null, return an empty array.
"""

def count_positives_sum_negatives(arr):    
    count_of_positive_num = 0
    #count_of_negative_num = 0

    list_of_positive_num = []
    list_of_negative_num = []

    for i in arr:
        if i == 0:
            continue
        elif i<0:
            list_of_negative_num.append(i)
        elif i>0:
            count_of_positive_num = count_of_positive_num+1
    
    list_of_positive_num.append(count_of_positive_num)
    
    list_of_negative_num2 = []
    list_of_negative_num2.append(sum(list_of_negative_num))
    
    result_list = []
    
    if arr == []:    
        return result_list
    else:
        result_list.append(list_of_positive_num[0])
        result_list.append(list_of_negative_num2[0])
           
        return result_list


