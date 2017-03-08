import sys

class RegEx:

    def main(self):
        exp = input("Please enter the regular expression to match to:")
        string = input("Now please enter the string to match to it:")
        print(self.is_submatch(string, exp))

    def is_submatch(self, s, p):
        spass = 0
        for i in range(len(p)-1):
            #remember edge case for final char!!!
            if p[i] == '(':
                sub = self.get_substr(p[1:])
                if sub is None:
                    return False
                    #Or maybe continue?
                i += (len(sub)+1)
                #right increment?
            elif p[i+1] == '*':
                print("Error, should have avoided this!")
                exit(1)
            else:
                sub = p[i]
            if p[i] == '*':
                #Should have marked the examined substring as passed already
                spass += self.match_star(s[spass:], sub, len(p) - len(sub))
            elif p[i] != ('.' or s[spass]):
                return False
            else: spass += 1
            if spass == len(s): return True

    def get_substr(self, p):
        start = self.pPass
        while self.pPass < len(p):
            if p[self.pPass] != ')':
                self.pPass += 1
            else:
                return p[start:self.pPass]
        return None

    def match_star(self, s, sub, cut):
        str = 0
        footer = cut + ((len(s) - cut) % len(sub))
        for i in range(len(s) - cut, len(sub)):
            if self.isMatch(s[i:footer], sub):
                str += 1
            else:
                return str
        return str

    main()


