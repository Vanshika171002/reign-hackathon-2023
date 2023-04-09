#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import messagebox

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("1700x1700")
photo=Image.open("background1.png")

bac_end=ImageTk.PhotoImage(photo)
lab=Label(win,image=bac_end)
lab.place(x=0,y=0)

#Create a canvas
canvas= Canvas(win, width= 300, height= 300)
canvas.pack()

#Load an image in the script
img= (Image.open("project.png"))

#Resize the Image using resize method
resized_image= img.resize((300,205), Image.Resampling.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)
space=Label(win,text="\n").pack()


#text content
lb1=Label(win,text="ARE YOU DEPRESSED ?",bg='black',fg='red',font=30).pack()
lb0=Label(win,text="\n").pack()
lb11=Label(win,text="Sadness is a normal human emotion whereas depression is a",font=10,bg='black',fg='white').pack()

lb12=Label(win,text="mental health concern that can affect how you think, feel or",font=10,bg='black',fg='white').pack()

lb13=Label(win,text="behave in many ways. Take this quiz to find out whether you are",font=10,bg='black',fg='white').pack()

lb14=Label(win,text="experiencing signs of depression.",font=10,bg='black',fg='white').pack()
lb15=Label(win,text="\n",font=10).pack()

#created a new window to ask user to login in the page

