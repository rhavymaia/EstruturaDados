def quickSort(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSort(alist,first,splitpoint-1)
       quickSort(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

def main():
  alist = [54,26,93,17,77,31,44,55,20]
  first = 0
  last = len(alist) - 1
  quickSort(alist, first, last)
  print(alist)

if (__name__=="__main__"):
  main()
