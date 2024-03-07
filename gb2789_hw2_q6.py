

#Question 6

def two_sum(srt_lst, target):
    for i in range(len(srt_lst)):
        if target - srt_lst[i] in srt_lst:
            num2 = srt_lst.index(target-srt_lst[i])
            return i, num2