def createNewWindow():
   
    
    #********
    def questwindow():
        
        questionwindow=tk.Toplevel(newWindow)
        questionwindow.minsize(width=1300,height=1300)
        #photo=Image.open("background.png")

        bac_end=ImageTk.PhotoImage(photo)
        lab=Label(questionwindow,image=bac_end)
        lab.place(x=0,y=0)
        
        #list of questions
        #q1.
        labl1=Label(questionwindow,text='What is your coverage sleeping ?',font=15).pack()
        
        
        def Next():
            button=Button(questionwindow,text="Next-->",font=8,fg='black',bg='orange',command=nextwindow).pack()
            

        def q3():
            labl3=Label(questionwindow,text='Do you have Poor appetite?',font=15).pack()
            sl1=Button(questionwindow,text="Not at All",font=5,bg='yellow',fg='purple',command=Next).pack()
            sl2=Button(questionwindow,text="Several days",font=5,bg='yellow',fg='purple',command=Next).pack()
            sl3=Button(questionwindow,text="More than half the days",font=5,bg='yellow',fg='purple',command=Next).pack()
            sl4=Button(questionwindow,text="Nearly Every day",font=5,bg='yellow',fg='purple',command=Next).pack()
           
            
        def q2():
            labl2=Label(questionwindow,text='Do you have a Little interest in doing things ?',font=15).pack()
            sel1=Button(questionwindow,text="Not at All",font=5,bg='yellow',fg='purple',command=q3).pack()
            sel2=Button(questionwindow,text="Sometimes",font=5,bg='yellow',fg='purple',command=q3).pack()
            sel3=Button(questionwindow,text="Most of the days",font=5,bg='yellow',fg='purple',command=q3).pack()
            sel4=Button(questionwindow,text="Nearly Every day",font=5,bg='yellow',fg='purple',command=q3).pack()
        def nextwindow():
            newqwindow=tk.Toplevel(questionwindow)
            newqwindow.minsize(width=400,height=400)

            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            def picturewindow():
                
                pictwindow=tk.Toplevel(newqwindow)
                
                pictwindow.geometry("400x400")
                def func():
                    messagebox.showinfo("Depression Level", "40/100\n Moderate level depression" )
                def suggestions():
                    pass
                    solution=tk.Toplevel(pictwindow)
                    solution.geometry('1000x1000')
                    tex=Label(solution,text='HOW TO GET RID OF DEPRESSION ??? ',font=30,fg='red',bg='black').pack()
                    tex1=Label(solution,text=' Here, we have solutions for you!!!   ',font=20,fg='black',bg='orange').pack()
                    tex2=Label(solution,text='If you have Low depression Level-\n',font=20,fg='blue').pack()
                    text3=Label(solution,text='1. Do Exercises on a daily basis.',font=20,fg='blue').pack()
                    text4=Label(solution,text='2. Breathe deep for 2-3 minutes.',font=20,fg='blue').pack()
                    text5=Label(solution,text='3. Spend more time with your family.\n\n',font=20,fg='blue').pack()
                    tex6=Label(solution,text='If you have Moderate depression Level-',font=20,fg='blue').pack()
                    tex3=Label(solution,text='1.Do Exercises.',font=20,fg='blue').pack()
                    tex4=Label(solution,text='2. Breathe deep for 2-3 minutes.',font=20,fg='blue').pack()
                    tex5=Label(solution,text='3. Spend more time with your family.',font=20,fg='blue').pack()
                    te5=Label(solution,text='4.Please consult from a Counceller .\n\n',font=20,fg='blue').pack()
                    te1=Label(solution,text='If you have High depression Level-',font=20,fg='blue').pack()
                    te2=Label(solution,text='1.Please consult from a Counceller/go to a psychologist .',font=20,fg='blue').pack()
                    te3=Label(solution,text='2. Hope you like listen music ,please listen some relax musics  .',font=20,fg='blue').pack()
                    te3=Label(solution,text='3. Do Exercises on a Daily basis.',font=20,fg='blue').pack()
                    


                    
                    
                def q10():
                    
                    
                    thanks=Label(pictwindow,text='THANKS !!',font=15,fg='red')
                    thanks.place(x=650,y=500)
                    nb=Button(pictwindow,text='View Score',fg='red',bg='grey',font=10,command=func)
                    nb.place(x=600,y=540)
                    nb=Button(pictwindow,text='Next-->',fg='black',bg='grey',font=7,command=suggestions)
                    nb.place(x=610,y=580)
                def q9():
                    
                    ques2=Label(pictwindow,text='Do you feel That nothing would work out for you ?',font=15)
                    ques2.place(x=400,y=390)
                    
                    cl1=Button(pictwindow,text="Never",font=5,bg='yellow',fg='purple',command=q10)
                    cl1.place(x=200,y=420)
                    cl2=Button(pictwindow,text="Hardly Ever",font=5,bg='yellow',fg='purple',command=q10)
                    cl2.place(x=400,y=420)
                    cl3=Button(pictwindow,text="Some of the Time ",font=5,bg='yellow',fg='purple',command=q10)
                    cl3.place(x=600,y=420)
                    cl4=Button(pictwindow,text="Most of the Time",font=5,bg='yellow',fg='purple',command=q10)
                    cl4.place(x=900,y=420)
                    
                    


                    
                def q8():
                    
                    ques1=Label(pictwindow,text='Have you feel difficulty in making decisions ??',font=15)
                    ques1.place(x=400,y=330)
                   
                    cli1=Button(pictwindow,text="Never",font=5,bg='yellow',fg='purple',command=q9)
                    cli1.place(x=200,y=360)
                    cli2=Button(pictwindow,text="Hardly Ever",font=5,bg='yellow',fg='purple',command=q9)
                    cli2.place(x=400,y=360)
                    cli3=Button(pictwindow,text="Some of the Time ",font=5,bg='yellow',fg='purple',command=q9)
                    cli3.place(x=600,y=360)
                    cli4=Button(pictwindow,text="Most of the Time",font=5,bg='yellow',fg='purple',command=q9)
                    cli4.place(x=900,y=360)
                    


                    
                def q7():
                    ques=Label(pictwindow,text="Moving or Speaking so slowly that other people could have noticed ?",font=15)
                    ques.place(x=300,y=260)
                    newl5=Label(pictwindow,text='\n').pack()
                    clic1=Button(pictwindow,text="Not at All",font=5,bg='yellow',fg='purple',command=q8)
                    clic1.place(x=200,y=290)
                    clic2=Button(pictwindow,text="Several days",font=5,bg='yellow',fg='purple',command=q8)
                    clic2.place(x=400,y=290)
                    clic3=Button(pictwindow,text="More than half the days",font=5,bg='yellow',fg='purple',command=q8)
                    clic3.place(x=600,y=290)
                    clic4=Button(pictwindow,text="Nearly Every day",font=5,bg='yellow',fg='purple',command=q8)
                    clic4.place(x=900,y=290)
                
                    
                
                    
                
                img=PhotoImage(name='image',file='card01.png')
                h=Label(pictwindow,image=img,bd=5,relief=SUNKEN)
                h.pack(padx=10,pady=10)
                ques=Label(pictwindow,text="observe the image and mark the suitable option",font=5).pack()
                btns1=Button(pictwindow,text='butterfly/moth/female',font=5,fg='purple',bg='yellow',command=q7)
                btns1.place(x=150,y=200)
                btns2=Button(pictwindow,text="Bat/mask/Jach-o-lankin",font=5,fg='purple',bg='yellow',command=q7)
                btns2.place(x=400,y=200)
                btns3=Button(pictwindow,text="anything deragatory/insulating asout females.",font=5,fg='purple',bg='yellow',command=q7)
                btns3.place(x=650,y=200)

            def nextb():
                but0=Button(newqwindow,text="Next-->",font=5,fg='black',bg='orange',command=picturewindow).pack()
                

            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            #*
            def q6():
                
                lab=Label(newqwindow,text='Trouble concentrating on things ,such as reading books or watching television ?.',font= 15).pack()
                lab1=Label(newqwindow,text='',font= 15).pack()
                
                click1=Button(newqwindow,text="Not at All",font=5,bg='yellow',fg='purple',command=nextb).pack()
                click2=Button(newqwindow,text="Several days",font=5,bg='yellow',fg='purple',command=nextb).pack()
                click3=Button(newqwindow,text="More than half the days",font=5,bg='yellow',fg='purple',command=nextb).pack()
                click4=Button(newqwindow,text="Nearly Every day",font=5,bg='yellow',fg='purple',command=nextb).pack()
               
            #*
            

            #*
            def q5():
                labl5=Label(newqwindow,text='Thoughts that you would be better off dead, or thoughts of hurting yourself in some way ?',font=15).pack()
                select5=Button(newqwindow,text="Not at All",font=5,bg='yellow',fg='purple',command=q6).pack()
                select6=Button(newqwindow,text="Several days",font=5,bg='yellow',fg='purple',command=q6).pack()
                select7=Button(newqwindow,text="More than half the days",font=5,bg='yellow',fg='purple',command=q6).pack()
                select8=Button(newqwindow,text="Nearly Every day",font=5,bg='yellow',fg='purple',command=q6).pack()
            #*


            labl4=Label(newqwindow,text='Do you feel bad about yourself - or that you are a failure or have let yourself or your family down ?',font=15).pack()
            sle1=Button(newqwindow,text="Not at All",font=5,bg='yellow',fg='purple',command=q5).pack()
            sle2=Button(newqwindow,text="Several days",font=5,bg='yellow',fg='purple',command=q5).pack()
            sle3=Button(newqwindow,text="More than half the days",font=5,bg='yellow',fg='purple',command=q5).pack()
            sle4=Button(newqwindow,text="Nearly Every day",font=5,bg='yellow',fg='purple',command=q5).pack()
            
            
        select1=Button(questionwindow,text="8 hours or more",font=5,bg='yellow',fg='purple',command=q2).pack()
        select2=Button(questionwindow,text="10 hours or more",font=5,bg='yellow',fg='purple',command=q2).pack()
        select3=Button(questionwindow,text="6 hours is sufficient",font=5,bg='yellow',fg='purple',command=q2).pack()
        select4=Button(questionwindow,text="dont remember when i had the good sleep",font=5,bg='yellow',fg='purple',command=q2).pack()
