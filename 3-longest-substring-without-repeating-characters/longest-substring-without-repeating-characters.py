class Solution(object):

    def compressor(self, s):
        cstring = ""
        index = 0
        while index < len(s):
            cstring += s[index]
            if cstring[0] == s[index] and index != 0:
                cstring = cstring[:len(cstring)-1]
                parts = s.split(cstring)
                print(parts)
                i = 0
                while i < len(parts):
                    if(parts[i] == ''):
                        parts.pop(0)
                    else:
                        return cstring + cstring.join(parts)
                return cstring
            index+=1
        return cstring
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = self.compressor(s)
        letters = {}
        count = 0
        length = 0
        i = 0
        while i in range(len(s)):
            #print("index: " + str(i) + " " + s[i] + " " + str(count) + " " + str(length))
            #print(letters)
            if(letters.get(s[i]) != None):
                if(count > length):
                    length = count
                count = 0
                #print(letters)
                i = letters.get(s[i]) + 1
                letters.clear()
            else:
                letters[s[i]] = i
                count+=1
                i+=1
        if(count > length):
            length = count
        return length