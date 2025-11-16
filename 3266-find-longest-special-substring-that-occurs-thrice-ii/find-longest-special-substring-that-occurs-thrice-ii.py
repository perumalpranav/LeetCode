from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        #Basic Solution
        #Iterate through all possible susbtrings (use length as iterator)
        #Store every substring in a HashTable, with the value being its occurences
        #If a substring ever occurs thrice, break early and consider next length
        #Important! if 3 is not posssible for length k, it is also not possible for k+1

        #Better solution
        #Store the string as a compressed string
        #Store as array of lists [("character",num_repeats),...]
        #Iterate through this array, and count occurences
        #Will have to separate long runs if num_repeats > considered_length (division?)

        #Even Better Solution
        #For each character run, store the best we can do, and how many
        #If we can do better, use the current value to retroactively calculate how many we could do?

        def updateoccurences(occurences, character, repeats, length):
            if repeats < length:
                return (False, occurences)
            elif repeats == length:
                occurences[character] += 1
                if occurences[character] >= 3:
                    return (True, occurences)
                else:
                    return (False, occurences)
            else:
                numtimes = (repeats + 1) - length 
                occurences[character] += numtimes
                if occurences[character] >= 3:
                    return (True, occurences)
                else:
                    return (False, occurences)

        compressed = []
        bestcompression = 1
        for c in s:
            if len(compressed) > 0 and c == compressed[-1][0]:
                compressed[-1][1] += 1
                bestcompression = max(bestcompression, compressed[-1][1])
            else:
                compressed.append([c, 1])
        

        if bestcompression < 3:
            best = -1
            start = 1
        else:
            best = bestcompression - 2
            start = best + 1

        for l in range(start,(len(s)-1)):
            satisfied = False
            occurences = defaultdict(int)
            i = 0


            while i < len(compressed):
                c, num_repeats = compressed[i]
                
                if num_repeats < l:
                    compressed.pop(i)
                    continue

                satisfied, occurences = updateoccurences(occurences, c, num_repeats, l)
                if satisfied:
                    break
                
                i += 1


            if satisfied:
                best = l
            else:
                return best
        return best

        