def heapsort(unsorted):
   n= len(unsorted)
   for i in range(n//2-1,-1,-1): #n//2-1이 의미하는 바는 힙의 자료구조에서 마지막으로 오는 원소의 부모 라인의 노드 index를 말합니다.
       heapify(unsorted, i, len(arr))
#이제 최대 힙을 구성하였고 아래에서 정렬이 시작됩니다.
   for i in range(n-1,0,-1):
       unsorted[0], unsorted[i]=unsorted[i], unsorted[0] #가장 최대인 unsorted[0]을 배열의 가장 뒤로 보내줍니다.
       heapify(unsorted, 0, i) #이후 맨 마지막 원소를 빼고 다시 최대 힙을 구성합니다.

def heapify(unsorted, index, heap_size): #최대 힙을 만들어주는 함수

   largest=index   #부모와 자식 노드의 index간에 성립하는 식입니다.
   left=index*2+1
   right=index*2+2

   if left<heap_size and unsorted[left]>unsorted[largest]:
       largest=left

   if right<heap_size and unsorted[right]>unsorted[largest]:
       largest=right

   if largest!=index:
       unsorted[index],unsorted[largest]=unsorted[largest],unsorted[index]
       heapify(unsorted, largest, heap_size)
#재귀를 이용해서 구현해줍니다.
#하지만 이렇게 하면 힙의 자료구조에서 한 줄을 따라서만 대소관계를 비교해서 위치를 바꿔주기 때문에
#반복문을 사용하여 heapify함수를 이용해서 완전하게 최대 힙을 만들 수 있습니다.

import sys
arr=[]

for i in range(int(input())):
   arr.append(int(sys.stdin.readline()))
   #이렇게 반복해서 입력값을 받는 경우 sys.stdin.readline함수가 running time을 절약할 수 있습니다.

heapsort(arr)

for i in arr:
   print(i)