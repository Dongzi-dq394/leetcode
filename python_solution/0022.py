class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(string, opening, closing, res):
            if opening < 0 or closing < 0: return
            if opening == 0 and closing == 0:
                res.append(string)
                return
            if opening == closing:
                generate(string+'(', opening-1, closing, res)
            else:
                generate(string+'(', opening-1, closing, res)
                generate(string+')', opening, closing-1, res)
        generate('', n, n, res)
        return res