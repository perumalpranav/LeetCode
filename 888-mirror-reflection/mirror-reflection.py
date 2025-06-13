class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        LCM = p
        traveled = 1
        while LCM % q != 0:
            LCM += p
            traveled += 1

        if traveled % 2 == 1:
            #1 or 2
            if (LCM / q) % 2 == 0:
                return 2
            else:
                return 1
        else:
            #0 or keep going??
            if (LCM / q) % 2 == 1:
                return 0
            else:
                return 1


        #Determine if ray hits a sensor
        #IF it does return sensor
        #Else, find new angles/sides to input back in to the function