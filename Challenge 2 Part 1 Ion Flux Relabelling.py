
def locate(top, num, left_deduction):
    # this allows us to find the left value of the tree
    # which is equal to (top_node-1)/2 starting from the topmost node
    left_deduction = left_deduction/2
    # right node is just top node -1
    right = top-1
    # left node is just top node - 1 - left deduction value
    left = top-1-left_deduction
    # if any of the right or left nodes match, then return the top node
    if right == num or left == num:
        return top
    # or recursively go through the left node if it's lower than the left node
    # this eliminates half the tree
    # go through right node if it's larger than the left node
    else:
        if num <= left:
            return locate(left, num, left_deduction)
        else:
            return locate(right, num, left_deduction)


def solution(h, q):
    # the top most value is 2 to the power h minus 1
    head = (2**h)-1
    result = []
    for i in range(len(q)):
        # make sure the values to be found are lower than the topmost node and greater than or equal to 1
        if q[i] < head and q[i] >= 1:
            # start with the topmost node and the first value in the array
            x = locate(head, q[i], head-1)
            result.append(x)
        else:
            # do this if the value to be found is outside the tree
            result.append(-1)
    return result
