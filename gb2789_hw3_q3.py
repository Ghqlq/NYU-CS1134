
#question 3

def find_duplicates(lst):
    duplicates = []
    count = [0]*(len(lst))
    for i in range(len(lst)):
        count[lst[i]] += 1
    for i in range(len(count)):
        if count[i] > 1:
            duplicates.append(i)
    return duplicates

   
    
