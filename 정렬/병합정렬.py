# 병합 정렬 
# 1. 배열 절반으로 나누기
# 2. 중간 지점을 mid라 할때, mid = (lt+rt)//2
# 3. D(lt, rt) -> D(lt, mid), D(mid+1, rt) 두 갈래로 호출
# 4. 그 후 그 밑에서 넘어온 범위의 자료를 두 영역으로 나눈 그 영역을 합치는 작업을 한다.
# 5. 위 과정을 반복
# 6. TEMP에 두개의 값을 비교해서 작은거부터 넣는다.

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2
        Dsort(lt, mid)
        Dsort(mid + 1, rt)
        p1 = lt
        p2 = mid + 1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        if p1<=mid:tmp=tmp+arr[p1:mid+1]
        if p2<=rt:tmp=tmp+arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt+i]=tmp[i]


if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before sort : ", end='')
    print(arr)
    Dsort(0, 7)
    print(arr)
    print("After sort : ", end='')
    print(arr)
