class RegEx:

    def is_match(self, s, p):
        sPass = 0
        pPass = 0
        sub = None
        match = -1
        while sPass < (len(s) - 1) and pPass < (len(p) - 1):
            if p[pPass] == '(':
                sub = self.get_substr(p[pPass+1])
                if sub is None:
                    return None
                pPass += (len(sub)+2)
                #This should appropriately move the index
            elif p[pPass] == '*':
                    print("Error, should have avoided this!");
                    exit(1)
            else:
                sub = p[pPass]
                pPass += 1
            if p[pPass] == '*':
                #Should have marked the examined substring as passed already
                pPass += 1
                match = self.match_star(s[sPass:], sub, len(p) - (len(sub) + pPass))
            else:
                match = self.is_subMatch(s[sPass:], sub)
            if match != -1:
                sPass += match
            else:
                return False

    def is_subMatch(self, s, p, sPass, pPass):

        while sPass < (len(s) - 1) and pPass < (len(p) - 1):
            if p[pPass] == '(':
                self.is_match_parenthesis(s, p, sPass, pPass+1)

    def get_substr(self, p):
        start = self.pPass
        while self.pPass < len(p):
            if p[self.pPass] != ')':
                self.pPass += 1
            else:
                return p[start:self.pPass]
        return None

    def match_star(self, s, sub, cut):
        stars = 0
        footer = cut + ((len(s) - cut) % len(sub))
        for i in range(len(s) - cut, len(sub)):
            stars += 1 if self.isMatch(s[i:footer], sub) else 0
            #Going to have to test this for any off by ones
        return stars


