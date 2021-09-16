

#first install matplotlib
pip install matplotlib


import matplotlib.pyplot as plt
import numpy as np #with help of numpy we can create array

xpoints= np.array([0,6])
ypoints = np.array([0,1000,'o'])
plt.plot(xpoints,ypoints)
plt.show()


##ypoints = np.array([3,8,1,10])
##plt.plot(ypoints,marker="*")#h,p,4,d capital small etc u can try
##plt.show()


#format string :something in string nottion 
##ypoints = np.array([3,8,1,10])
##plt.plot(ypoints,marker="o:r")
# #r for red,y for yellow,k for black etc u can try
##plt.show()


##ypoints = np.array([3,8,1,10])
##plt.plot(ypoints,marker="o:r",ms=20)#ms is marker size 
##plt.show()


##ypoints = np.array([3,8,1,10])
##plt.plot(ypoints,marker="o:r",ms=20,mec='r')
# #mec is marker  boundary colour e is edge 
##plt.show()

##ypoints = np.array([3,8,1,10])
##plt.plot(ypoints,marker="o:r",ms=20,mec='r',mfc='r',linetyle='dotted')
###mfc is marker inside colour f is face ,
###linestyle can be dashed,dotted etc
##plt.show()
#when x cordinate was not their by default cordinates are taken  as 1 

##xpoints= np.array([1,15,5,7])
##ypoints = np.array([3,8,1,10])
##plt.plot(xpoints,ypoints,marker="o:r",ms=20,mec='r',mfc='r',linetyle='dotted')
##plt.show()
#when y cordinate was not their by default cordinates are taken  as 1

##xpoints= np.array([1,15,5,7])
##plt.plot(xpoints,ls=':',color='r',linewidth='10')
###ls is linestyle 
# ...linestyle can be written as dashed or dotted or dashdot or -. etc
###linewidth is for increasing the width
##plt.show()


###for getting multiple lines
##xpoints1= np.array([1,15,5,7])
##xpoints2= np.array([3,6,9,7])
##plt.plot(xpoints1)
##plt.plot(xpoints2)
##plt.show()


#you will get single line
##xpoints1= np.array([1,15,5,7])
##xpoints2= np.array([3,6,9,7])
##plt.plot(xpoints1 ,xpoints2 )
##plt.show()


##xpoints1= np.array([1,15,5,7])
##xpoints2= np.array([3,6,9,7])
##xpoints3= np.array([1,10,9,7])
##plt.plot(xpoints1 ,xpoints2,xpoints3 )
##plt.show()

#label:it willl label x and y axis
#title will give title to graph
##loc is to set location left right top and bottom etc
##plt.grid() will provide us coloums it will provide both x and y 
##to get coloum in x axis :axis=x
##to get coloum in y axis :axis=y


##xpoints1= np.array([1,15,5,7])
##xpoints2= np.array([3,6,9,7])
##plt.plot(xpoints1 ,xpoints2 )
##plt.xlabel("aakriti" , loc="top")
##plt.ylabel("bhavesh", loc="right")
##plt.title("WWE" , color ='r',loc="right")
##plt.grid(axis="x', color='hotpink',linewidth='3',linestyle='--')
##plt.show()

####to get two graphs together we can plot only two graphs using sub plot together
####plot 1
##x=np.array([1,2,3,4,5])
##y=np.array([9,8,7,6,5])
##plt.subplot(1,2,1)
##plt.title("aakriti")
###format (row no,coloumn number,graph number)
###plt.subplot(1,2,1) 1 row 2 coloum and 1 is graph number 
##plt.plot(x,y)
####plot 2
##x=np.array([1,2,3,4,5])
##y=np.array([9,8,7,6,5])
##plt.subplot(1,2,2)
##plt.plot(x,y)
##plt.title("arshul")
####plot 2
##x=np.array([1,2,3,4,5])
##y=np.array([9,8,7,6,5])
##plt.subplot(1,3,1)
##plt.plot(x,y)
##plt.title("adyyy")
##plt.suptitle("divya")
####supertitle will act like top title

#piechart
##y=np.array([9,8,7,6,5])
##plt.pie(y)

#explode will bring the things out 
##y=np.array([9,8,7,6,5])
##x=['apple','banana','orange','papaya']
##z=[0.2,0,0,0]
##a=["hotpink","black","yellow","brown"]
##plt.pie(y,labels=x,startangle=90,explode=z,shadow=True,colors=a)
##plt.legend(title="oh yeah")#keep it in bottom   


#histogram
##x=np.random.normal(12,34,45)
##plt.hist(x)

##x=np.random.normal(12,34,45)
##plt.hist(x)
##plt.show()
#interpreter line ko check karega ...compiler pura show krega phir error hi ku na ho

#bargarph
##x=np.array(["A","B","C","D"])
##y=np.array([1,2,3,4])
##plt.bar(x,y)
##
##to have horizontal put bar=barh
##x=np.array(["A","B","C","D"])
##y=np.array([1,2,3,4])
##plt.barh(x,y,color="r)
##
##x=np.array(["A","B","C","D"])
##y=np.array([1,2,3,4])
##plt.bar(x,y,color="r",width=0.1)
##
##x=np.array(["A","B","C","D"])
##y=np.array([1,2,3,4])
##plt.barh(x,y,color="r",height=0.1)


#scaTTER
##x=np.array([1,3,6,7,9,5])
##y=np.array([3,5,8,2,4,6])
##plt.scatter(x,y)
##
##x1=np.array([10,11,12,13,14,81])
##y1=np.array([13,25,18,12,14,16])
##plt.scatter(x1,y1)
##
##
##x1=np.array([10,11,12,13,14,81])
##y1=np.array([13,25,18,12,14,16])
##color=np.array(["red',"blue","green,"pink"])
##size=np.array([500,600,700,800])
##plt.scatter(x1,y1,c=color,s=size,alpha=0.5)#c is used to give
#  color in scatter










