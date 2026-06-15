class Solution:
    def max_meetings(self,start, end):
        # store meetings as (end, start, index) and then sort it by end time  
        meeting = [(end[i], start[i],i+1) for i in range(len(start))]
        meeting.sort()

        result = []
        last_end= -1 

        # traverse the meeting 
        for e, srt, indx in meeting :
            if srt > last_end :
                result.append(indx)
                last_end = e
        return result 
start = [1, 4, 3, 0, 5, 8, 5]
end   = [2, 8, 4, 6, 7, 9, 9]
s1 = Solution()
print(s1.max_meetings(start, end))