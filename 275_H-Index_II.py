def hIndex(citations):
        paper_num = len(citations) 
        left = 0
        right = paper_num - 1 
        while right >= left:
            mid = (right + left)//2
            if citations[mid] > paper_num - mid:
                right = mid - 1
            if citations[mid] < paper_num - mid:
                left = mid + 1
            if citations[mid] == paper_num - mid:
                return citations[mid]
        return paper_num -left

hIndex([0,1,2,3,4])
hIndex([0])
hIndex([0,0,0,0])
hIndex([100])

