#1、引入grammar模块，通过引入的grammar模块生成句子，并把生成的句子写到名字为data.txt的文件中，写1亿次。
from random import choice, seed, randrange
import time
import grammar

class costTime:
    def __init__(self,func):
        self.func=func
      
    def __call__(self, *args):
        st = time.time()
        self.func(*args)
        et = time.time()
        print("用时：%f"%(et-st))


#写1亿次进入到hw3.txt，并执行
def writof():
    with open('D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\hw3.txt','w+') as f:
        for i in range(100000):
            f.write(" ".join(grammar.sentence()))
          
writof()

#2、参考课上讲解的代码，通过装饰器测试在几种不同读取数据（读取自己生成的data.txt文件）的方式下的运行时间。
#法一：打开文件，遍历数据，关闭；
@costTime
def count_file1(fname):
    digits = letters = spaces = others = 0
    with open(fname,encoding="utf_8") as infile:
        for line in infile:  #读取行
            for c in line:  #读取每行的字符
                if c.isdigit():
                    digits+=1
                elif c.isalpha():
                    letters+=1
                elif c.isspace():
                    spaces+=1
                else:
                    others+=1
   
count_file1("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\hw3.txt")

#法二：将文件读到内存中，用一个数据表记录文件中的数据，并对其进行遍历
@costTime
def count_file2(fname):
    digits = letters = spaces = others = 0
    data = []
    with open(fname,encoding="utf_8") as infile:
        for i in infile.read().split():#遍历字符
            data.append(i) #将遍历得到的字符记录到数据表中
            if i.isalpha():
                letters+=1
            elif i.isdigit():
                digits+=1
            elif i.isspace():
                spaces+=1
            else:
                others+=1    
        
count_file2("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\hw3.txt")

#法三：采用缓冲式处理。用一个数据表记录文件中一行的数据。
#一旦表中数据用完，再从文件中读取一行，降低全部读入内存的压力
'''
#@costTime
#定义所需的全局变量
infile = None
nlist = [] #保存每行数据的数据表/缓冲区
crt = 0 #指针，用于记录当前所在的位置，判断是否到行尾
def open_file(fname):
    global infile
    infile = open(fname)

@costTime(open_file)
def next_line():
    global nlist, crt #缓冲式处理，使用全局变量
    if crt == len(nlist): #当前一行读完，再读一行，crt用于定位
        line = infile.readline()
        if not line: #空字符串表示文件已经处理完毕
            infile.close()
            return None
        nlist = line.split()
        crt = 0 #记录当前项的下标
    i = nlist[crt]
  
if __name__ == "__main__":
    open_file("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\hw3.txt")
    next_line()
'''
@costTime
def count_file3(fname):
    digits = letters = spaces = others = 0
    data = []
    crt = 0
    infile = open(fname, encoding="utf_8")
    if crt == len(data):
        line = infile.readline()#每次读入一行，缓冲式处理
        if not line:
            infile.close()
            return None
        data = line.split()
        crt = 0
    i = data[crt]
    for i in data:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            digits+=1
        elif i.isspace():
            spaces+=1
        else:
            others+=1 
        crt += 1  
    return data[crt-1]    

count_file3("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\hw3.txt")    

#法四：为了安全起见，采用闭包的方式，将全局变量变为局部变量
@costTime
def open_file1(fname):
    nlist1 = []
    f = open(fname)
    crt1 = 0
    #定义局部函数
    def next_line1():
        nonlocal nlist1
        nonlocal crt1
        if crt1 == len(nlist1):
            line = f.readline()
            if not line:
                f.close()
                return None
            nlist1 = line.split()
            crt1 = 0
        crt1 += 1
        return nlist1[crt1-1]
    return next_line1

if __name__ == "__main__":
    open_file1("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\hw3.txt")