
test = ">--<-<-><"

# answer - 8


def solution(test):
    score = 0
    right_counter = 0
    for char in test:
        if char == ">":
            right_counter += 1
        if char == "<":
            score += right_counter*2
    return score

# print(solution(test))
