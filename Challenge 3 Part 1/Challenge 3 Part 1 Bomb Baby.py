# This method doesn't work for some reason
# even though right answers are outputed

import math
def solution_unused(x, y):
    M = int(x)
    F = int(y)
    generations = 0
    if M > 1 or F > 1:
        while True:
            # print("generations: ", generations)
            # print("M: ", M, "F: ", F)
            if M is 0 or F is 0:
                return str(generations-1)
            if M > F:
                # print("M>F")
                # print("M =",M,"F =",F)
                if M % F ==0 and F is not 1:
                    return "impossible"
                generations += math.floor(M / F)
                # print("generations after = ", generations)
                M = M % F
                # print("M now=",M,"F =",F)
                # print("M>F")
            elif M < F:
                # print("M<F")
                # print("M =",M,"F =",F)
                # print("generations before = ", generations)
                if F % M == 0 and M is not 1:
                    return "impossible"
                generations += math.floor(F / M)
                # print("generations after = ", generations)
                F = F % M
                # print("F<M")
                # print("M =",M,"F now =",F)
            elif (M == 1) and (F == 1):
                # print("M =",M,"F =",F)
                return str(generations)
            elif M == F:
                # print("F=M")
                return "impossible"
            # else:
            # return "Error"

"""
Suppose M > F, to hit (M, F), last state must be (M-F, F).
We can use Euclidean algorithm to calcualte the generations
from (M, F) down to (1, 1)
A simple case: (1, 1)-(2, 1)-(3, 1)-(3, 4)-(7, 4)
Impossible Case: gcd(M, F) != 1
"""


def solution(M, F):
    x, y = int(M), int(F)
    count = 0
    while y >= 1:
        if x < y:
            x, y = y, x
        x, y, q = y, x % y, x // y
        count += q
    return str(count - 1) if x == 1 else "impossible"
