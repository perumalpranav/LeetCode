class Solution:
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        T = [0] * (n + 1)
        
        # Iterate from the end to the beginning
        for i in range(n, 0, -1):
            # Points from current question
            curr_points = questions[i-1][0]
            
            # Find the next available question after skipping brainpower
            next_question = i + questions[i-1][1] + 1
            
            # If next question is within array bounds, add its accumulated points
            if next_question <= n:
                curr_points += T[next_question]
            
            # Take max of current points or previous accumulated points
            T[i] = max(curr_points, T[i+1] if i+1 <= n else 0)
        
        return T[1]