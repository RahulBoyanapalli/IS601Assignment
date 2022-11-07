a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    if type(arr[0])!=str:
        Positive_Output=[-1*odd if (odd)<0 else (odd) for odd in arr ]
    else:
        b=[int(ine) for ine in arr]
        Positive_Output=[odd[1:] if odd.startswith('-') else (odd) for odd in a4 ]
    print(Positive_Output)


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)