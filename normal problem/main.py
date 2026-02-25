# True = False
# d = {0, 1, 2}
# for x in d:
#     print(x)
# print(d)
# print(type(type(int)))
# a="d"
# b=a.maketrans("as","bd")
# print(chr(b[115]))
# set1 = {3, 4, 5} 
# set1.update([1, 2, 3]) 
# print(set1)
# set1 = {1, 2, 3} 
# set2 = set1.add(4) 
# print(set2)
# set1 = {1, 2, 3} 

# set2 = {4, 5, 6} 
# print(len(set1 )+len(set2))\
# from functools import reduce
# lst=[1,2,3,4]
# add_sub=reduce(lambda x,y:x+y,lst)
# # a,b=add_sub(lst,lst)
# print(add_sub)

# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     c = a/b;
#     print(c)
# except Exception as e:
#     print(e)
# else:
#     print("Hi I am else block")
# finally:
#     print("I am finally block")
# import pickle


# a={"hello":"bye","namesta":"gako"}
# a_piclek=pickle.dumps(a)
# print(a_piclek)
# a_unpickel=pickle.loads(a_piclek)
# print(a_unpickel)

# with open("a.txt") as f:
#     print(f.write("hgf"))

# f=open("a.txt") 
# print(f.readlines())


# print("hello\\") ## back slash dluble
# # print("hello\")  # back slash error

# print("hello/") #hello/
# print("hello//") #hello//
# b = [1, 2, 3]
# a=list(map(lambda x:x*2,b))
# print(a)
# #[2, 4, 6]
# a = 10
# b = 20
# print("""
# print(f"{a+b}")
# print("Hello\nWorld")
# print(len(" "))

#       """)

# a = 10
# b = 20
# # print(a b)
# print(len(10))
# a = {1,2,3}
# print(a[0])
# name="program"
# result=name.maketrans("pr","PR")
# print(name.translate(result))
# # output =PRogRam

# s={1,2,3}
# s.add(4)
# print(s)
# s.discard(6)
# print(s)

# print(len(""))
# print(bool(len("")))

# f=open("a.txt","w",encoding="utf-8") 
# f.writelines(["dfdddfgfg\n f 😅😅","sdg987"])

# print(0 or 3)
# print(0 or 5)
# for i in range(0):
#       print(i)
# from time import sleep


# for i in range(2):

#     for j in range(3):
#         if j==1:
#             break
  
#         print(j,end=" ")

# a=10
# b=20
# print("{0}{1}{c}".format(b,a,c=12))

# x, y = 5, 10

# if x > y:
#     pass
# elif x == y:
#     print("Equal")
# else:
#     print("Smaller") if x < y else print("Greater")

# def test(x=[]):
#     x.append(1)
#     return x

# print(test())
# print(test())
# f = open("sample.txt", "w")

# f.write("Hello\nWorld")

# f.close()

# f = open("sample.txt", "r")

# print(f.readline(),end="")

# f.seek(0)

# print(f.read(5))
# a = 10
# b = 5
# if a > b:
#     if a + b > 20:
#         print("A")
#     elif a - b > 2:
#         print("B")
#     else:
#         print("C")
# else:
#     print("D")
# try:

#     print(1 / 0)

# except:

#     print("A")

# finally:

#     print("B")
    
# print("AB")


# x = -5
# if x:

#     if x < 0:

#         print("Success")

#     else:

#         print("Fail")

# else:

#     print("Zero")