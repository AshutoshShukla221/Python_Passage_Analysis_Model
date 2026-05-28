from tkinter import *
from tkinter import messagebox
from mydb import DataBase
import json
from myapi import API
class NLPApp:
    def __init__(self):
        #database object
        self.dbo=DataBase()
        self.myapio=API()
        self.root=Tk()
        self.root.title('NLPAPP')
        self.root.iconbitmap('resources/favicon.ico')#for icon creation
        self.root.geometry('350x600')
        self.root.config(bg='#2E2E2A')
        self.login_gui()


        self.root.mainloop() #to keep the gui fixed on the display
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='#2E2E2A',fg='white')
        heading.pack(pady=(30,30))#used to integrate the label with gui
        heading.configure(font=('verdana','24','bold'))

        label1=Label(self.root,text='Email',bg='#2E2E2A',fg='white')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2=Label(self.root,text='Password',bg='#2E2E2A',fg='white')
        label2.pack(pady=(10,10))

        self.pass_input=Entry(self.root,width=50,show='*')
        self.pass_input.pack(pady=(5,10),ipady=4)
        
        login_btn=Button(self.root,text='LogIn',width=20,height=2,command=self.perform_logIn)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Not a Member?',bg='#2E2E2A',fg='white')
        label3.pack(pady=(10,10))

        register_btn=Button(self.root,text='Register Now',command=self.register_gui)
        register_btn.pack(pady=(5,5))
    def register_gui(self):
        self.clear()
        # heading
        heading=Label(self.root,text='NLPApp',bg='#2E2E2A',fg='white')
        heading.pack(pady=(30,30))#used to integrate the label with gui
        heading.configure(font=('verdana','24','bold'))

        #userName
        label0=Label(self.root,text='User Name',bg='#2E2E2A',fg='white')
        label0.pack(pady=(10,10))

        self.userName_input=Entry(self.root,width=50)
        self.userName_input.pack(pady=(5,10),ipady=4)

        #Email
        label1=Label(self.root,text='Email',bg='#2E2E2A',fg='white')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        #Password
        label2=Label(self.root,text='Password',bg='#2E2E2A',fg='white')
        label2.pack(pady=(10,10))

        self.pass_input=Entry(self.root,width=50,show='*')
        self.pass_input.pack(pady=(5,10),ipady=4)
        

        register_btn=Button(self.root,text='Register',width=20,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Already a Member?',bg='#2E2E2A',fg='white')
        label3.pack(pady=(10,10))

        login_btn=Button(self.root,text='LogIn',command=self.login_gui)
        login_btn.pack(pady=(5,5))

         
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        name=self.userName_input.get()
        email=self.email_input.get()
        password=self.pass_input.get()
        response=self.dbo.add_Data(name,email,password)
        if(response):
            messagebox.showinfo('Success','Registration Sucessful! You can now LogIn')
        else:
           messagebox.showerror('Error','Email Already Exists')

    def perform_logIn(self):
        email=self.email_input.get()
        password=self.pass_input.get()
        response=self.search(email,password)

        if (response):
            messagebox.showinfo('Sucess','LogIn Sucessful!')
            self.home_gui()
        else:
            messagebox.showerror('Error','LogIn Failed')
    
    def search(self,email,password):
        with open('db.json','r') as rf:
             database=json.load(rf)
        if(email in database):
            if database[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0
    def home_gui(self):
        self.clear()
        # heading
        heading=Label(self.root,text='NLPApp',bg='#2E2E2A',fg='white')
        heading.pack(pady=(30,30))#used to integrate the label with gui
        heading.configure(font=('verdana','24','bold'))

        #sentiment
        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=40,height=5,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        #ner
        ner_btn=Button(self.root,text='Named Entity Recognition (N.E.R)',width=40,height=5,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))
        #sentiment
        emotion_btn=Button(self.root,text='Emotion Prediction',width=40,height=5,command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))

        #logout
        logout_btn=Button(self.root,text='LogOut',command=self.login_gui,width=20,height=1)
        logout_btn.pack(pady=(5,5))
    

    def sentiment_gui(self):
        self.clear()
        # heading

        heading=Label(self.root,text='NLPApp',bg='#2E2E2A',fg='white')
        heading.pack(pady=(30,30))#used to integrate the label with gui
        heading.configure(font=('verdana','24','bold'))

        #subheading
        heading=Label(self.root,text='Sentiment Analysis',bg='#2E2E2A',fg='white')
        heading.pack(pady=(10,10))#used to integrate the label with gui
        heading.configure(font=('verdana','20'))

        #text
        label1=Label(self.root,text='Enter Text',bg='#2E2E2A',fg='white')
        label1.pack(pady=(10,10))

        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=10)

        #analysis button
        analyse_btn=Button(self.root,text='Analyse',width=20,command=self.do_sentiment_analysis)
        analyse_btn.pack(pady=(5,5))

        #result
        self.sentiment_result=Label(self.root,text='',bg='#2E2E2A',fg='white')
        self.sentiment_result.pack(pady=(15,15))
        self.sentiment_result.configure(font=('verdana',8))



        #go_back button
        goBack_btn=Button(self.root,text='Go Back',command=self.home_gui,width=20,height=1)
        goBack_btn.pack(pady=(5,5))
    

    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        response=self.myapio.sentiment_analysis(text)
        output=response[0]['label'],'->',response[0]['score']
        self.sentiment_result['text']=output
        
          
        self.sentiment_result['text']=output

    def ner_gui(self):
        self.clear()
        # heading

        heading=Label(self.root,text='NLPApp',bg='#2E2E2A',fg='white')
        heading.pack(pady=(30,30))#used to integrate the label with gui
        heading.configure(font=('verdana','24','bold'))

        #subheading
        heading=Label(self.root,text='Named Entity Recognition',bg='#2E2E2A',fg='white')
        heading.pack(pady=(10,10))#used to integrate the label with gui
        heading.configure(font=('verdana','20'))

        #text
        label1=Label(self.root,text='Enter Text',bg='#2E2E2A',fg='white')
        label1.pack(pady=(10,10))

        self.ner_analyse_input=Entry(self.root,width=50)
        self.ner_analyse_input.pack(pady=(5,10),ipady=10)

        #analysis button
        analyse_btn=Button(self.root,text='N.E.R Analyse' ,width=20,command=self.do_ner_analysis)
        analyse_btn.pack(pady=(5,5))

        #result
        self.ner_result=Label(self.root,text='',bg='#2E2E2A',fg='white')
        self.ner_result.pack(pady=(15,15))
        self.ner_result.configure(font=('verdana',8))



        #go_back button
        goBack_btn=Button(self.root,text='Go Back',command=self.home_gui,width=20,height=1)
        goBack_btn.pack(pady=(5,5))

    def do_ner_analysis(self):
        text=self.n=self.ner_analyse_input.get()
        response=self.myapio.ner_analysis(text)
        print(response)
        output=''
        for item in response:
           wordi = item['word']
           # Extract entity type
           entity = item['entity_group']
           output+=f"{wordi}->{entity}\n"

        self.ner_result['text']=output
    
    def emotion_gui(self):
        self.clear()
        # heading

        heading=Label(self.root,text='NLPApp',bg='#2E2E2A',fg='white')
        heading.pack(pady=(30,30))#used to integrate the label with gui
        heading.configure(font=('verdana','24','bold'))

        #subheading
        heading=Label(self.root,text='Emotion Analysis',bg='#2E2E2A',fg='white')
        heading.pack(pady=(10,10))#used to integrate the label with gui
        heading.configure(font=('verdana','20'))

        #text
        label1=Label(self.root,text='Enter Text',bg='#2E2E2A',fg='white')
        label1.pack(pady=(10,10))

        self.emotion_input=Entry(self.root,width=50)
        self.emotion_input.pack(pady=(5,10),ipady=10)

        #analysis button
        analyse_btn=Button(self.root,text='Emotion Analyse' ,width=20,command=self.do_emotion_analysis)
        analyse_btn.pack(pady=(5,5))

        #result
        self.emotion_result=Label(self.root,text='',bg='#2E2E2A',fg='white')
        self.emotion_result.pack(pady=(15,15))
        self.emotion_result.configure(font=('verdana',8))



        #go_back button
        goBack_btn=Button(self.root,text='Go Back',command=self.home_gui,width=20,height=1)
        goBack_btn.pack(pady=(5,5))

    def do_emotion_analysis(self):
        text=self.emotion_input.get()
        response=self.myapio.emotion_analysis(text)
        output=response[0]['label'],'->',response[0]['score']

        self.emotion_result['text']=output





    










            

        
        
nlp=NLPApp()

