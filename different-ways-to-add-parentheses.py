class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def compute(expr):
            if expr in memo:
                return memo[expr]
            if expr.isdigit():
                return [int(expr)]
            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])
                    
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            elif char == '*':
                                results.append(left * right)
            
            memo[expr] = results
            return results
        
        return compute(expression)
            
