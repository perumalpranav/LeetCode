class Solution:
    def maxValue(self, n: str, x: int) -> str:
        nArray = list(n)
        if not nArray[0] == '-':
            #Value of x
            #Iterate --> 
            #When x is > current position digit insert x there
            inserted = False
            for i,c in enumerate(nArray):
                if x > int(c):
                    nArray.insert(i,str(x))
                    inserted = True
                    break
            
            if not inserted:
                nArray.append(str(x))

        else:
            #Value of x
            #Iterate --> 
            #When x is < current position digit insert x there
            nArray.pop(0)
            inserted = False
            for i,c in enumerate(nArray):
                if x < int(c):
                    nArray.insert(i,str(x))
                    inserted = True
                    break
            
            if not inserted:
                nArray.append(str(x))

            nArray.insert(0,'-')

        return ''.join(nArray)




        