array=list(range(1,10))

def vivod(array):
    print("Так в данный момент выглядит поле:")
    for i in range(3):
        print("-------------")
        print("|", array[i*3+0], "|",array[i*3+1], "|", array[i*3+2], "|")
        print()
    print("-------------")
def proverka(array):
    if array[0]==array[1]==array[2]:
        return array[0]
    elif array[3]==array[4]==array[5]:
        return array[3]
    elif array[6]==array[7]==array[8]:
        return array[6]
    elif array[0]==array[3]==array[6]:
        return array[0]
    elif array[1]==array[4]==array[7]:
        return array[1]
    elif array[2]==array[5]==array[8]:
        return array[2]
    elif array[0]==array[4]==array[8]:
        return array[0]
    elif array[2]==array[4]==array[6]:
        return array[2]
    else:
        return False
    
def hod(array, pick):
    print("Ходят ", pick, "\nВведите номер клетки, куда хотите походить")
    a=int(input())
    if a<1 or a>9:
        print("Вы сходили неправильно, нужно переходить")
        hod(array,pick)
    elif array[a-1]=="X" or array[a-1]=="0":
        print("Клетка уже занята! Ходите заново")
        hod(array,pick)
    elif a>=1 and a<=9:
        array[a-1]=pick
        vivod(array)
    else:
        print("Вы сходили неправильно, нужно переходить")
        hod(array,pick)
vivod(array)
hodnomer=0
while True:
    if hodnomer%2==0:
        pick="X"
        hod(array, pick)
    else:
        pick="0"
        hod(array, pick)
    hodnomer=hodnomer+1
    if hodnomer>4:
        if proverka(array) != False:
            print("Победили ", proverka(array))
            break
    if hodnomer==9:
        print("Ничья")
        break
