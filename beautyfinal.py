from tkinter import *
from time import *
from random import *
tk = Tk()
s = Canvas(tk, width=1000, height=1000, background="midnightblue")
s.pack()





s.create_arc(450,-20,550,20,start=170,extent=190,fill="bisque3",outline="bisque3")
# red carpet


s.create_polygon(120,660,210,600,750, 600,840, 660,870, 800,120,800, fill="brown")
##CHANDELIER##

#chandelier body

s.create_line(500,0, 500, 150, fill="black",width=4,smooth="true")
s.create_rectangle(490,0, 510,30, fill="black")
s.create_line(500,150,490,180,370,150,340,120,fill="black",smooth="true",width=2)
s.create_line(500,150,590,180,640,150,670,120, fill="black",smooth="true",width=2)
s.create_line(500,150,490,150,460,170,460,180,430, 100, fill="black",smooth="true",width=2)
s.create_line(500,150,520,150,540,180,570,120,570, 60, fill="black",smooth="true",width=2)
s.create_line(500,150,530,160,430,150,400,120, fill="black",smooth="true",width=2)
s.create_line(500,150, 530,160, 570,150,600,120, fill="black",smooth="true",width=2)

#candles

#bottom
x1= [430,570,400,600,340,670]
x2= [420,555,385,585,320,655]
x3= [455,575,415,615,355,690]
y1= [100,100,120,120,120,120]
y2= [90,80,110,110,110,110]
y3= [90,80,110,110,110,110]
for i in range(6):
    s.create_polygon(x1[i],y1[i],x2[i],y2[i],x3[i],y3[i], fill="black")
    

#wax body

x1= [440,580,410,610,350,680]
x2=[420,560,390,590,330,660]
y1=[90,80,110,110,110,110]
y2= [50,50,70,70,70,70]

for i in range(6):
    s.create_rectangle(x1[i],y1[i],x2[i],y2[i], fill="white",outline="white")


#door

s.create_rectangle(390,270,570,660, outline="NavajoWhite3",fill="NavajoWhite3")
s.create_rectangle(390,270,570,280, fill="NavajoWhite2",outline="NavajoWhite2")
s.create_line(300,280,300,660, fill="midnightblue")
s.create_rectangle(220,360,290,580, fill="midnightblue",outline="midnightblue")
s.create_arc(541,300,420,500, start=0, extent=180, fill="midnightblue",outline="midnightblue")
s.create_rectangle(420, 360, 540, 650, fill="midnightblue",outline="midnightblue")
s.create_arc(310,300,380,420, start=0, extent= 180,  fill="midnightblue",outline="midnightblue")
s.create_rectangle(0,0,120,800, fill="tan4",outline="tan4")


s.create_rectangle(0,540,125,550,fill="goldenrod1",outline="goldenrod1")
s.create_rectangle(0,570,125,580, fill="goldenrod1",outline="goldenrod1")
s.create_rectangle(870,0,1000,800, fill="tan4",outline="tan4")
s.create_rectangle(870,540,1000,550,fill="goldenrod1",outline="goldenrod1")
s.create_rectangle(870,570,1000, 580, fill="goldenrod1",outline="goldenrod1")


#inside poles
s.create_polygon(870,300,820,310,820,340,870, 330, fill="sandybrown")
s.create_polygon(750,340,720,330,720,800,750, 800, fill="salmon4", outline="salmon4")
s.create_polygon(690,360,690,340,720,330,720,355,690,360, fill="sandy brown",outline="black" )
s.create_rectangle(720,370, 690, 800, fill="tan2", outline="tan2")
s.create_rectangle(870,360,820, 800, fill="tan2", outline="tan2")
s.create_polygon(120,300,160,320,163,340,120,335, fill="sandy brown")
s.create_rectangle(220,360,240,800,fill="salmon4",outline="black")
s.create_rectangle(120,360,160, 800, fill="tan2",outline="tan2")
s.create_rectangle(240,360,270,800, fill="tan2",outline="tan2")
s.create_polygon(870,330,690,360,690,390,870,360, fill="sandy brown")
s.create_polygon(120,330,270,360,270,390,120, 360, fill="sandy brown")
s.create_polygon(240,330,270,340,270,360,240,355, fill="sandy brown",outline="black")
s.create_polygon(240,330,230,335,220,340,220,350,240, 355, fill="salmon4", outline="black")


##s.create_line(220,330,290,330, fill="white",width=2)
##s.create_line(220,360,290,360, fill="white", width=2)
##s.create_line(220,390,290,90, fill="white", width=2)
##s.create_line(220,420,290,420,fill="white", width=2)
##s.create_line(220,450,290,450,fill="white", width=2)
##s.create_line(220,480,290,480, fill="white", width=2)
##s.create_line(220,520, 290, 520, fill="white", width=2)
##s.create_line(220,550,290,550,fill="white", width=2)
##s.create_line(240,305,240,580, fill="white",width=2)
##s.create_line(270,305, 270, 580, fill="white", width=2)
##s.create_line(310,330,380,330, fill="white", width=2)
##s.create_line(310,360,380,360, fill="white", width=2)
##s.create_line(310,390,380,390, fill="white", width=2)
##s.create_line(310,420,380,420, fill="white", width=2)
##s.create_line(310,450,380,450, fill="white", width=2)
##s.create_line(310,490,380,490, fill="white", width=2)
##s.create_line(310,520,380,520, fill="white", width=2)
##s.create_line(310,550,380,550, fill="white", width=2)
##s.create_line(330,300,330,580,fill="white", width=2)
##s.create_line(360,300, 360,580,fill="white", width=2)
##
##

#fire
numflames =6 
x1= [340,400,430,570,600,670]
x2= [343,403,430,570,603,673]
y1=[70,70,50,50,70,70]
y2= [65,65,50,50,65,65]
drawings= []

for i in range(0,numflames):
    drawings.append(0)

for f in range(500): #in every frame of the animation...
    
    for i in range(0,numflames): #for each flame...
        y1[i] = y2[i] - randint( 10, 15 ) #Sets the top edge of this flame randomly
        drawings[i] = s.create_oval( x1[i], y1[i], x2[i], y2[i], fill="yellow",outline="yellow") #Makes the current flame
                                                                          #Why is it y2 and not y2[i]?
    s.update() #Draws all 10 flames on screen at once
    sleep(0.03)

    for i in range(0,numflames): #Erases all 10 flames
        s.delete( drawings[i] )

##    
##s.create_polygon(340,70, 335,60,340,50,345,60,343,65, fill="orange")
##s.create_polygon(400,70,395,60,400,50,405,60,403,65, fill="orange")
##s.create_polygon(430,50, 425,40,435, 30, 440, 40, 430, 50, fill="orange")
##s.create_polygon(570,50,560,40,570,30,575, 40, 570, 50, fill="orange")
##s.create_polygon(600,70,595,60,600,50,605,60,603, 65, fill="orange")
##s.create_polygon(670,70,665,60,670,50,675,60, 673, 65, fill="orange")
##

spacing = 30#try changing this
for x in range(0, 1000, spacing): 
    s.create_line(x, 20, x, 1000, fill="yellow")
    s.create_text(x, 10, text=str(x), font="Times 10", anchor = N)


for y in range(0, 1000, spacing):
    s.create_line(30, y, 1000, y, fill="yellow")
    s.create_text(5, y, text=str(y), font = "Times 10", anchor = W, fill="yellow")

