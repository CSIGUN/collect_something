import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont,QFontDatabase
from PyQt5.QtCore import QDateTime, Qt


sulme_1=[]
sulme_2=[]
naeun=[]
ggotnip=[]
muyo=[]
hayo=[]
jieun=[]
gunwoo=[]
######
init={}
result={}

class MyApp(QMainWindow,QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString('yyyy.MM.dd.ddd hh:mm:ss'))
        #############
        self.setWindowTitle('Collect Something')
        self.setGeometry(300,700,500,500)   #아이콘 x,y,w,h
        #self.move(300, 300)
        self.resize(2100, 1200)  #윈도우 크기 
        self.center()   #화면 중앙에 띄우기 위한 만든 함수
        self.button()   #버튼을 위함 만든 함수
        self.line_box_1()
        self.line_box_2()
        self.line_box_3()
        self.line_box_4()
        self.line_box_5()
        self.line_box_6()
        self.line_box_7()
        self.line_box_8()
        #################
        self.text_box_1()
        self.text_box_2()
        self.text_box_3()
        self.text_box_4()
        self.text_box_5()
        self.text_box_6()
        self.text_box_7()
        self.text_box_8()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def button(self):
        #라벨 y 간격 : 130
        #버튼 y 간격 : 130
        label1 = QLabel('A', self)
        label1.move(30, 50)
        label2 = QLabel('B', self)
        label2.move(30, 180)
        label3 = QLabel('C', self)
        label3.move(30, 310)
        label4 = QLabel('D', self)
        label4.move(30, 440)
        label5 = QLabel('E', self)
        label5.move(30, 570)
        label6 = QLabel('F', self)
        label6.move(30, 700)
        label7 = QLabel('G', self)
        label7.move(30, 830)
        label8 = QLabel('H', self)
        label8.move(30, 960)

        btn1 = QPushButton('입력', self)
        btn1.move(30, 130)
        btn1.clicked.connect(self.button_clicked_1)
        
        btn2 = QPushButton('입력', self)
        btn2.move(30, 260)
        btn2.clicked.connect(self.button_clicked_2)
        
        btn3 = QPushButton('입력', self)
        btn3.move(30, 390)
        btn3.clicked.connect(self.button_clicked_3)
        
        btn4 = QPushButton('입력', self)
        btn4.move(30, 520)
        btn4.clicked.connect(self.button_clicked_4)
        
        btn5 = QPushButton('입력', self)
        btn5.move(30, 650)
        btn5.clicked.connect(self.button_clicked_5)
        
        btn6 = QPushButton('입력', self)
        btn6.move(30, 780)
        btn6.clicked.connect(self.button_clicked_6)

        btn7 = QPushButton('입력', self)
        btn7.move(30, 910)
        btn7.clicked.connect(self.button_clicked_7)

        btn8 = QPushButton('입력', self)
        btn8.move(30, 1040)
        btn8.clicked.connect(self.button_clicked_8)

        btncalc = QPushButton('최종 결과', self)
        btncalc.move(1130, 1100)
        btncalc.clicked.connect(self.calc_top)
        
    def line_box_1(self):
        #lable y + 30 / linebox line 간격 : 130
        self.lineedit_1 = QLineEdit(self)
        self.lineedit_1.move(30,80)
        self.lineedit_1.resize(300,40)
        self.lineedit_1.returnPressed.connect(self.button_clicked_1)
        
    def line_box_2(self):
        self.lineedit_2 = QLineEdit(self)
        self.lineedit_2.move(30,210)
        self.lineedit_2.resize(300,40)
        self.lineedit_2.returnPressed.connect(self.button_clicked_2)
    def line_box_3(self):
        self.lineedit_3 = QLineEdit(self)
        self.lineedit_3.move(30,340)
        self.lineedit_3.resize(300,40)
        self.lineedit_3.returnPressed.connect(self.button_clicked_3)
    def line_box_4(self):
        self.lineedit_4 = QLineEdit(self)
        self.lineedit_4.move(30,470)
        self.lineedit_4.resize(300,40)
        self.lineedit_4.returnPressed.connect(self.button_clicked_4)
    def line_box_5(self):
        self.lineedit_5 = QLineEdit(self)
        self.lineedit_5.move(30,600)
        self.lineedit_5.resize(300,40)
        self.lineedit_5.returnPressed.connect(self.button_clicked_5)
    def line_box_6(self):
        self.lineedit_6 = QLineEdit(self)
        self.lineedit_6.move(30,730)
        self.lineedit_6.resize(300,40)
        self.lineedit_6.returnPressed.connect(self.button_clicked_6)
    def line_box_7(self):
        self.lineedit_7 = QLineEdit(self)
        self.lineedit_7.move(30,860)
        self.lineedit_7.resize(300,40)
        self.lineedit_7.returnPressed.connect(self.button_clicked_7)
    def line_box_8(self):
        self.lineedit_8 = QLineEdit(self)
        self.lineedit_8.move(30,990)
        self.lineedit_8.resize(300,40)
        self.lineedit_8.returnPressed.connect(self.button_clicked_8)

    def text_box_1(self):
        label1 = QLabel('A', self)
        label1.move(440, 70)
        self.text_edit_1 = QTextEdit(self)
        self.text_edit_1.setGeometry(400,100,150,900)
    def text_box_2(self):
        label1 = QLabel('B', self)
        label1.move(640, 70)
        self.text_edit_2 = QTextEdit(self)
        self.text_edit_2.setGeometry(600,100,150,900)
    def text_box_3(self):
        label1 = QLabel('C', self)
        label1.move(840, 70)
        self.text_edit_3 = QTextEdit(self)
        self.text_edit_3.setGeometry(800,100,150,900)
    def text_box_4(self):
        label1 = QLabel('D', self)
        label1.move(1040, 70)
        self.text_edit_4 = QTextEdit(self)
        self.text_edit_4.setGeometry(1000,100,150,900)
    def text_box_5(self):
        label1 = QLabel('E', self)
        label1.move(1240, 70)
        self.text_edit_5 = QTextEdit(self)
        self.text_edit_5.setGeometry(1200,100,150,900)
    def text_box_6(self):
        label1 = QLabel('F', self)
        label1.move(1440, 70)
        self.text_edit_6 = QTextEdit(self)
        self.text_edit_6.setGeometry(1400,100,150,900)
    def text_box_7(self):
        label1 = QLabel('G', self)
        label1.move(1640, 70)
        self.text_edit_7 = QTextEdit(self)
        self.text_edit_7.setGeometry(1600,100,150,900)
    def text_box_8(self):
        label1 = QLabel('H', self)
        label1.move(1840, 70)
        self.text_edit_8 = QTextEdit(self)
        self.text_edit_8.setGeometry(1800,100,150,900)

    def move_to_text_1(self):
        txt = self.lineedit_1.text()
        self.text_edit_1.append(txt)
        sulme_1.append(txt)
        self.lineedit_1.clear()
        self.who_is_top(txt, "A")
    def move_to_text_2(self):
        txt = self.lineedit_2.text()
        self.text_edit_2.append(txt)
        sulme_2.append(txt)
        self.lineedit_2.clear()
        self.who_is_top(txt, "B")
    def move_to_text_3(self):
        txt = self.lineedit_3.text()
        self.text_edit_3.append(txt)
        naeun.append(txt)
        self.lineedit_3.clear()
        self.who_is_top(txt, "C")
    def move_to_text_4(self):
        txt = self.lineedit_4.text()
        self.text_edit_4.append(txt)
        ggotnip.append(txt)
        self.lineedit_4.clear()
        self.who_is_top(txt, "D")
    def move_to_text_5(self):
        txt = self.lineedit_5.text()
        self.text_edit_5.append(txt)
        muyo.append(txt)
        self.lineedit_5.clear()
        self.who_is_top(txt, "E")
    def move_to_text_6(self):
        txt = self.lineedit_6.text()
        self.text_edit_6.append(txt)
        hayo.append(txt)
        self.lineedit_6.clear()
        self.who_is_top(txt, "F")
    def move_to_text_7(self):
        txt = self.lineedit_7.text()
        self.text_edit_7.append(txt)
        jieun.append(txt)
        self.lineedit_7.clear()
        self.who_is_top(txt, "G")
    def move_to_text_8(self):
        txt = self.lineedit_8.text()
        self.text_edit_8.append(txt)
        gunwoo.append(txt)
        self.lineedit_8.clear()
        self.who_is_top(txt, "H")
        

    def button_clicked_1(self):
        self.move_to_text_1()
    def button_clicked_2(self):
        self.move_to_text_2()
    def button_clicked_3(self):
        self.move_to_text_3()
    def button_clicked_4(self):
        self.move_to_text_4()
    def button_clicked_5(self):
        self.move_to_text_5()
    def button_clicked_6(self):
        self.move_to_text_6()
    def button_clicked_7(self):
        self.move_to_text_7()
    def button_clicked_8(self):
        self.move_to_text_8()

    def who_is_top(self,text,admin):
        if text in init:
            init[text][0]=int(init[text][0])+1
            init[text].append(admin)
        else:
            init.setdefault(text, [1])
            init[text].append(admin)


    def show_result(self, person_1, person_2,person_3,person_4,person_5,person_6,person_7):
        a = QMessageBox()
        a.setWindowTitle("결과")
        
        a.setText(person_1+"\n"+person_2+"\n"+person_3+"\n"+person_4+"\n"+person_5+"\n"+person_6+"\n"+person_7)

        a.setStandardButtons(QMessageBox.Ok)
        a.exec_()
        
    def calc_top(self):
        result={}
        result=sorted(init.items(), key=lambda x: x[1], reverse=True) #정렬:많은순으
        #####################
        
        person_1=str(result[0][0])
        person_1=person_1+" : "
        
        person_1+=str(result[0][1][0])
        person_1=person_1+"개"
        print(person_1) 

        #####################################
        
        person_2=str(result[1][0])
        person_2=person_2+" : "
        
        person_2+=str(result[1][1][0])
        person_2=person_2+"개"
        #####################################
        
        person_3=str(result[2][0])
        person_3=person_3+" : "
        
        person_3+=str(result[2][1][0])
        person_3=person_3+"개"
        #####################################

        if len(result) >= 4:
            person_4=str(result[3][0])
            person_4=person_4+" : "
        
            person_4+=str(result[3][1][0])
            person_4=person_4+"개"
        elif len(result) < 4:
            person_4=""
        
        #####################################
        if len(result) >= 5:
            person_5=str(result[4][0])
            person_5=person_5+" : "
        
            person_5+=str(result[4][1][0])
            person_5=person_5+"개"
            
        elif len(result) < 5:
            person_5=""
        #####################################
        if len(result) >= 6:
            person_6=str(result[5][0])
            person_6=person_6+" : "
        
            person_6+=str(result[5][1][0])
            person_6=person_6+"개"
            
        elif len(result) < 6:
            person_6=""         
       #####################################
        if len(result) >= 7:
            person_7=str(result[6][0])
            person_7=person_7+" : "
        
            person_7+=str(result[6][1][0])
            person_7=person_7+"개"
            
        elif len(result) < 7:
            person_7=""
        
        
        self.show_result(person_1,person_2,person_3,person_4,person_5,person_6,person_7)
        #결과를 7명까지 출력하도록, 개수랑
        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   fontDB = QFontDatabase()
   fontDB.addApplicationFont('./PyeongChang-Regular.ttf')
   app.setFont(QFont('평창'))
   ex = MyApp()
   sys.exit(app.exec_())
