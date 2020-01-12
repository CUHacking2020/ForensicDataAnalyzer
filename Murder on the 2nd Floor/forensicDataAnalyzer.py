
from tkinter import *
from forensicAnalysis import *
from datetime import *

class GUI:
    
    global password
    global data_file
    
    password = "123"
    data_file = "Murder-on-the-2nd-Floor-Raw-Data.json"
    
    def __init__(self, master):
        self.master = master
        master.title("Forensic Data Analyzer")

        self.security_window()

    def security_window(self):


        photo = PhotoImage(file = "forensics.png")
        background = Label(self.master, image = photo)
        background.image = photo
        background.place(x=150, y=90)
        
        Label(self.master, text = "Enter ID to Access:",
              font=("Courier",12)).place(x=800, y=300)
        
        ID_field = Entry(self.master,show="*")
        ID_field.place(x=810,y=335)

        but1 = Button(self.master,text="Enter",command=lambda:self.correct_answer(ID_field.get()))
        but1.place(x=940,y=330)
        
    def correct_answer(self,answer):
        if answer == password:
            self.master.withdraw()
            self.suspects_window()
        else:
            wrong_answer = Label(self.master,text="Incorrect ID, ID is 123.").place(x=825, y=355)
            
    
    def suspect_profile_window(self, suspect):
        window = Toplevel(root)
        window.geometry("950x650")
        
        label = Label(window, text = "Search: ", font=("Courier",12)).pack(side=LEFT)
        search = Entry(window).pack(side=LEFT)
        scrollbar = Scrollbar(window)
        scrollbar.pack(side = RIGHT, fill = Y)
       
        mylist = Listbox(window, yscrollcommand = scrollbar.set, height = 10)
        mylist.pack(side = LEFT, fill = BOTH)
        mylist.config(width = 130, font = ("Courier",12))
        scrollbar.config(command = mylist.yview)

        suspect_data = suspect_profiles(data_file, suspect)

        
        mylist.insert(END, "Suspect : " + suspect)
        mylist.insert(END, "")
        mylist.insert(END, "      Time      -       Device  -  Room/DevID  -  Event")
        mylist.insert(END, "")
        for event in suspect_data:
            time = datetime.fromtimestamp(int(event[0])).strftime("%c")


            mylist.insert(END, time[:-5] + " | " + event[1] + " | " + event[2] +
                          " | " + event[3])
            mylist.insert(END, "")


    def data_window(self):
        window = Toplevel(root)
        window.geometry("950x650")

        label = Label(window, text = "Search: ", font=("Courier",12)).pack(side=LEFT)
        search = Entry(window).pack(side=LEFT)
        scrollbar = Scrollbar(window)
        scrollbar.pack(side = RIGHT, fill = Y)
       
        mylist = Listbox(window, yscrollcommand = scrollbar.set, height = 10)
        mylist.pack(side = LEFT, fill = BOTH)
        mylist.config(width = 130, font = ("Courier",12))
        scrollbar.config(command = mylist.yview)

        mylist.insert(END, "All Collected Data: ")
        


    def suspects_window(self):
        window = Toplevel(root)
        window.geometry("1280x700")
        
        photo1 = PhotoImage(file = "veronica.png")
        img1 = photo1.subsample(3,3)
        sus1 = Button(window,text="  Veronica\n  Hotel Guest", height = 200, width = 300, image = img1,compound="left",
                      command=lambda:self.suspect_profile_window("Veronica"))
        sus1.image = img1
        sus1.grid(row=0, column = 1)

        photo2 = PhotoImage(file = "jason.png")
        img2 = photo2.subsample(3,3)
        sus2 = Button(window,text="  Jason\n  Hotel Guest", height = 200, width = 300, image = img2, compound = "left",
                      command=lambda:self.suspect_profile_window("Jason"))
        sus2.image = img2
        sus2.grid(row=0)

        photo3 = PhotoImage(file = "thomas.png")
        img3 = photo3.subsample(3,3)
        sus3 = Button(window,text="  Thomas\n  Hotel Guest", height = 200, width = 300, image = img3, compound = "left",
                      command=lambda:self.suspect_profile_window("Thomas"))
        sus3.image = img3
        sus3.grid(row=0,column=3)

        photo4 = PhotoImage(file = "rob.png")
        img4 = photo4.subsample(3,3)
        sus4 = Button(window,text="  Rob\n  Hotel Guest", height = 200, width = 300, image = img4, compound = "left",
                      command=lambda:self.suspect_profile_window("Rob"))
        sus4.image = img4
        sus4.grid(row=1,column=1)

        photo5 = PhotoImage(file = "kristina.png")
        img5 = photo5.subsample(3,3)
        sus5 = Button(window,text="  Kristina\n  Hotel Guest", height = 200, width = 300, image = img5, compound = "left",
                      command=lambda:self.suspect_profile_window("Kristina"))
        sus5.image = img5
        sus5.grid(row=1,column=0)

        photo6 = PhotoImage(file = "marc_andre.png")
        img6 = photo6.subsample(3,3)
        sus6 = Button(window,text="  Marc-Andre\n  Hotel Staff", height = 200, width = 300, image = img6, compound = "left",
                      command=lambda:self.suspect_profile_window("Marc-Andre"))
        sus6.image = img6
        sus6.grid(row=0,column=2)

        photo7 = PhotoImage(file = "dave.png")
        img7 = photo7.subsample(3,3)
        sus7 = Button(window,text="  Dave\n  Hotel Staff", height = 200, width = 300, image = img7, compound = "left",
                      command=lambda:self.suspect_profile_window("Dave"))
        sus7.image = img7
        sus7.grid(row=1,column=2)

        photo8 = PhotoImage(file = "selena.png")
        img8 = photo8.subsample(3,3)
        sus8 = Button(window,text="  Salina\n  Hotel Staff", height = 200, width = 300, image = img8, compound = "left",
                      command=lambda:self.suspect_profile_window("Salina"))
        sus8.image = img8
        sus8.grid(row=2,column=2)

        photo9 = PhotoImage(file = "harrison.png")
        img9 = photo9.subsample(3,3)
        sus9 = Button(window,text="  Harrison\n  Hotel Staff", height = 200, width = 300, image = img9, compound = "left",
                      command=lambda:self.suspect_profile_window("Harrison"))
        sus9.image = img9
        sus9.grid(row=2,column=3)

        photo10 = PhotoImage(file = "eugene.png")
        img10 = photo10.subsample(3,3)
        sus10 = Button(window,text="  Eugene\n  Non-Guest", height = 200, width = 300, image = img10, compound = "left",
                       command=lambda:self.suspect_profile_window("Eugene"))
        sus10.image = img10
        sus10.grid(row=2,column=1)

        photo11 = PhotoImage(file = "alok.png")
        img11 = photo11.subsample(3,3)
        sus11 = Button(window,text="  Alok\n  Non-Guest", height = 200, width = 300, image = img11, compound = "left",
                       command=lambda:self.suspect_profile_window("Alok"))
        sus11.image = img11
        sus11.grid(row=1,column=3)

        photo12 = PhotoImage(file = "james.png")
        img12 = photo12.subsample(3,3)
        sus12 = Button(window,text="  James\n  Non-Guest", height = 200, width = 300, image = img12, compound = "left",
                       command=lambda:self.suspect_profile_window("James"))
        sus12.image = img12
        sus12.grid(row=2,column=0)

        Label(window, text="").grid(row=3,column=3)

        Label(window, text= "The suspect list is in order from most to least suspicious based off their data.\n Click profile to analize their individual data.\n To view phone calls, click the All Data tab.",
              font=("Courier", 12)).grid(row = 3, columnspan = 3)

        Button(window, text="   All Data   ",command=lambda:self.data_window()).grid(row=3,column=3)
        Button(window, text="   Log Out    ", command=lambda:self.end()).grid(row=4,column=3)
    
    def searching(self, keyword):
        data = analyzeFile(data_file)
        wordlist = []

        for event in data:
            if keyword in event:
                wordlist.append(event)

    def end(self):
        self.master.destroy()

root = Tk()
root.geometry("1280x700")
forensic_data_analyzer = GUI(root)
root.mainloop()
