# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    a,b,c=map(str, input().split())
    ord1=ord(a)
    ord2=ord(b)
    ord3=ord(c)
    print("Код символа " + str(a) + " равен " + str(ord1) + '\n' + "Код символа " + str(b) + " равен " + str(ord2) + '\n'+ "Код символа " + str(c) + " равен " + str(ord3))
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()