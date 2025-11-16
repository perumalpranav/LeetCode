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

        compressions = defaultdict(list)
        char = s[0]
        num_repeats = 1
        for c in s[1:]:
            if c == char:
                num_repeats += 1
            else:
                compressions[char].append(num_repeats)
                char = c
                num_repeats = 1
        compressions[char].append(num_repeats)

        best = 0
        for letter, compression_lengths in compressions.items():
            compression_lengths = sorted(compression_lengths, reverse=True)
            if len(compression_lengths) == 1:
                if compression_lengths[0] >= 3:
                    best = max(best, compression_lengths[0] - 2)
            elif len(compression_lengths) == 2:
                if compression_lengths[0] > compression_lengths[1]:
                    best = max(best, max(compression_lengths[0] - 2, compression_lengths[1]))
                else:
                    best = max(best, compression_lengths[0] - 1)
            else:
                if compression_lengths[0] > compression_lengths[1]:
                    best = max(best, max(compression_lengths[0] - 2, compression_lengths[1]))
                else:
                    best = max(best, compression_lengths[0] - 1)
                
                best = max(best, compression_lengths[2])

        if best == 0:
            return -1
        
        return best


        