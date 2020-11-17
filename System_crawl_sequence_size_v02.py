import os
import re
import pyseq
import sys
import pprint
from PIL import Image
from pathlib import Path
import fsutil

#file = os.stat("Schilpad_retopo_V01_bak5.hip")
#print('Size of file is', file.st_size, 'bytes')
f = open("my_sequences2.txt", "w")

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
import qtmodern.styles
import qtmodern.windows
from interface import Ui_MainWindow




#print("my root sets zijn : {}".format(my_root_set))

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'kilo', 2: 'mega', 3: 'giga', 4: 'tera'}
    while size > power:
        size /= power
        n += 1
    return size, power_labels[n]+'bytes'

def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)

tests = [1, 1024, 500000, 1048576, 50000000, 1073741824, 5000000000, 1099511627776, 5000000000000]

#for t in tests: print('{0} == {1}'.format(t,humanbytes(t)))

def print_lijstnamen(folder):
    """print namen uit van alle lijst sequences uit een folder"""
    for lijstnaam in range(len(folder)):
        #print(folder[lijstnaam])
        pass

def detect_sequences(pad): # geeft een pad aan en ontvang alle sequences uit dat pad.
    folder = pyseq.get_sequences(pad) # dit is een pad waar meerdere sequences in bestaan
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(folder)
    #print(str(pad) + " bevat volgende aantal file sequenses: " + str(len(folder))) # aantal folder in folder
    #print_lijstnamen(folder)
    #print("type folder is:" +  str(type(folder)))
    return folder

def get_list_file_size(folder, items):
    #my_sequence_dict = {"eq": {"foldernaam": "", "sequencenaam" : "","sequencesize":""}}
    my_sequence_dict = {"sequence":["","",""]}

    for i, sequence in enumerate(folder):
        #print("naam folder is {}".format(len(folder[i])))

        if len(folder[i]) == 1:
            pass
        else:
            #print("naam daadwerkelijke sequence is {}".format(folder[i]))


            filesize_list = []
            for file in folder[i]:
                #print(file)
                #print(path + file)
                full_path = str(items) + "\\" + str(file)
                #print(str(path))
                #print(str(file))
                #print(full_path)
                #file_size=os.path.getsize(str(full_path))
                #file_size = os.stat(full_path)
                #print('Size of file is', file_size.st_size, 'bytes')
                #print("the size of " + full_path)


                # mijn os.stat approach
                #current_file = os.stat(full_path)
                #print('Size of file is', os.stat(path).st_size, 'bytes')
                #filesize_list.append(os.stat(path).st_size)

                #mijn sys.getsizeof approach
                """ image_file = Image.open(full_path)
                print("File Size In Bytes:- "+str(len(image_file.fp.read()))) """


                maat = fsutil.get_file_size(full_path)
                #print("get file size is: " + str(maat)) 
                size_str = fsutil.get_file_size_formatted(full_path)
                #print("get file size formatted is: " + str(size_str))
                filesize_list.append(maat)



            filesize_totaal = sum(filesize_list)
            #print(len(filesize_list))
            #print(filesize_totaal)
            #print(humanbytes(filesize_totaal))

            #my_sequence_dict ["foldernaam"] = folder

            my_sequence_dict["sequence"][0] = str(items)
            my_sequence_dict["sequence"][1] = str(folder[i])
            my_sequence_dict["sequence"][2] = humanbytes(filesize_totaal)
            #print(my_sequence_dict)
            f.write(str(my_sequence_dict) + "\n")
    return my_sequence_dict


def write_to_txt(resultaat):
    f = open("my_sequences.txt", "w")
    for key , values in resultaat.items():
        pass


def del_none_keys(dict):
    for elem in dict.keys():
        if dict[elem] == None:
           del dict[elem]

#for its, items in enumerate(my_root_set):
    #gevonden = detect_sequences(items)
    #print("gevonden: {}".format(gevonden))
    #print("its: {}".format(its))
    #print("items: {}".format(items))
    #print("Formaat van dict is: {}".format(len(gevonden)))
    #resultaat = get_list_file_size(gevonden, items)
    #print("gevonden" + str(type(gevonden)))
    #print(resultaat)



    #write_to_txt(resultaat)


class Mainwindow(qtw.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_start.clicked.connect(self.zoeken)
        self.ui.tableWidget_resultaat.setColumnWidth(0,350)
        self.ui.tableWidget_resultaat.setColumnWidth(1,550)

        self.show()

    def zoeken(self):
        file = str(qtw.QFileDialog.getExistingDirectory(self, "Selecteer een Directory"))
        self.ui.label_zoekfolder.setText(file)

        path = (file)
        print(path)

        mijn_table_data = {}
        my_root_set =  set()

        for root, dirs, files in os.walk(path):
            for name in files:
                my_root_set.add(root)
                #print(root)

        global_resultaat = []
        for its, items in enumerate(my_root_set):
            gevonden = detect_sequences(items)
            print(gevonden)
            resultaat = get_list_file_size(gevonden, items)
            global_resultaat.append(resultaat)



        aantallen = len(global_resultaat)
        print("aantallen is: {}".format(aantallen))
        print("global resultaat is 1 1 : {}".format(global_resultaat))


        row = 0
        self.ui.tableWidget_resultaat.setRowCount(aantallen)
        for index, sequence_object in enumerate(global_resultaat):

            print("index is : {}".format(index))
            print("sequence_object is : {}".format(sequence_object))
            print("Folder is : {}".format(sequence_object["sequence"][0]))

            self.ui.tableWidget_resultaat.setItem(index, 0, qtw.QTableWidgetItem(sequence_object["sequence"][0]))
            self.ui.tableWidget_resultaat.setItem(index, 1, qtw.QTableWidgetItem(sequence_object["sequence"][1]))
            self.ui.tableWidget_resultaat.setItem(index, 2, qtw.QTableWidgetItem(sequence_object["sequence"][2]))
            row=row+1













if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = Mainwindow()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())

f.close()