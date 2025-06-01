from random import randint

class No:
    def __init__(self, number):
        self.number = number
        self.previous = None
        self.next = None

class Circulate_List:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert_number(self, number):
        new_number = No(number)
        if self.head == None:
            self.head = new_number
            self.head.next  = self.head
            self.head.previous = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_number
            new_number.previous = temp
            new_number.next = self.head
        self.length += 1
    
    def show_number(self):
        if self.head == None:
            print("Lista vazia !")
        else:
            temp = self.head
            while(temp.next != self.head):
                print("- {%d} -" % (temp.number), end = " ")
                temp = temp.next
            print("\nFim da Lista !")

    def get_number(self, pos):
        if(pos < 0) or (pos > self.length):
            return -1
        temp = self.head
        for i in range(pos):
            temp = temp.next
        return temp.number

    def search_number(self, target, s):
        if(s < 0) or (s > self.length):
            return -1
        if(self.get_number(s) == target):
            return s
        for k in range(1, self.length):
            if(s - k >= 0 and self.get_number(s - k) == target):
                return s - k
            if(s + k < self.length and self.get_number(s + k) == target):
                return s + k 
        return -1 #valor de retorno se não achou

#teste
wall = Circulate_List()
start_len = randint(10, 100) #tamanho inicial de 10 a 100 valores
s = int(input("\nDigite a posicao inicial: "))
for i in range(start_len):
    number = randint(1, 10) #valores de 1 a 10 sendo adicionados ao "muro"
    wall.insert_number(number)
target = randint(1, 10) #o alvo é um valor aleatório entre 1 a 10
wall.show_number()
result = wall.search_number(target, s)
print("\nO valor {%d} esta na posicao {%d}" % (target, result))
print("\n----------FIM------------")



    



