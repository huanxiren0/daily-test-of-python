#coding=utf-8
import math
radiusString = raw_input('请输入圆的半径')
radiusinteger = int(radiusString)
circumference = 2 * math.pi * radiusinteger
area = math.pi * (radiusinteger ** 2)
print "圆的周长为：",circumference, "圆的面积为：",area

