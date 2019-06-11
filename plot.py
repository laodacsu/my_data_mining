import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.patches import Polygon
print(3)
# plt.style.use('ggplot')
# x=np.linspace(0,10,100)
# y=x**2
# plt.plot(x,y,'*',alpha=0.5)
# plt.legend('r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
# r=np.ones((1,5))*5
# theta = np.linspace(0,2*np.pi,5)
# ax = plt.subplot(111,projection='polar')
# ax.plot(theta,r,'r',linewidth=2)
# ax.grid(True)
# plt.show()
# x=np.linspace(0,10,100)
# y=x**2
# fig,ax=plt.subplots()
# plt.plot(x,y,'r',linewidth=2)
# plt.style.use('ggplot')
# a=2
# b=9
# ax.set_xticks([a,b])
# plt.ylim(ymin=0)
# ax.set_yticks([])
# ax.set_xticklabels(['$a$','$b$'])
# ix=np.linspace(a,b)
# iy=ix**2
# ixy=zip(ix,iy)
# verts=[(a,0)]+list(ixy)+[(b,0)]
# poly = Polygon(verts,facecolor='0.9',edgecolor='0.1')
# ax.add_patch(poly)
# plt.figtext(0.9,0.1,'$x$')
# plt.figtext(0.1,0.9,'$y$')
# ax.text(6,20,r'$\int_a^b x^2dx$')
# plt.show()

plt.style.use('ggplot')
x=np.random.rand(200)
y=x+np.random.randn(200)*0.5

margin_border = 0.1
width = 0.6
height = 0.2
margin_between = 0.02

left_s = margin_border
bottom_s = margin_border
height_s = width
width_s = width

left_x = margin_border
bottom_x = margin_border+width+margin_between
height_x = height
width_x = width

left_y = margin_border+width+margin_between
bottom_y = margin_border
height_y = width
width_y = height

plt.figure(1,figsize=(8,8))
rect_s = [left_s,bottom_s,width_s,height_s]
rect_x = [left_x,bottom_x,width_x,height_x]
rect_y = [left_y,bottom_y,width_y,height_y]

axScatter = plt.axes(rect_s)
axHistX = plt.axes(rect_x)
axHistY = plt.axes(rect_y)
axHistX.set_xticks([])
axHistY.set_yticks([])

axScatter.scatter(x,y)

bin_width = 0.25
xymax = np.max([np.max(abs(x)),np.max(abs(y))])
lim = int(xymax/bin_width+1)*bin_width

axScatter.set_xlim(-lim,lim)
axScatter.set_ylim(-lim,lim)

bins = np.arange(-lim,lim+bin_width,bin_width)
axHistX.hist(x,bins=bins)
axHistY.hist(y,bins=bins,orientation='horizontal')
axHistX.set_xlim(axScatter.get_xlim())
axHistY.set_ylim(axScatter.get_ylim())
plt.show()