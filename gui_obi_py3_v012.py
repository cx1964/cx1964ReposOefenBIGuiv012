#!/usr/bin/python3
# Filenaam: gui_obi_py3_v012.py
# Functie: Python3 script tbv het maken van een CSV file obv een input CSV file.
#          Inputfile wordt ongelezen mbv een FileDialog.
# v.0.0 12  20180908    C.X. la Fontaine    Gebruik van Lambda functie voor button die de function generate_OutputFile aanroept
# v.0.0 11  20180908    C.X. la Fontaine    Gebruik van Lambda functie om buttons met parameters mee te geven. Werkt
# v.0.0 10  20180906    C.X. la Fontaine    Uitzoeken doorgegeven parameters bij uitlezen button <Select InputFile> 
#                                           zie gui_obi_py3_v009.py vooir overige werkende functies van alle buttons
#                                           zie https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/
#
#                                            zie ook tkinter_param_pass_lambda.py
#
# v.0.0 8   20180904    C.X. la Fontaine    Function show_entry_fields and generate_OutputFile work
#                                           select_InputFile does not work
#                                           
# v.0.0 7   20180903    C.X. la Fontaine    Use of Radio buttons works and calling of show_entry_fields works  
# v.0.0 4   20180830    C.X. la Fontaine    Determine RowCount en ColumnCount DataFrame
#                                           generate Sorted output
# v.0.0 2   20180829    C.X. la Fontaine 
# v.0.0 1   20180829    C.X. la Fontaine 

# Zie https://pythonprogramming.net/tkinter-tutorial-python-3-event-handling/?completed=/tkinter-python-3-tutorial-adding-buttons/
# Zie https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/
# Zie https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# Zie https://www.youtube.com/watch?v=A0gaXfM1UN0 # Crash course OOP tkinter
# Zie http://zetcode.com/gui/tkinter/layout/
# Zie https://tkdocs.com/tutorial/index.html
# Zie https://python-forum.io/Thread-Tkinter-Entry-widget-unable-to-get-the-text-entered
# Zie https://www.python-course.eu/tkinter_entry_widgets.php
# Zie https://www.python-course.eu/python_tkinter.php
# Zie https://www.programcreek.com/python/example/95892/tkinter.filedialog.Open
# Zie https://docs.python.org/3.1/library/tkinter.html
# Zie https://docs.python.org/3/using/
# Zie https://docs.python.org/3.6/using/
# Zie https://tkdocs.com/tutorial/index.html
# Zie https://tkdocs.com/tutorial/windows.html#dialogs
# Zie https://wiki.python.org/moin/TkInter
# Zie http://thinkingtkinter.sourceforge.net/
#
# Uitzoeken doorgegeven parameters bij uitlezen button <Select InputFile> 
# zie http://www.datadependence.com/2016/04/how-to-build-gui-in-python-3/
# For ubuntu install tkinter library via
# sudo apt-get install python3-tk

from tkinter import *
import tkinter.filedialog
import pandas as pd
import numpy as np
from sys import *
import os

programTitle = sys.argv[0]
programWindowSizeAndPosition="1000x400+300+300"

