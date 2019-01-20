import os

f=open("123.txt",'w')
f.write("123456789\nabcdefg\n")
f.close()

f=open("123.txt",'r')
print('-'*20)
content=f.read(5)
print(content)
print('-'*20)
content=f.read(5)
print(type(content))
print(content)
f.close()

f=open("123.txt",'r')
print('-'*20)
content=f.readlines()
print(type(content))
print(content)
f.close()

f=open("123.txt",'r')
print('-'*20)
content=f.readline()
while len(content):
    print(content)
    content=f.readline()
print(type(content))
print(content)
f.close()

f=open("123.txt",'w+')
f.close()


files = os.listdir('./')
print(files)

try:
    xxx=100
    print(xxx)
    open("xxxxxxxxx",'r')
#except:
#    print("Error!!!!!!!")
#except NameError:
#    print("NameError!!!!!!!")
#except FileNotFoundError:
#    print("FileNotFoundError!!!!!!!")
except (NameError,FileNotFoundError) as e:
    print("ERROR!!!!!!!",e)
else:
    print("else----")
finally:
    print("finally!!!!!")


if __name__ == '__main__':
    print(__name__)