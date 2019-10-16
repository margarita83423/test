# f = open('D:\python\lesson9\nums.txt' , 'r')
# read_data = f.read()
# f.close()


def initPoints():
    points = []
    f = open('D:\\python\\lesson9\\nums.txt')
    points = max(f.read().split())
    f.close()
    # print(points)

    f1 = open('D:\\python\\lesson9\\max_num.txt', 'w')
    f1.write(points)
    f1.close()

    f1 = open('D:\\python\\lesson9\\max_num.txt')
    read = f1.read()
    print(f1)

initPoints()



	






	



