import heapq
# two ways to import data to heap,:
# 1. one by one
heap=[]
for n in range(5):
	heapq.heapush(heap,n)

#2.from list
data = [19,12,32,1,2,3]
heapq.heapify(data)
#access data in heap
while data:
	print smallest = heapq.heappop(data)
# replace the existing new smallest element with new element
heapq.heapreplace(data,newval) # return the old smallest element
