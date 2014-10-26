class ReversePolish:
    def __init__(self, tokens=[]):
        self.tokens = tokens;

    def evalRPN(self, tokens):
        s = []
        for i in tokens:
            if i == '+':
                a = s.pop()
                b = s.pop()
                s.append(a + b)
                print("%d + %d" % (a, b))
            elif i == '-':
                a = s.pop()
                b = s.pop()
                s.append(b - a)
                print("%d - %d" % (b, a))
            elif i == '*':
                a = s.pop()
                b = s.pop()
                s.append(a * b)
                print("%d * %d" % (a, b))
            elif i == '/':
                a = s.pop()
                b = s.pop()
                s.append(int(b*1.0 / a))
                print("%d / %d" % (b, a))
            else:
                s.append(int(i))

        return int(round((s.pop())))

if __name__ == "__main__":
    #tokens = ["2", "1", "+", "3", "*"]
    #tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(ReversePolish().evalRPN(tokens))
