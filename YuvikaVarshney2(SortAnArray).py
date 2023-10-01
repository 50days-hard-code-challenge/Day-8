"""def sortArray(arr, n):

	# Write your code here
	arr.sort()
"""
def sortArray(arr, n):
    
    zero = 0
    one = 0
    two = 0

    for i in range(n):
        if arr[i] == 0:
            zero += 1

        elif arr[i] == 1:
            one += 1

        else:
            two += 1


    index = 0

    while zero > 0:
        arr[index] = 0
        index += 1
        zero -= 1

    while one > 0:
        arr[index] = 1
        index += 1
        one -= 1

    while two > 0:
        arr[index] = 2
        index += 1
        two -= 1

  """
  def sortArray(arr, n):

    

    zeroPos = 0

    onePos = 0

    twoPos = n - 1



    while onePos <= twoPos:

        if arr[onePos] == 1:

            onePos += 1



        elif arr[onePos] == 0:

            arr[zeroPos], arr[onePos] = arr[onePos], arr[zeroPos]

            

            zeroPos += 1

            onePos += 1



        else:

            arr[onePos], arr[twoPos] = arr[twoPos], arr[onePos]

            

            twoPos -= 1
"""
