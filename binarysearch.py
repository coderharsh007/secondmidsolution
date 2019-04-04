def binary_search(A,L,H,K):
	if L<=H:
		mid = int(L + (H-L)/2)
		if A[mid]==K:
			return True
		elif A[mid] >K:
			return binary_search(A,L,mid-1,K)
		elif A[mid] < K:
			return binary_search(A,mid+1,H,K)
	else:
		return False
		
B=[2,4,8,90,328,24,35,859,812,38,98913,98,981,84,21,1]
B.sort()
K=int(input('enter the value'))
result = binary_search(B,0,len(B)-1,K)
print(result)