# Here, we are creating our class, GuiApp, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class GuiApp(Frame): 
    
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # END def init()   


    #Creation of init_window
    def init_window(self):

        # self.style=Style()
        # self.style.theme_use("default")
        
        # changing the title of our master widget      
        self.master.title(programTitle)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        print(sys.argv[0])

        inputFrame1 = Frame(self)
        inputFrame1.pack(expand=0, fill=BOTH, padx=5, pady=5)
        lb1=Label(inputFrame1, text="InputFile")
        lb1.grid(row=0, column=5, padx=5, pady=5)
        self.entry_var1 = StringVar()
        self.entry_var1.set("bla_entry_var1") # dit werkt
        etr1 = Entry(inputFrame1, width=100, textvariable=self.entry_var1) # dit werkt
        #etr1.bind('<Return>', self.show_entry_fields) # dit werkt
        etr1.grid(row=0, column=100, padx=5, pady=5)


        inputFrame2 = Frame(self)
        inputFrame2.pack(expand=0, fill=BOTH, padx=5, pady=5)
        lb2=Label(inputFrame2, text="OutputFile")
        lb2.grid(row=1, column=5, padx=5, pady=5)
        self.entry_var2 = StringVar()
        self.entry_var2.set("bla_entry_var2") # dit werkt
        etr2 = Entry(inputFrame2, width=100, textvariable=self.entry_var2)
        #etr2.bind('<Return>', self.show_entry_fields) # Dit werkt
        etr2.grid(row=1, column=100, padx=5, pady=5)
        #etr2.insert(10,"test01.out.csv")

        self.v = IntVar()
        rbgFrame = Frame(self)
        rbgFrame.pack()
        rbAlphaSorted  = Radiobutton(rbgFrame, text="AlphaSorted" , value=1, variable=self.v) # 
        rbAlphaSorted.pack()
        rbRandomSorted = Radiobutton(rbgFrame, text="RandomSorted", value=2, variable=self.v) #  variable=self.radiobuttonSelectionSortType,
        rbRandomSorted.pack()
        # Make first radiobutton the default
        self.v.set(1)
        
        btnFrame = Frame(self)
        btnFrame.pack(fill=X)
        btn1=Button(btnFrame, text='Quit', command=self.client_exit)
        btn1.pack(sid=RIGHT,padx=5, pady=5)
        btn2=Button(btnFrame, text='Show', command=lambda: self.show_entry_fields(etr1.get(),etr2.get()))  # zie https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/
        btn2.pack(sid=RIGHT,padx=5, pady=5)
        btn3=Button(btnFrame, text='Generate OutputFile', command=lambda: self.generate_OutputFile(etr1.get())) # zie https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/
        btn3.pack(sid=RIGHT,padx=5, pady=5)

        ## BEGIN Anders tov v009
        #self.entry_var1.set("bla_entry_var1")
        btn4=Button(btnFrame, text='Select InputFile', command=lambda: self.select_InputFile(self, etr1.get())) # zie https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/

        #btn4.bind('<Return>', lambda: self.select_InputFile) # gebruik lambda functie om parameters door te geven !!!!!!!!! 
                                                       
                                                     
                                                     # zie ook tkinter_param_pass_lambda.py
        ## EINDE Anders tov v009
        btn4.pack(sid=RIGHT,padx=5, pady=5)
       
    # END init_window()


    def not_yet_implemented():
        # Standard function to show not yet implemented messagebox
        import tkinter.messagebox
        tkinter.messagebox.showinfo(message="Not yet implemented!")
    # END not_yet_implemented()


    def RowCount (self, DataFrame):
        return(DataFrame.shape[0])
    # END RowCount ()    


    def ColumnCount (self, DataFrame):
        return(DataFrame.shape[1])
    # END ColumnCount ()    


    def client_exit(self):
        exit()
    # END client_exit(()    


    def show_entry_fields(self, pEtr1, pEtr2):
        # Lees de waarden van de Entry Fields 
        print("Hier\n")
        print("InputFile: %s\nOutputFile: %s" % (pEtr1, pEtr2)) # dit werkt
    # END show_entry_fields()


    def create_outputFileName(self, pInputFilenName):
        # Maak outputFileName

        # find string ".csv"
        posCSV=pInputFilenName.rfind(".csv")
        if  posCSV != -1 :
            # bevat .csv extention 
            fileNameWithoutExtention=pInputFilenName.replace(".csv", "")     
        else:
            # bevat .CSV extention 
            posCSV=pInputFilenName.rfind(".CSV")
            if posCSV != -1 : 
               fileNameWithoutExtention=pInputFilenName.replace(".CSV", "") 

        # Write output to outputFile
        outputFile = fileNameWithoutExtention+".out"+".csv"
        return (outputFile)
    # END create_outputFileName()


    def select_InputFile(self, mwindow, pEtr1):
        self.filetypes = [
             ("CSV Files", "*.csv *.CSV", "TEXT"),
             ("HTML Files", "*.htm *.html", "TEXT"),
             ("PDF Files", "*.pdf", "TEXT"),
             ("Windows Help Files", "*.chm"),
             ("Text Files", "*.txt", "TEXT"),
             ("All Files", "*")]

        print("Doorgegeven in select_InputFile() " + pEtr1)

        # show Open File Dialog
        #self.opendialog = tkinter.filedialog.Open(parent=master, filetypes=self.filetypes)
        self.opendialog = tkinter.filedialog.Open(parent=mwindow, filetypes=self.filetypes)
        self.base="oefen.csv"
        # Get current directory
        self.dir = os.getcwd()
        self.filename = self.opendialog.show(initialdir=self.dir, initialfile=self.base)
        print("InputFilenaName: "+self.filename)
        # Maak de Entry Fields leeg
        #e1.delete(0,END)
        self.entry_var1.set("")
        #e2.delete(0,END)
        self.entry_var2.set("")
        

        # Set value Entry field InputFile
        #e1.insert(10,filename)
        self.entry_var1.set(self.filename)
        self.outputFileName=self.create_outputFileName(self.entry_var1.get())
        # print("Outputfile wordt:" + outputFileName)
        #e2.insert(10,outputFileName ) 
        self.entry_var2.set(self.outputFileName)

    # END select_InputFile()


    def generate_OutputFile(self, pEtr1):
        # Code 
        # not_yet_implemented()

        # Import libraries
        #import pandas as pd
        #import tkinter.messagebox

        print("Doorgegeven in generate_OutputFile() " + pEtr1)


        #self.inputFilenName = self.entry_var1.get()
        self.inputFilenName = pEtr1
        print("InputFilename in generate_OutputFile" + self.inputFilenName)

        self.outputFile = self.create_outputFileName(self.inputFilenName)
        print("outputFile: " + self.outputFile)

        self.df1 = pd.read_csv(   self.inputFilenName
                            ,sep='|' #delimiter='|'
                     )
        print("Unsorted:")
        print("RowCount: " + str(self.RowCount(self.df1)) + "  " + "ColumnCount: " + str(self.ColumnCount(self.df1)))
        self.rowCount = self.RowCount(self.df1)
        print(self.df1)

        self.SortedOutput = False
        self.RandomSortedOutput = True


        self.radiobuttonSelectionSortType = self.v.get()
        print ("radiobuttonSelectionSortType: " + str(self.radiobuttonSelectionSortType))

        if self.radiobuttonSelectionSortType == 1 :
            # AlphaSortedOutput selected

            # Sorteer op kolom 'Bahasa_Indonesia'
            self.result = self.df1.sort_values(    ["Bahasa_Indonesia","Nederlands"]
                                        ,axis=0 # axis=0 => vertical | axis=1 => horizontal   
                                        ,ascending=[True,False]
                                        #,inplace=True
                                    )
            print("Sorted: ")
            print(self.result)
      

        elif self.radiobuttonSelectionSortType == 2 : 
            # RandomSortedOutput selected
            
            # not_yet_implemented()
            #import numpy as np

            # Create extra column for sortOrder.
            self.df1['SortOrder'] = np.random.randint(low=0, high=10*(self.rowCount+1), size=(self.rowCount, 1)) # maxint value is unlimited
            # Add Extra column on exiting Dataframe
            self.result=self.df1
            print("result with extra column and unsorted")
            print(self.result)

            # Sorteer op kolom 'SortOrder'
            self.result = self.df1.sort_values(    ["SortOrder"]
                                        ,axis=0 # axis=0 => vertical | axis=1 => horizontal   
                                        ,ascending=[True] #[True,False]
                                        #,inplace=True
                                    )
            print("Sorted: ")
            print(self.result)

        else :
            tkinter.messagebox.showinfo(message="Invalid input: \nOnly SortedOutput or\nRandomSortedOutput possible")



        self.result.to_csv(   self.outputFile
                             ,sep='|'
                          )
        print("RowCount: " + str(self.RowCount(self.result)) + "  " + "ColumnCount: " + str(self.ColumnCount(self.result)))

    # END generate_OutputFile()


# ### Main program ###
def main(): 

    mainwindow = Tk()
    mainwindow.geometry(programWindowSizeAndPosition)

    # Start main
    app = GuiApp(mainwindow)
    mainwindow.mainloop()


if __name__ == '__main__':
    main()
