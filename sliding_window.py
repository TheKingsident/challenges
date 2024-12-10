# Challenge 1: Maximum Sum Subarray of Size K:
# Find the maximum sum of any subarray of size K in a given array.
def chl1_max_sum_sub_array(array, k):
    max_sum = float('-inf') #Initialize this to track the max sum
    current_sum = sum(array[:k])  #Initialize this to track the current sum

    for i in range(len(array) - k):
        #Slide the window by adding the entering element and removing the leaving element
        current_sum = current_sum + array[k + i] - array[i]
        max_sum = max(current_sum, max_sum)  #Update the meximum

    return max_sum

# Challenge 2: Longest Subarray with Sum Less Than or Equal to K:
# Find the length of the longest subarray whose sum is ≤ K.
def chl2_longest_sub_array_k_sum(array, k):
    current_sum = 0
    max_length = 0
    start = 0

    for i in range(len(array)):
        current_sum += array[i]
        if current_sum > k and start <= i:
            current_sum -= array[start]
            start += 1

    max_length = max(max_length, i - start + 1)g

