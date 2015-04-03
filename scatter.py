# from matplotlib import pyplot
# from matplotlib import style
import pylab

# style.use('ggplot')
# pyplot.figure()

# /*----------------------------------------------*/
# x = [5,6,7,8]
# y = [7,3,8,3]
# x2 = [5,6,7,8]
# y2 = [6,7,2,6]

# pyplot.plot(True, color='k')
# pyplot.plot(x,y,'g',linewidth=5,label='line One')
# pyplot.plot(x2,y2,'c',linewidth=10,label='line Two')

# pyplot.title('Epic Chart')
# pyplot.ylabel('Y axis')
# pyplot.xlabel('X axis')
# pyplot.legend()
# pyplot.show()
# /*----------------------------------------------*/




a = {
    1 : [11, 7, '+', '+', '+', '+'],
    2 : [8, 5, '+', '+', '+', '+'],
    3 : [7, 12, '+', '+', '+', '+'],
    4 : [5, 6, '+', '+', '+', '+'],
    5 : [3, 18, '+', '+', '+', '+'],
    6 : [2, 11, '+', '+', '+', '+'],
    7 : [9, 3, '+', '+', '+', '+'],
    8 : [19, 4, '+', '+', '+', '+'],
    9 : [5, 19, '+', '+', '+', '+'],
}

b = a.values()

# for i in b:
# 	pylab.plot(i[0], i[1])

x = [i[0] for i in b]
y = [i[1] for i in b]

# for i in x:
# 	print(i)

# x = [i/10 for i in range(0, 100)]
# y = [i*i for i in x]

pylab.plot(x, y, 'bs')
for i in range(0,9):
    pylab.annotate('F(x{0})'.format(i), xy=(x[i], y[i]), xytext=(x[i]+.2, y[i]+.2))

pylab.xticks(range(20))
pylab.yticks(range(20))
pylab.show()

# pylab.hist(pylab.randn(10000)) 
# pylab.hist(pylab.randn(10000)) 
# pylab.show()