import itertools


def maxSumDivThree(nums):
    divThree = []

    for i in range(len(nums)+1):
        for j in itertools.combinations(nums,i):
            print(j)
            if sum(j) % 3 == 0:
                
                divThree.append(sum(j))

    return max(divThree)

print(maxSumDivThree([366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]))
