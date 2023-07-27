class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        sumlist=[]
        for i in nums:
            print(i) 
            sum=sum+i
            sumlist.append(sum)
        return sumlist
