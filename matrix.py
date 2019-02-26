class Matrix:

    def __init__(self, w=None, k=None):
        self.w = w
        self.k = k
        self.items = []

    def push(self, data):
        self.items.append(data)


class Operations:

    def __init__(self, A=None, B=None):
        self.A = A
        self.B = B
        self.sum = 0
        self.determinant_result = []

    def adding(self):
        result=[]
        if A.w == B.w and A.k == B.k:
            for x in range(A.w*A.k):
                result.append(A.items[x]+B.items[x])
        return result

    def multiplying(self):
        result = []
        if A.k == B.w:
            for z in range(A.w):
                for x in range(B.k):
                    sum = 0
                    for y in range(B.w):
                        sum += (A.items[z*A.k+y]*B.items[y+A.k*x])
                    result.append(sum)
            return result

    def determinant(self, W):
        lastcol = None
        sum = 0
        s=1
        if W.k == W.w:
            if W.k == 2:
                if self.determinant_result!=[]:
                    for x in self.determinant_result:

                        s *= x
                    sum += W.items[0] * W.items[3] - (W.items[1] * W.items[2])
                    sum *= s
                else:
                    sum += W.items[0]*W.items[3]-(W.items[1]*W.items[2])
                return sum
            # sprawdzamy czy i nie jest zerem jeśli jest zostawiamy i przechodzimy do następnej kolumny
            # w innym przypadku szukamy numbe w tym wierszu która nie jest zerem i nią odejmujemy tą kolumnę
            for i in range(W.k):
                if W.items[i] != 0:
                    number = None

                    for x in range(i+1, W.k):
                        if W.items[x] != 0:
                            number = x
                            lastcol = x
                    if lastcol == None:
                        lastcol = W.k-1
                    if number == None:
                        # okrajanie macirzy
                        # górny wiersz
                        if lastcol%2==0:
                            self.determinant_result.append(W.items[lastcol])
                        else:
                            self.determinant_result.append(-W.items[lastcol])
                        for x in range(W.k):
                            W.items.pop(0)
                        # kolumna
                        for x in range(W.w-1):
                            W.items.pop(lastcol+x*(W.w-1))

                        W.k-=1
                        W.w-=1
                        return self.determinant(W)
                    num = 1 * W.items[i]
                    num2 = 1 * W.items[number]
                    for j in range(W.w):

                        W.items[i+W.w*j] -= W.items[number+W.w*j]*(num/num2)

            self.determinant_result = []
            return self.sum






A=Matrix(5, 5)

# for x in range(9):
#     A.push(x)

# result=24
# A.push(7)
# A.push(6)
# A.push(5)
# A.push(4)
# A.push(4)
# A.push(2)
# A.push(9)
# A.push(7)
# A.push(8)
# A.push(9)
# A.push(3)
# A.push(3)
# A.push(7)
# A.push(4)
# A.push(9)
# A.push(7)
# A.push(0)
# A.push(0)
# A.push(5)
# A.push(3)
# A.push(6)
# A.push(1)
# A.push(0)
# A.push(0)
# A.push(0)
# A.push(0)
# A.push(5)
# A.push(6)
# A.push(0)
# A.push(0)
# A.push(0)
# A.push(0)
# A.push(6)
# A.push(8)
# A.push(0)
# A.push(0)


# result=-531
A.push(1)
A.push(0)
A.push(0)
A.push(3)
A.push(-1)
A.push(3)
A.push(-2)
A.push(0)
A.push(0)
A.push(2)
A.push(1)
A.push(1)
A.push(0)
A.push(0)
A.push(1)
A.push(2)
A.push(0)
A.push(4)
A.push(1)
A.push(-2)
A.push(-1)
A.push(1)
A.push(7)
A.push(0)
A.push(3)

# result=14
# A.push(1)
# A.push(3)
# A.push(0)
# A.push(-1)
# A.push(0)
# A.push(2)
# A.push(1)
# A.push(3)
# A.push(3)
# A.push(1)
# A.push(2)
# A.push(1)
# A.push(-1)
# A.push(2)
# A.push(0)
# A.push(3)



print(A.items)

B = Matrix(5, 5)
B.push(5)
for x in range(23):
    B.push(2)
B.push(5)

print(B.items)

oper = Operations(A, B)
print(oper.adding())
print(oper.determinant(A))
print(oper.determinant(B))