#**

    newWindow = tk.Toplevel(win)
    newWindow.minsize(width=1200,height=1200)

    def save_info():
        first_name_info=firstname.get()
        last_name_info=lastname.get()
        age_info=age.get()
        print(first_name_info,last_name_info,age_info)

        file=open("user.txt","w")
        file.write("YOUR FIRST NAME :" + first_name_info)
        file.write("\n")
        file.write("YOUR LAST NAME :" + last_name_info)
        file.write("\n")
        file.write("YOUR AGE :" + str(age_info))
        file.close()

    win.geometry("500x500")
    win.title("PYTHON FILE HANDLING IN FORMS")
    lbl6=Label(newWindow,text='WELCOME TO SERENITY SPACE!!',font =20,fg='red').pack()
    lbl7=Label(newWindow,text='To know a bit more about your depreesion level',font =10).pack()
    lbl8=Label(newWindow,text='please complete the task given below',font =10).pack()
    heading=Label(newWindow,text='Sign Up',bg='yellow',fg='black',font='15',width='500',height='3')
    heading.pack()
    firstname_text=Label(newWindow,text='First Name :')
    lastname_text=Label(newWindow,text='Last Name:')
    age_text=Label(newWindow,text='Age:')

    firstname_text.place(x=15,y=180) 
    lastname_text.place(x=15,y=250) 
    age_text.place(x=15,y=320)

    firstname=StringVar()
    lastname=StringVar()
    age=IntVar()

    first_name_entry=Entry(newWindow,textvariable=firstname,width='30')
    last_name_entry=Entry(newWindow,textvariable=lastname,width='30')
    age_entry=Entry(newWindow,textvariable=age,width='30')

    first_name_entry.place(x=80,y=180)
    last_name_entry.place(x=80,y=250)
    age_entry.place(x=80,y=320)

    btn2=Button(newWindow,text='SUBMIT DATA',fg='green',command=save_info)
    btn2.place(x=25,y=370)
    
    
    def greet():
        labell=Label(newWindow,text='Thanks',font=10,fg='red')
        labell.place(x=550,y=270)
        label=Label(newWindow,text="Things to Remember Before You Start the Quiz",fg='red',font=20)
        label.place(x=300,y=300)
        label1=Label(newWindow,text="1. Please consider your thoughts, feelings and actions in the last 2 weeks.",fg='black',font=10)
        label1.place(x=300,y=330)
        label2=Label(newWindow,text="2. Choose the response that you relate with the most ",fg='black',font=10)
        label2.place(x=300,y=360)
        label3=Label(newWindow,text="3. There are no right or wrong answers to the questions.  ",fg='black',font=10)
        label3.place(x=300,y=390)
        label4=Label(newWindow,text="4. Please answer all questions to get your results..  ",fg='black',font=10)
        label4.place(x=300,y=420)
       
        btn3=Button(newWindow,text='start analysis',font=10,fg='green',command=questwindow)

        btn3.place(x=525,y=450)

        
    btn2=Button(newWindow,text='Next',font=10,fg='black',bg='orange',command=greet)

    btn2.place(x=525,y=450)
    
        

btn1 = Button(win, text="Next-->",font=20,fg='blue',command=createNewWindow)

btn1.pack()

win.mainloop()