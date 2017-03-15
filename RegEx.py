import sys


class RegEx:

    def is_submatch(self, s, p):
        spass = 0
        i = 0
        increment = 0
        while i < (len(p)):
            #remember edge case for final char!!!
            if p[i] == '(':
                sub = self.get_substr(p[i+1:])
                if sub is None:
                    print(sub)
                    return -1
                    #Or maybe continue?
                i += (len(sub)+2)
                #right increment?
            elif p[i] == '*':
                print("Error, should have avoided this!")
                exit(1)
            else:
                sub = p[i]
                i += 1
            if i < len(p) and p[i] == '*':
                #Should have marked the examined substring as passed already
                i += 1
                #print(s[spass:(len(s) - (len(p) - i))])
                print(i, s, spass, sub)
                spass += self.match_star(s[spass:], sub)
                print(i, s, spass)
            elif len(sub) == 1:
                if sub != '.' and sub != s[spass]:
                    print("char doesn't match!", sub, s[spass], spass)
                    return -1
                else:
                    spass += 1
            else:
                print("Making a recursive call.....")
                increment = self.is_submatch(s[spass:spass+len(sub)], sub)
                if increment == -1:
                    return -1
                else:
                    spass += increment
        print(spass)
        return i if spass == len(s) else -1

    def get_substr(self, p):
        for ind in range(len(p)):
            if p[ind] == ')':
                return p[:ind]
        print("Parenthesized substring not found in", p)
        return None

    def match_star(self, s, sub):
        str = 0
        footer = len(s) % len(sub)
        s = s[:(len(s) - footer)]
        print(len(s))
        for i in range(0, len(s), len(sub)):
            print(s[i:])
            if self.is_submatch(s[i:], sub) != -1:
                str += len(sub)
            else:
                return str
        return str

    def main(self):
        exp = input("Please enter the regular expression to match to:")
        string = input("Now please enter the string to match to it:")
        if self.is_submatch(string, exp) != -1:
            print("The string is a match!")
        else:
            print("The string is not a match!")

matcher = RegEx()
matcher.main()



