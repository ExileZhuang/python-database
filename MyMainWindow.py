import pymysql
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyMainWindow(Ui_MainWindow,QMainWindow):

    #初始化并实现功能连接：
    def __init__(self):
        super(MyMainWindow,self).__init__()
        self.setupUi(self)

        #init_quit_pushButton:
        self.init_quit_pushButton.clicked.connect(self.close)

        #init_login_pushButton:
        self.init_login_pushBotton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

        #dataManage_animaldata_pushButton:
        self.dataManage_animaldata_pushButton.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))

        #dataManage_passengerdata_pushButton:
        self.dataManage_passengerdata_pushButton.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))

        #dataManage_workerdata_pushButton:
        self.dataManage_workerdata_pushButton.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(2))

        #dataManage_housedata_pushButton:
        self.dataManage_housedata_pushButton.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(3))

        #dataManage_apartmentdata_pushButton:
        self.dataManage_apartmentdata_pushButton.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(4))

        #dataManage_homedata_pushButton:
        self.dataManage_homedata_pushButton.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(5))

        #dataManage_quit_pushButton:
        self.dataManage_quit_pushButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

        #user_informationDisplay_pushButton:
        self.user_informationDisplay_pushButton.clicked.connect(self.informationDisplay)

        #user_animalsDisplay_pushButton:
        self.user_animalsDisplay_pushButton.clicked.connect(lambda:self.stackedWidget_3.setCurrentIndex(1))

        #user_quit_pushButton:
        self.user_quit_pushButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

        #login_page：登录功能的基本实现：
        self.login_login_pushButton.clicked.connect(self.isManager)

        #dataManage:animal_search_pushButton:
        self.animal_search_pushButton.clicked.connect(self.animal_search)

        #dataManage:animal_delete_pushButton:
        self.animal_delete_pushButton.clicked.connect(self.animal_delete)

        #dataManage:animal_create_pushButton:
        self.animal_create_pushButton.clicked.connect(self.animal_create)

        #dataManage:self.animal_update_pushButton:
        self.animal_update_pushButton.clicked.connect(self.animal_update)

        #dataManage:self.passenger_search_pushButton:
        self.passenger_search_pushButton.clicked.connect(self.passenger_search)

        #dataManage:self_passenger_delete_pushButton:
        self.passenger_delete_pushButton.clicked.connect(self.passenger_delete)

        #dataManage:passenger_create_pushButton:
        self.passenger_create_pushButton.clicked.connect(self.passenger_create)

        #dataManage:passenger_update_pushButton:
        self.passenger_update_pushButton.clicked.connect(self.passenger_update)

        #dataManage:worker_search_pushButton:
        self.worker_search_pushButton.clicked.connect(self.worker_search)

        #dataManage:worker_delete_pushButton:
        self.worker_delete_pushButton.clicked.connect(self.worker_delete)

        #dataManage:worker_create_pushButton:
        self.worker_create_pushButton.clicked.connect(self.worker_create)

        #dataManage:worker_update_pushButton:
        self.worker_update_pushButton.clicked.connect(self.worker_update)

        #dataManage:house_search_pushButton:
        self.house_search_pushButton.clicked.connect(self.house_search)

        #dataManage:house_delete_pushButton:
        self.house_delete_pushButton.clicked.connect(self.house_delete)

        #dataManage:house_create_pushButton:
        self.house_create_pushButton.clicked.connect(self.house_create)

        #dataManage:house_update_pushButton:
        self.house_update_pushButton.clicked.connect(self.house_update)

        #dataManage:apartment_search_pushButton:
        self.apartment_search_pushButton.clicked.connect(self.apartment_search)

        #dataManage:apartment_delete_pushButton:
        self.apartment_delete_pushButton.clicked.connect(self.apartment_delete)

        #dataManage:apartment_create_pushButton:
        self.apartment_create_pushButton.clicked.connect(self.apartment_create)

        #dataManage:apartment_update_pushButton:
        self.apartment_update_pushButton.clicked.connect(self.apartment_update)

        #dataManage:home_search_pushButton:
        self.home_search_pushButton.clicked.connect(self.home_search)

        #dataManage:home_delete_pushButton:
        self.home_delete_pushButton.clicked.connect(self.home_delete)

        #dataManage:home_create_pushButton:
        self.home_create_pushButton.clicked.connect(self.home_create)

        #dataManage:home_update_pushButton:
        self.home_update_pushButton.clicked.connect(self.home_update)

        #user:personalInformation_save_pushButton:
        self.personalInformation_save_pushButton.clicked.connect(self.personalInformation_save)

        #user:viewAnimal_search_pushButton:
        self.viewAnimal_search_pushButton.clicked.connect(self.viewAnimal_search)


    #判断是管理员还是用户从而跳转到不同界面;
    def isManager(self):
        account=self.login_account_lineEdit.text()
        password=self.login_password_lineEdit.text()
        if len(account)==0 or len(password)==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            if account == 'admin':
                if password == 'admin1234':
                    self.stackedWidget.setCurrentIndex(2)
                else:
                    QMessageBox.warning(self, "Warning", "Error:Account Or Password Incorrect!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            else:
                db = pymysql.connect(host='localhost',
                                     user='root',
                                     password='20020911Zjl',
                                     database='zoo_manage_sysytem',
                                     charset='utf8')
                cursor = db.cursor()
                sqlSelect = "select password from pub_passenger where passenger_id='" + account+"'"
                response1 = cursor.execute(sqlSelect)
                # response=0说明为新用户，则登录密码即为初始密码；response=1则是已存在账号，观察账号与密码是否匹配；
                if response1 == 0:
                    if len(account) != 11:
                        QMessageBox.warning(self, "Warning", "Wraning:Account Format Error!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                        # account长度不为11时认为账号无效并跳出弹窗：warning:Account Fromat Error!
                    else:
                        sqlAdd = 'insert into pub_passenger(passenger_id,password) values (%s,%s)'
                        try:
                            cursor.execute(sqlAdd, (account, password))
                            db.commit()
                            self.stackedWidget.setCurrentIndex(3)
                        except:
                            db.rollback()
                else:
                    data_password = cursor.fetchall()
                    if data_password[0][0] == password:  # pymysql返回结果为嵌套式元组;
                        self.stackedWidget.setCurrentIndex(3)
                    else:
                        QMessageBox.warning(self, "Warning", "Error:Account Or Password Incorrect!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                        # 账号密码不匹配，无法登录；
                cursor.close()
                db.close()


    #animal_page功能实现：
    #animal_search:
    def animal_search(self):
        animal_id=self.animal_id_input_lineEdit.text()
        animal_gender=self.animal_gender_input_comboBox.currentText()
        if animal_gender=='unknown':#性别为unknown时设置为空
            animal_gender=''
        animal_homeid=self.animal_homeid_input_lineEdit.text()
        animal_keeperid=self.animal_keeperid_input_lineEdit.text()
        animal_age=self.animal_age_input_lineEdit.text()
        animal_name=self.animal_name_input_lineEdit.text()
        animal_species=self.animal_species_input_lineEdit.text()
        animal_dict={"animal_id":animal_id,
                     "age":animal_age,
                     "species":animal_species,
                     "home_id":animal_homeid,
                     "animal_name":animal_name,
                     "keeper_id":animal_keeperid,
                     "gender":animal_gender}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select * from pub_animals where "
        tempsqlSelect=sqlSelect
        for i in animal_dict:
            if len(animal_dict[i])!=0:
                tempstr=i+"='"+animal_dict[i]+"' And "
                sqlSelect=sqlSelect+tempstr
        if tempsqlSelect==sqlSelect:
            sqlSelect="select * from pub_animals"
        else:
            list_sqlSelect = list(sqlSelect)
            for i in range(-5, 0, 1):
                del (list_sqlSelect[i])
            sqlSelect = ''.join(list_sqlSelect)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            self.animal_animalDisplay_tableWidget.setRowCount(0)
            QMessageBox.warning(self,"Error","Error:No Such Data Exists!",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            self.animal_animalDisplay_tableWidget.setRowCount(0)
            #用于将之前查询数据清空，使表中只显示本次查询数据;
            data=cursor.fetchall()
            for i in range(len(data)):
                row_count=self.animal_animalDisplay_tableWidget.rowCount()
                self.animal_animalDisplay_tableWidget.insertRow(row_count)
                for j in range(len(data[i])):
                    self.animal_animalDisplay_tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j])))
        cursor.close()
        db.close()

    #animal_delete:
    def animal_delete(self):
        animal_id=self.animal_id_input_lineEdit.text()
        animal_gender=self.animal_gender_input_comboBox.currentText()
        if animal_gender=='unknown':#性别为unknown时设置为空
            animal_gender=''
        animal_homeid=self.animal_homeid_input_lineEdit.text()
        animal_keeperid=self.animal_keeperid_input_lineEdit.text()
        animal_age=self.animal_age_input_lineEdit.text()
        animal_name=self.animal_name_input_lineEdit.text()
        animal_species=self.animal_species_input_lineEdit.text()
        animal_dict={"animal_id":animal_id,
                     "age":animal_age,
                     "species":animal_species,
                     "home_id":animal_homeid,
                     "animal_name":animal_name,
                     "keeper_id":animal_keeperid,
                     "gender":animal_gender}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select animal_id from pub_animals where "
        tempsqlSelect=sqlSelect
        sqlDel="Delete From pub_animals where "
        tempsqlDel=sqlDel
        for i in animal_dict:
            if len(animal_dict[i])!=0:
                tempstr=i+"='"+animal_dict[i]+"' And "
                sqlDel=sqlDel+tempstr
                sqlSelect=sqlSelect+tempstr
        if tempsqlSelect==sqlSelect:
            sqlSelect="select animal_id from pub_animals"
        else:
            list_sqlSelect = list(sqlSelect)
            for i in range(-5, 0, 1):
                del (list_sqlSelect[i])
            sqlSelect = "".join(list_sqlSelect)
        if tempsqlDel==sqlDel:
            sqlDel="Delete From pub_animals"
        else:
            list_sqlDel = list(sqlDel)
            for i in range(-5, 0, 1):
                del (list_sqlDel[i])
            sqlDel = "".join(list_sqlDel)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            QMessageBox.warning(self,"Warning","Error:No Such Data Exists",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            try:
                cursor.execute(sqlDel)
                db.commit()
                QMessageBox.information(self, "Information", "Information:Deleted %d Data" % (response1),QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            except:
                db.rollback()
        cursor.close()
        db.close()

    #animal_create:
    def animal_create(self):
        animal_id = self.animal_id_input_lineEdit.text()
        animal_gender = self.animal_gender_input_comboBox.currentText()
        if animal_gender == 'unknown':  # 性别为unknown时设置为空
            animal_gender = ''
        animal_homeid = self.animal_homeid_input_lineEdit.text()
        animal_keeperid = self.animal_keeperid_input_lineEdit.text()
        animal_age = self.animal_age_input_lineEdit.text()
        animal_name = self.animal_name_input_lineEdit.text()
        animal_species = self.animal_species_input_lineEdit.text()
        animal_dict = {"animal_id": animal_id,
                       "age": animal_age,
                       "species": animal_species,
                       "home_id": animal_homeid,
                       "animal_name": animal_name,
                       "keeper_id": animal_keeperid,
                       "gender": animal_gender}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(animal_dict["home_id"])!=8 or len(animal_dict["keeper_id"])!=7 or len(animal_dict["animal_id"])==0:
            QMessageBox.warning(self,"Warning","Error:Lack Necessary Information!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect = "select animal_id from pub_animals where animal_id='" + animal_dict["animal_id"] + "'"
            response1 = cursor.execute(sqlSelect)
            if response1 != 0:
                QMessageBox.warning(self, "Warning", "Error:Such Data Existed!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlInsert = "Insert into pub_animals ("
                for i in animal_dict:
                    sqlInsert = sqlInsert + i + ","
                list_sqlInsert = list(sqlInsert)
                del (list_sqlInsert[-1])
                sqlInsert = "".join(list_sqlInsert)
                sqlInsert = sqlInsert + ") values ("
                for i in animal_dict:
                    if len(animal_dict[i]) != 0:
                        sqlInsert = sqlInsert + "'" + animal_dict[i] + "',"
                    else:
                        sqlInsert = sqlInsert + "null,"
                list_sqlInsert = list(sqlInsert)
                del (list_sqlInsert[-1])
                sqlInsert = "".join(list_sqlInsert)
                sqlInsert = sqlInsert + ")"
                try:
                    cursor.execute(sqlInsert)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Create Data Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()

    #animal_update:
    def animal_update(self):
        animal_id = self.animal_id_input_lineEdit.text()
        animal_gender = self.animal_gender_input_comboBox.currentText()
        if animal_gender == 'unknown':  # 性别为unknown时设置为空
            animal_gender = ''
        animal_homeid = self.animal_homeid_input_lineEdit.text()
        animal_keeperid = self.animal_keeperid_input_lineEdit.text()
        animal_age = self.animal_age_input_lineEdit.text()
        animal_name = self.animal_name_input_lineEdit.text()
        animal_species = self.animal_species_input_lineEdit.text()
        animal_dict = {"animal_id": animal_id,
                       "age": animal_age,
                       "species": animal_species,
                       "home_id": animal_homeid,
                       "animal_name": animal_name,
                       "keeper_id": animal_keeperid,
                       "gender": animal_gender}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(animal_dict["animal_id"])==0:
            QMessageBox.warning(self,"Warning","Error:Lack Necessary Information!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select animal_id from pub_animals where animal_id='"+animal_dict["animal_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1==0:
                QMessageBox.warning(self,"Warning","Error:No Such Data Exists!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            else:
                sqlUpdate="update pub_animals set "
                for i in animal_dict:
                    if len(animal_dict[i])!=0 and i!="animal_id":
                        tempstr=i+"='"+animal_dict[i]+"',"
                        sqlUpdate=sqlUpdate+tempstr
                list_sqlUpdate=list(sqlUpdate)
                del(list_sqlUpdate[-1])
                sqlUpdate="".join(list_sqlUpdate)
                sqlUpdate=sqlUpdate+" where animal_id='"+animal_dict["animal_id"]+"' "
                try:
                    cursor.execute(sqlUpdate)
                    db.commit()
                    QMessageBox.information(self,"Information","Information:Update Successfully!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()


    #passenger_page功能实现:
    #passenger_search:
    def passenger_search(self):
        passenger_id=self.passenger_passendgeid_input_lineEdit.text()
        passenger_guideid=self.passenger_guideid_input_lineEdit.text()
        passenger_gender=self.passenger_gender_input_comboBox.currentText()
        if passenger_gender=="unknown":
            passenger_gender=""
        passenger_age=self.passenger_age_input_lineEdit.text()
        passenger_name=self.passenger_name_input_lineEdit.text()
        passenger_dict={"passenger_id":passenger_id,
                        "gender":passenger_gender,
                        "name":passenger_name,
                        "age":passenger_age,
                        "guide_id":passenger_guideid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select * from pub_passenger where "
        tempsqlSelect=sqlSelect
        for i in passenger_dict:
            if len(passenger_dict[i])!=0:
                tempstr=i+"='"+passenger_dict[i]+"' And "
                sqlSelect=sqlSelect+tempstr
        if tempsqlSelect==sqlSelect:
            sqlSelect="select * from pub_passenger"
        else:
            list_sqlSelect = list(sqlSelect)
            for i in range(-5, 0, 1):
                del (list_sqlSelect[i])
            sqlSelect = "".join(list_sqlSelect)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            self.passenger_passengerDisplay_tableWidget.setRowCount(0)
            QMessageBox.warning(self,"Error","Error:No Such Data Exists!",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            self.passenger_passengerDisplay_tableWidget.setRowCount(0)
            data=cursor.fetchall()
            for i in range(len(data)):
                row_count=self.passenger_passengerDisplay_tableWidget.rowCount()
                self.passenger_passengerDisplay_tableWidget.insertRow(row_count)
                for j in range(len(data[i])):
                    self.passenger_passengerDisplay_tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j])))
        cursor.close()
        db.close()

    #passenger_delete:
    def passenger_delete(self):
        passenger_id = self.passenger_passendgeid_input_lineEdit.text()
        passenger_guideid = self.passenger_guideid_input_lineEdit.text()
        passenger_gender = self.passenger_gender_input_comboBox.currentText()
        if passenger_gender == "unknown":
            passenger_gender = ""
        passenger_age = self.passenger_age_input_lineEdit.text()
        passenger_name = self.passenger_name_input_lineEdit.text()
        passenger_dict = {"passenger_id": passenger_id,
                          "gender": passenger_gender,
                          "name": passenger_name,
                          "age": passenger_age,
                          "guide_id": passenger_guideid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select passenger_id from pub_passenger where "
        tempsqlSelect=sqlSelect
        sqlDel="delete from pub_passenger where "
        tempsqlDel=sqlDel
        for i in passenger_dict:
            if len(passenger_dict[i])!=0:
                tempstr=i+"='"+passenger_dict[i]+"' And "
                sqlSelect=sqlSelect+tempstr
                sqlDel=sqlDel+tempstr
        if tempsqlSelect==sqlSelect or tempsqlDel==sqlDel:
            sqlSelect="select passenger_id from pub_passenger"
            sqlDel = "delete from pub_passenger"
        else:
            list_sqlDel = list(sqlDel)
            list_sqlSelect = list(sqlSelect)
            for i in range(-5, 0, 1):
                del (list_sqlSelect[i])
                del (list_sqlDel[i])
            sqlSelect = "".join(list_sqlSelect)
            sqlDel = "".join(list_sqlDel)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            QMessageBox.warning(self, "Warning", "Error:No Such Data Exists", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            try:
                cursor.execute(sqlDel)
                db.commit()
                QMessageBox.information(self, "Information", "Information:Deleted %d Data" % (response1),QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            except:
                db.rollback()
        cursor.close()
        db.close()

    #passenger_create:
    def passenger_create(self):
        passenger_id = self.passenger_passendgeid_input_lineEdit.text()
        passenger_guideid = self.passenger_guideid_input_lineEdit.text()
        passenger_gender = self.passenger_gender_input_comboBox.currentText()
        if passenger_gender == "unknown":
            passenger_gender = ""
        passenger_age = self.passenger_age_input_lineEdit.text()
        passenger_name = self.passenger_name_input_lineEdit.text()
        passenger_dict = {"passenger_id": passenger_id,
                          "gender": passenger_gender,
                          "name": passenger_name,
                          "age": passenger_age,
                          "guide_id": passenger_guideid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(passenger_dict["passenger_id"])!=11 or len(passenger_dict["guide_id"])!=7:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select passenger_id from pub_passenger where passenger_id='"+passenger_dict["passenger_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1!=0:
                QMessageBox.warning(self, "Warning", "Error:Such Data Existed!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlInsert="insert into pub_passenger ("
                for i in passenger_dict:
                    sqlInsert=sqlInsert+i+","
                sqlInsert=sqlInsert+"password) values ("
                for i in passenger_dict:
                    if len(passenger_dict[i])!=0:
                        sqlInsert=sqlInsert+"'"+passenger_dict[i]+"',"
                    else:
                        sqlInsert=sqlInsert+"null,"
                sqlInsert=sqlInsert+passenger_dict["passenger_id"]+")"
                try:
                    cursor.execute(sqlInsert)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Create Data Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()

    #passenger_update:
    def passenger_update(self):
        passenger_id = self.passenger_passendgeid_input_lineEdit.text()
        passenger_guideid = self.passenger_guideid_input_lineEdit.text()
        passenger_gender = self.passenger_gender_input_comboBox.currentText()
        if passenger_gender == "unknown":
            passenger_gender = ""
        passenger_age = self.passenger_age_input_lineEdit.text()
        passenger_name = self.passenger_name_input_lineEdit.text()
        passenger_dict = {"passenger_id": passenger_id,
                          "gender": passenger_gender,
                          "name": passenger_name,
                          "age": passenger_age,
                          "guide_id": passenger_guideid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(passenger_dict["passenger_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select passenger_id from pub_passenger where passenger_id='"+passenger_dict["passenger_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1==0:
                QMessageBox.warning(self, "Warning", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlUpdate="update pub_passenger set "
                for i in passenger_dict:
                    if len(passenger_dict[i])!=0 and i!="passenger_id":
                        tempstr=i+"='"+passenger_dict[i]+"',"
                        sqlUpdate=sqlUpdate+tempstr
                list_sqlUpdate=list(sqlUpdate)
                del(list_sqlUpdate[-1])
                sqlUpdate="".join(list_sqlUpdate)
                sqlUpdate=sqlUpdate+" where passenger_id='"+passenger_dict["passenger_id"]+"'"
                try:
                    cursor.execute(sqlUpdate)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Update Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()


    #worker_page功能实现：
    #workeder_search:
    def worker_search(self):
        worker_job=self.worker_staff_comboBox.currentText()
        worker_id=self.worker_id_input_lineEdit.text()
        worker_houseid=self.worker_houseid_input_lineEdit.text()
        worker_apartmentid=self.worker_apartmentid_input_lineEdit.text()
        worker_name=self.worker_name_input_lineEdit.text()
        worker_gender=self.worker_gender_input_comboBox.currentText()
        if worker_gender=="unknown":
            worker_gender=""
        worker_age=self.worker_age_input_lineEdit.text()
        worker_salary=self.worker_salary_input_lineEdit.text()
        worker_workyears=self.worker_workyears_input_lineEdit.text()
        worker_dict={"worker_id":worker_id,
                     "name":worker_name,
                     "gender":worker_gender,
                     "age":worker_age,
                     "salary":worker_salary,
                     "work_years":worker_workyears,
                     "house_id":worker_houseid,
                     "apartment_id":worker_apartmentid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if worker_job!="unknown":
            if worker_job=="guide":
                sqlSelect="select * from pub_guide where "
                key="guide_id"
            else:
                sqlSelect="select * from pub_keeper where "
                key="keeper_id"
            tempsqlSelect=sqlSelect
            if len(worker_dict["worker_id"])!=0:
                sqlSelect=sqlSelect+key+"='"+worker_dict["worker_id"]+"' and "
            for i in worker_dict:
                if len(worker_dict[i])!=0 and i!="worker_id":
                    tempstr=i+"='"+worker_dict[i]+"' And "
                    sqlSelect=sqlSelect+tempstr
            if tempsqlSelect==sqlSelect:
                list_sqlSelect=list(sqlSelect)
                for i in range(-7,0,1):
                    del(list_sqlSelect[i])
                sqlSelect="".join(list_sqlSelect)
            else:
                list_sqlSelect = list(sqlSelect)
                for i in range(-5, 0, 1):
                    del (list_sqlSelect[i])
                sqlSelect = "".join(list_sqlSelect)
            response1=cursor.execute(sqlSelect)
            if response1==0:
                self.worker_workerDisplay_tableWidget.setRowCount(0)
                QMessageBox.warning(self, "Error", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                self.worker_workerDisplay_tableWidget.setRowCount(0)
                data=cursor.fetchall()
                for i in range(len(data)):
                    row_count=self.worker_workerDisplay_tableWidget.rowCount()
                    self.worker_workerDisplay_tableWidget.insertRow(row_count)
                    self.worker_workerDisplay_tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(worker_job))
                    for j in range(len(data[i])):
                        self.worker_workerDisplay_tableWidget.setItem(i,j+1,QtWidgets.QTableWidgetItem(str(data[i][j])))
        else:
            sqlSelect1="select * from pub_guide where "
            sqlSelect2="select * from pub_keeper where "
            if len(worker_dict["worker_id"])!=0:
                sqlSelect1=sqlSelect1+"guide_id='"+worker_dict["worker_id"]+"' And "
                sqlSelect2=sqlSelect2+"keeper_id='"+worker_dict["worker_id"]+"' And "
            else:
                pass
            currentStr=""
            for i in worker_dict:
                if len(worker_dict[i])!=0 and i!="worker_id":
                    tempstr=i+"='"+worker_dict[i]+"' And "
                    currentStr=currentStr+tempstr
            sqlSelect1 = sqlSelect1 + currentStr
            sqlSelect2 = sqlSelect2 + currentStr
            if len(currentStr)==0 and len(worker_dict["worker_id"])==0:
                sqlSelect1="select * from pub_guide"
                sqlSelect2="select * from pub_keeper"
            else:
                list_sqlSelect1=list(sqlSelect1)
                list_sqlSelect2=list(sqlSelect2)
                for i in range(-5,0,1):
                    del(list_sqlSelect1[i])
                    del(list_sqlSelect2[i])
                sqlSelect1="".join(list_sqlSelect1)
                sqlSelect2="".join(list_sqlSelect2)
            response1=cursor.execute(sqlSelect1)
            data1=cursor.fetchall()
            response2=cursor.execute(sqlSelect2)
            data2=cursor.fetchall()
            if response1==0 and response2==0:
                self.worker_workerDisplay_tableWidget.setRowCount(0)
                QMessageBox.warning(self, "Error", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                self.worker_workerDisplay_tableWidget.setRowCount(0)
                if response1!=0:
                    for i in range(len(data1)):
                        row_count=self.worker_workerDisplay_tableWidget.rowCount()
                        self.worker_workerDisplay_tableWidget.insertRow(row_count)
                        self.worker_workerDisplay_tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem("guide"))
                        for j in range(len(data1[i])):
                            self.worker_workerDisplay_tableWidget.setItem(i, j+1,QtWidgets.QTableWidgetItem(str(data1[i][j])))
                else:
                    pass
                rows=self.worker_workerDisplay_tableWidget.rowCount()
                if response2!=0:
                    for i in range(len(data2)):
                        row_count=self.worker_workerDisplay_tableWidget.rowCount()
                        self.worker_workerDisplay_tableWidget.insertRow(row_count)
                        self.worker_workerDisplay_tableWidget.setItem(rows+i,0,QtWidgets.QTableWidgetItem("keeper"))
                        for j in range(len(data2[i])):
                            self.worker_workerDisplay_tableWidget.setItem(rows+i,j+1,QtWidgets.QTableWidgetItem(str(data2[i][j])))
                else:
                    pass
        cursor.close()
        db.close()

    #worker_delete:
    def worker_delete(self):
        worker_job = self.worker_staff_comboBox.currentText()
        worker_id = self.worker_id_input_lineEdit.text()
        worker_houseid = self.worker_houseid_input_lineEdit.text()
        worker_apartmentid = self.worker_apartmentid_input_lineEdit.text()
        worker_name = self.worker_name_input_lineEdit.text()
        worker_gender = self.worker_gender_input_comboBox.currentText()
        if worker_gender == "unknown":
            worker_gender = ""
        worker_age = self.worker_age_input_lineEdit.text()
        worker_salary = self.worker_salary_input_lineEdit.text()
        worker_workyears = self.worker_workyears_input_lineEdit.text()
        worker_dict = {"worker_id": worker_id,
                       "name": worker_name,
                       "gender": worker_gender,
                       "age": worker_age,
                       "salary": worker_salary,
                       "work_years": worker_workyears,
                       "house_id": worker_houseid,
                       "apartment_id": worker_apartmentid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if worker_job!="unknown":
            if worker_job=="guide":
                sqlDel="delete from pub_guide where "
                sqlSelect="select guide_id from pub_guide where "
                key="guide_id"
            else:
                sqlDel="delete from pub_keeper where "
                sqlSelect="select keeper_id from pub_keeper where "
                key="keeper_id"
            tempsqlDel=sqlDel
            tempsqlSelect=sqlSelect
            if len(worker_dict["worker_id"])!=0:
                sqlDel=sqlDel+key+"='"+worker_dict["worker_id"]+"' and "
                sqlSelect=sqlSelect+key+"='"+worker_dict["worker_id"]+"' and "
            for i in worker_dict:
                if len(worker_dict[i])!=0 and i!="worker_id":
                    sqlDel=sqlDel+i+"='"+worker_dict[i]+"' and "
                    sqlSelect=sqlSelect+i+"='"+worker_dict[i]+"' and "
            if tempsqlDel==sqlDel or tempsqlSelect==sqlSelect:
                list_sqlDel=list(sqlDel)
                list_sqlSelect=list(sqlSelect)
                for i in range(-7,0,1):
                    del(list_sqlSelect[i])
                    del(list_sqlDel[i])
                sqlDel="".join(list_sqlDel)
                sqlSelect="".join(list_sqlSelect)
            else:
                list_sqlDel=list(sqlDel)
                list_sqlSelect=list(sqlSelect)
                for i in range(-5,0,1):
                    del(list_sqlSelect[i])
                    del(list_sqlDel[i])
                sqlDel="".join(list_sqlDel)
                sqlSelect="".join(list_sqlSelect)
                response1=cursor.execute(sqlSelect)
                if response1==0:
                    QMessageBox.warning(self, "Warning", "Error:No Such Data Exists", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                else:
                    try:
                        cursor.execute(sqlDel)
                        db.commit()
                        QMessageBox.information(self, "Information", "Information:Deleted %d Data" % (response1),QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    except:
                        db.rollback()
        else:
            sqlSelect1="select guide_id from pub_guide where "
            sqlDel1="delete from pub_guide where "
            sqlSelect2="select keeper_id from pub_keeper where "
            sqlDel2="delete from pub_keeper where  "
            tempsqlSelect1=sqlSelect1
            if len(worker_dict["worker_id"])!=0:
                tempstr1="guide_id='"+worker_dict["worker_id"]+"' and "
                sqlSelect1=sqlSelect1+tempstr1
                sqlDel1=sqlDel1+tempstr1
                tempstr2="keeper_id='"+worker_dict["worker_id"]+"' and "
                sqlSelect2=sqlSelect2+tempstr2
                sqlDel2=sqlDel2+tempstr2
            for i in worker_dict:
                if len(worker_dict[i])!=0 and i!="worker_id":
                    tempstr=i+"='"+worker_dict[i]+"' and "
                    sqlSelect1=sqlSelect1+tempstr
                    sqlDel1=sqlDel1+tempstr
                    sqlSelect2=sqlSelect2+tempstr
                    sqlDel2=sqlDel2+tempstr
            if tempsqlSelect1==sqlSelect1:
                sqlSelect1="select guide_id from pub_guide"
                sqlDel1="delete from pub_guide"
                sqlSelect2="select keeper_id from pub_keeper"
                sqlDel2="delete from pub_keeper"
            else:
                list_sqlSelect1=list(sqlSelect1)
                list_sqlDel1=list(sqlDel1)
                list_sqlSelect2=list(sqlSelect2)
                list_sqlDel2=list(sqlDel2)
                for i in range(-5,0,1):
                    del(list_sqlSelect1[i])
                    del(list_sqlSelect2[i])
                    del(list_sqlDel1[i])
                    del(list_sqlDel2[i])
                sqlSelect1="".join(list_sqlSelect1)
                sqlSelect2="".join(list_sqlSelect2)
                sqlDel1="".join(list_sqlDel1)
                sqlDel2="".join(list_sqlDel2)
                response1=cursor.execute(sqlSelect1)
                response2=cursor.execute(sqlSelect2)
                if response1==0 and response2==0:
                    QMessageBox.warning(self, "Warning", "Error:No Such Data Exists", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                else:
                    if response1 != 0:
                        try:
                            cursor.execute(sqlDel1)
                            db.commit()
                        except:
                            db.rollback()
                    else:
                        pass
                    if response2 != 0:
                        try:
                            cursor.execute(sqlDel2)
                            db.commit()
                        except:
                            db.rollback()
                    else:
                        pass
                    QMessageBox.information(self, "Information","Information:Deleted %d Data" % (response1 + response2),QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        cursor.close()
        db.close()

    #worker_create:
    def worker_create(self):
        worker_job = self.worker_staff_comboBox.currentText()
        worker_id = self.worker_id_input_lineEdit.text()
        worker_houseid = self.worker_houseid_input_lineEdit.text()
        worker_apartmentid = self.worker_apartmentid_input_lineEdit.text()
        worker_name = self.worker_name_input_lineEdit.text()
        worker_gender = self.worker_gender_input_comboBox.currentText()
        if worker_gender == "unknown":
            worker_gender = ""
        worker_age = self.worker_age_input_lineEdit.text()
        worker_salary = self.worker_salary_input_lineEdit.text()
        worker_workyears = self.worker_workyears_input_lineEdit.text()
        worker_dict = {"worker_id": worker_id,
                       "name": worker_name,
                       "gender": worker_gender,
                       "age": worker_age,
                       "salary": worker_salary,
                       "work_years": worker_workyears,
                       "house_id": worker_houseid,
                       "apartment_id": worker_apartmentid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(worker_dict["worker_id"])!=7 or len(worker_dict["house_id"])==0 or len(worker_dict["apartment_id"])==0 or worker_job=="unknown":
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            if worker_job == "guide":
                sqlSelect = "select guide_id from pub_guide where guide_id='" + worker_dict["worker_id"] + "'"
                key="guide"
            else:
                sqlSelect = "select keeper_id from pub_keeper where keeper_id='" + worker_dict["worker_id"] + "'"
                key="keeper"
            response1 = cursor.execute(sqlSelect)
            if response1 != 0:
                QMessageBox.warning(self, "Warning", "Error:Such Data Existed!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlInsert="insert into pub_"+key+" ("
                for i in worker_dict:
                    if i=="worker_id":
                        sqlInsert=sqlInsert+key+"_id,"
                    elif i=="apartment_id":
                        sqlInsert=sqlInsert+i+") values ("
                    else:
                        sqlInsert=sqlInsert+i+","
                for i in worker_dict:
                    if len(worker_dict[i])!=0:
                        sqlInsert=sqlInsert+"'"+worker_dict[i]+"',"
                    else:
                        sqlInsert=sqlInsert+"null,"
                list_sqlInsert=list(sqlInsert)
                del(list_sqlInsert[-1])
                sqlInsert="".join(list_sqlInsert)
                sqlInsert=sqlInsert+")"
                try:
                    cursor.execute(sqlInsert)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Create Data Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()

    #worker_update:
    def worker_update(self):
        worker_job = self.worker_staff_comboBox.currentText()
        worker_id = self.worker_id_input_lineEdit.text()
        worker_houseid = self.worker_houseid_input_lineEdit.text()
        worker_apartmentid = self.worker_apartmentid_input_lineEdit.text()
        worker_name = self.worker_name_input_lineEdit.text()
        worker_gender = self.worker_gender_input_comboBox.currentText()
        if worker_gender == "unknown":
            worker_gender = ""
        worker_age = self.worker_age_input_lineEdit.text()
        worker_salary = self.worker_salary_input_lineEdit.text()
        worker_workyears = self.worker_workyears_input_lineEdit.text()
        worker_dict = {"worker_id": worker_id,
                       "name": worker_name,
                       "gender": worker_gender,
                       "age": worker_age,
                       "salary": worker_salary,
                       "work_years": worker_workyears,
                       "house_id": worker_houseid,
                       "apartment_id": worker_apartmentid}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(worker_dict["worker_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            if worker_job!="unknown":
                sqlSelect="select "+worker_job+"_id from pub_"+worker_job+" where "+worker_job+"_id='"+worker_dict["worker_id"]+"'"
                response1=cursor.execute(sqlSelect)
                if response1==0:
                    QMessageBox.warning(self, "Warning", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                else:
                    sqlUpdate="update pub_"+worker_job+" set "
                    for i in worker_dict:
                        if len(worker_dict[i])!=0 and i!="worker_id":
                            tempstr=i+"='"+worker_dict[i]+"',"
                            sqlUpdate=sqlUpdate+tempstr
                    list_sqlUpdate=list(sqlUpdate)
                    del(list_sqlUpdate[-1])
                    sqlUpdate="".join(list_sqlUpdate)
                    sqlUpdate=sqlUpdate+" where "+worker_job+"_id='"+worker_dict["worker_id"]+"'"
                    try:
                        cursor.execute(sqlUpdate)
                        db.commit()
                        QMessageBox.information(self, "Information", "Information:Update Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    except:
                        db.rollback()
            else:
                sqlSelect1="select guide_id from pub_guide where guide_id='"+worker_dict["worker_id"]+"'"
                sqlSelect2="select keeper_id from pub_keeper where keeper_id='"+worker_dict["worker_id"]+"'"
                response1=cursor.execute(sqlSelect1)
                response2=cursor.execute(sqlSelect2)
                if response1==0 and response2==0:
                    QMessageBox.warning(self, "Warning", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
                else:
                    if response1!=0:
                        sqlUpdate="update pub_guide set "
                        for i in worker_dict:
                            if len(worker_dict[i])!=0 and i!="worker_id":
                                tempstr=i+"='"+worker_dict[i]+"',"
                                sqlUpdate=sqlUpdate+tempstr
                        list_sqlUpdate=list(sqlUpdate)
                        del(list_sqlUpdate[-1])
                        sqlUpdate="".join(list_sqlUpdate)
                        sqlUpdate=sqlUpdate+" where guide_id='"+worker_dict["worker_id"]+"'"
                        try:
                            cursor.execute(sqlUpdate)
                            db.commit()
                            QMessageBox.information(self, "Information", "Information:Update Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                        except:
                            db.rollback()
                    else:
                        sqlUpdate="update pub_keeper set "
                        for i in worker_dict:
                            if len(worker_dict[i])!=0 and i!="worker_id":
                                tempstr=i+"='"+worker_dict[i]+"',"
                                sqlUpdate=sqlUpdate+tempstr
                        list_sqlUpdate=list(sqlUpdate)
                        del(list_sqlUpdate[-1])
                        sqlUpdate="".join(list_sqlUpdate)
                        sqlUpdate=sqlUpdate+" where keeper_id='"+worker_dict["worker_id"]+"'"
                        try:
                            cursor.execute(sqlUpdate)
                            db.commit()
                            QMessageBox.information(self, "Information", "Information:Update Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                        except:
                            db.rollback()
        cursor.close()
        db.close()


    #house_page功能实现:
    #house_search:
    def house_search(self):
        house_id=self.house_id_input_lineEdit.text()
        name=self.house_name_input_lineEdit.text()
        homes=self.house_homes_input_lineEdit.text()
        guides=self.house_guides_input_lineEdit.text()
        keepers=self.house_keepers_input_lineEdit.text()
        house_dict={"house_id":house_id,
                    "name":name,
                    "num_of_homes":homes,
                    "num_of_guides":guides,
                    "num_of_keepers":keepers}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select * from pub_house where "
        tempsqlSelect=sqlSelect
        for i in house_dict:
            if len(house_dict[i])!=0:
                tempstr=i+"='"+house_dict[i]+"' and "
                sqlSelect=sqlSelect+tempstr
        if sqlSelect==tempsqlSelect:
            sqlSelect="select * from pub_house"
        else:
            list_sqlSelect=list(sqlSelect)
            for i in range(-5,0,1):
                del(list_sqlSelect[i])
            sqlSelect="".join(list_sqlSelect)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            self.house_houseDisplay_tableWidget.setRowCount(0)
            QMessageBox.warning(self, "Error", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            self.house_houseDisplay_tableWidget.setRowCount(0)
            data=cursor.fetchall()
            for i in range(len(data)):
                row_count=self.house_houseDisplay_tableWidget.rowCount()
                self.house_houseDisplay_tableWidget.insertRow(row_count)
                for j in range(len(data[i])):
                    self.house_houseDisplay_tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j])))
        cursor.close()
        db.close()

    #house_delete:
    def house_delete(self):
        house_id=self.house_id_input_lineEdit.text()
        name=self.house_name_input_lineEdit.text()
        homes=self.house_homes_input_lineEdit.text()
        guides=self.house_guides_input_lineEdit.text()
        keepers=self.house_keepers_input_lineEdit.text()
        house_dict={"house_id":house_id,
                    "name":name,
                    "num_of_homes":homes,
                    "num_of_guides":guides,
                    "num_of_keepers":keepers}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select house_id from pub_house where "
        tempsqlSelect=sqlSelect
        sqlDel="delete from pub_house where "
        for i in house_dict:
            if len(house_dict[i])!=0:
                tempstr=i+"='"+house_dict[i]+"' and "
                sqlSelect=sqlSelect+tempstr
                sqlDel=sqlDel+tempstr
        if sqlSelect==tempsqlSelect:
            sqlSelect="select house_id from pub_house"
            sqlDel="delete from pub_house"
        else:
            list_sqlSelect=list(sqlSelect)
            list_sqlDel=list(sqlDel)
            for i in range(-5,0,1):
                del(list_sqlSelect[i])
                del(list_sqlDel[i])
            sqlSelect="".join(list_sqlSelect)
            sqlDel="".join(list_sqlDel)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            QMessageBox.warning(self, "Warning", "Error:No Such Data Exists", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            try:
                cursor.execute(sqlDel)
                db.commit()
                QMessageBox.information(self, "Information", "Information:Deleted %d Data" % (response1),QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            except:
                db.rollback()
        cursor.close()
        db.close()

    #house_create:
    def house_create(self):
        house_id=self.house_id_input_lineEdit.text()
        name=self.house_name_input_lineEdit.text()
        homes=self.house_homes_input_lineEdit.text()
        guides=self.house_guides_input_lineEdit.text()
        keepers=self.house_keepers_input_lineEdit.text()
        house_dict={"house_id":house_id,
                    "name":name,
                    "num_of_homes":homes,
                    "num_of_guides":guides,
                    "num_of_keepers":keepers}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(house_dict["house_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select house_id from pub_house where house_id='"+house_dict["house_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1!=0:
                QMessageBox.warning(self, "Warning", "Error:Such Data Existed!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlInsert="insert into pub_house ("
                for i in house_dict:
                    sqlInsert=sqlInsert+i+","
                list_sqlInsert=list(sqlInsert)
                del(list_sqlInsert[-1])
                sqlInsert="".join(list_sqlInsert)
                sqlInsert = sqlInsert + ") values ("
                for i in house_dict:
                    if len(house_dict[i])!=0:
                        sqlInsert=sqlInsert+"'"+house_dict[i]+"',"
                    else:
                        sqlInsert=sqlInsert+"null,"
                list_sqlInsert=list(sqlInsert)
                del(list_sqlInsert[-1])
                sqlInsert="".join(list_sqlInsert)
                sqlInsert=sqlInsert+")"
                try:
                    cursor.execute(sqlInsert)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Create Data Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()

    #house_update:
    def house_update(self):
        house_id=self.house_id_input_lineEdit.text()
        name=self.house_name_input_lineEdit.text()
        homes=self.house_homes_input_lineEdit.text()
        guides=self.house_guides_input_lineEdit.text()
        keepers=self.house_keepers_input_lineEdit.text()
        house_dict={"house_id":house_id,
                    "name":name,
                    "num_of_homes":homes,
                    "num_of_guides":guides,
                    "num_of_keepers":keepers}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(house_dict["house_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select house_id from pub_house where house_id='"+house_dict["house_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1==0:
                QMessageBox.warning(self, "Warning", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlUpdate="update pub_house set "
                for i in house_dict:
                    if len(house_dict[i])!=0 and i!="house_id":
                        tempstr=i+"='"+house_dict[i]+"',"
                        sqlUpdate=sqlUpdate+tempstr
                list_sqlUpdate=list(sqlUpdate)
                del(list_sqlUpdate[-1])
                sqlUpdate="".join(list_sqlUpdate)
                sqlUpdate=sqlUpdate+" where house_id='"+house_dict["house_id"]+"'"
                try:
                    cursor.execute(sqlUpdate)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Update Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()


    #apartment_page功能实现:
    #apartment_search:
    def apartment_search(self):
        apartment_id=self.apartment_id_input_lineEdit.text()
        peoples=self.apartment_peoples_input_lineEdit.text()
        name=self.apartment_name_input_lineEdit.text()
        apartment_dict={"apartment_id":apartment_id,
                        "num_of_people":peoples,
                        "name":name}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select * from pub_apartment where "
        tempsqlSelect=sqlSelect
        for i in apartment_dict:
            if len(apartment_dict[i])!=0:
                tempstr=i+"='"+apartment_dict[i]+"' and "
                sqlSelect=sqlSelect+tempstr
        if sqlSelect==tempsqlSelect:
            sqlSelect="select * from pub_apartment"
        else:
            list_sqlSelect=list(sqlSelect)
            for i in range(-5,0,1):
                del(list_sqlSelect[i])
            sqlSelect="".join(list_sqlSelect)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            self.apartment_apartmentDisplay_tableWidget.setRowCount(0)
            QMessageBox.warning(self, "Error", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            self.apartment_apartmentDisplay_tableWidget.setRowCount(0)
            data=cursor.fetchall()
            for i in range(len(data)):
                row_count=self.apartment_apartmentDisplay_tableWidget.rowCount()
                self.apartment_apartmentDisplay_tableWidget.insertRow(row_count)
                for j in range(len(data[i])):
                    self.apartment_apartmentDisplay_tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j])))
        cursor.close()
        db.close()

    #apartment_delete:
    def apartment_delete(self):
        apartment_id = self.apartment_id_input_lineEdit.text()
        peoples = self.apartment_peoples_input_lineEdit.text()
        name = self.apartment_name_input_lineEdit.text()
        apartment_dict = {"apartment_id": apartment_id,
                          "num_of_people": peoples,
                          "name": name}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select apartment_id from pub_apartment where "
        tempsqlSelect=sqlSelect
        sqlDel="delete from pub_apartment where "
        for i in apartment_dict:
            if len(apartment_dict[i])!=0:
                tempstr=i+"='"+apartment_dict[i]+"' and "
                sqlSelect=sqlSelect+tempstr
                sqlDel=sqlDel+tempstr
        if sqlSelect==tempsqlSelect:
            sqlSelect="select apartment_id from pub_apartment"
            sqlDel="delete from pub_apartment"
        else:
            list_sqlSelect=list(sqlSelect)
            list_sqlDel=list(sqlDel)
            for i in range(-5,0,1):
                del(list_sqlSelect[i])
                del(list_sqlDel[i])
            sqlSelect="".join(list_sqlSelect)
            sqlDel="".join(list_sqlDel)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            QMessageBox.warning(self, "Warning", "Error:No Such Data Exists", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            try:
                cursor.execute(sqlDel)
                db.commit()
                QMessageBox.information(self, "Information", "Information:Deleted %d Data" % (response1),QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            except:
                db.rollback()
        cursor.close()
        db.close()

    #apartment_create:
    def apartment_create(self):
        apartment_id = self.apartment_id_input_lineEdit.text()
        peoples = self.apartment_peoples_input_lineEdit.text()
        name = self.apartment_name_input_lineEdit.text()
        apartment_dict = {"apartment_id": apartment_id,
                          "num_of_people": peoples,
                          "name": name}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(apartment_dict["apartment_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select apartment_id from pub_apartment where apartment_id='"+apartment_dict["apartment_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1!=0:
                QMessageBox.warning(self, "Warning", "Error:Such Data Existed!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlInsert="insert into pub_apartment("
                for i in apartment_dict:
                    sqlInsert=sqlInsert+i+","
                list_sqlInsert=list(sqlInsert)
                del(list_sqlInsert[-1])
                sqlInsert="".join(list_sqlInsert)
                sqlInsert = sqlInsert + ") values ("
                for i in apartment_dict:
                    if len(apartment_dict[i])!=0:
                        sqlInsert=sqlInsert+"'"+apartment_dict[i]+"',"
                    else:
                        sqlInsert=sqlInsert+"null,"
                list_sqlInsert=list(sqlInsert)
                del(list_sqlInsert[-1])
                sqlInsert="".join(list_sqlInsert)
                sqlInsert=sqlInsert+")"
                try:
                    cursor.execute(sqlInsert)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Create Data Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()

    #apartment_update:
    def apartment_update(self):
        apartment_id = self.apartment_id_input_lineEdit.text()
        peoples = self.apartment_peoples_input_lineEdit.text()
        name = self.apartment_name_input_lineEdit.text()
        apartment_dict = {"apartment_id": apartment_id,
                          "num_of_people": peoples,
                          "name": name}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(apartment_dict["apartment_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select apartment_id from pub_apartment where apartment_id='"+apartment_dict["apartment_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1==0:
                QMessageBox.warning(self, "Warning", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlUpdate="update pub_apartment set "
                for i in apartment_dict:
                    if len(apartment_dict[i])!=0 and i!="apartment_id":
                        tempstr=i+"='"+apartment_dict[i]+"',"
                        sqlUpdate=sqlUpdate+tempstr
                list_sqlUpdate=list(sqlUpdate)
                del(list_sqlUpdate[-1])
                sqlUpdate="".join(list_sqlUpdate)
                sqlUpdate=sqlUpdate+" where apartment_id='"+apartment_dict["apartment_id"]+"'"
                try:
                    cursor.execute(sqlUpdate)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Update Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()


    #home_page功能实现:
    #home_search:
    def home_search(self):
        home_id=self.home_homeid_input_lineEdit.text()
        house_id=self.home_houseid_input_lineEdit.text()
        name=self.home_name_input_lineEdit.text()
        animals=self.home_animals_input_lineEdit.text()
        home_dict={"home_id":home_id,
                   "name":name,
                   "num_of_animals":animals,
                   "house_id":house_id}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select * from pub_home where "
        tempsqlSelect=sqlSelect
        for i in home_dict:
            if len(home_dict[i])!=0:
                tempstr=i+"='"+home_dict[i]+"' and "
                sqlSelect=sqlSelect+tempstr
        if tempsqlSelect==sqlSelect:
            sqlSelect="select * from pub_home"
        else:
            list_sqlSelect=list(sqlSelect)
            for i in range(-5,0,1):
                del(list_sqlSelect[i])
            sqlSelect="".join(list_sqlSelect)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            self.home_homeDisplay_tableWidget.setRowCount(0)
            QMessageBox.warning(self, "Error", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            self.home_homeDisplay_tableWidget.setRowCount(0)
            data=cursor.fetchall()
            for i in range(len(data)):
                row_count=self.home_homeDisplay_tableWidget.rowCount()
                self.home_homeDisplay_tableWidget.insertRow(row_count)
                for j in range(len(data[i])):
                    self.home_homeDisplay_tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(data[i][j])))
        cursor.close()
        db.close()

    #home_delete:
    def home_delete(self):
        home_id = self.home_homeid_input_lineEdit.text()
        house_id = self.home_houseid_input_lineEdit.text()
        name = self.home_name_input_lineEdit.text()
        animals = self.home_animals_input_lineEdit.text()
        home_dict = {"home_id": home_id,
                     "name": name,
                     "num_of_animals": animals,
                     "house_id": house_id}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect="select home_id from pub_home where "
        tempsqlSelect=sqlSelect
        sqlDel="delete from pub_home where "
        for i in home_dict:
            if len(home_dict[i])!=0:
                tempstr=i+"='"+home_dict[i]+"' and "
                sqlSelect=sqlSelect+tempstr
                sqlDel=sqlDel+tempstr
        if sqlSelect==tempsqlSelect:
            sqlSelect="select home_id from pub_home"
            sqlDel="delete from pub_home"
        else:
            list_sqlSelect=list(sqlSelect)
            list_sqlDel=list(sqlDel)
            for i in range(-5,0,1):
                del(list_sqlSelect[i])
                del(list_sqlDel[i])
            sqlSelect="".join(list_sqlSelect)
            sqlDel="".join(list_sqlDel)
        response1=cursor.execute(sqlSelect)
        if response1==0:
            QMessageBox.warning(self, "Warning", "Error:No Such Data Exists", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            try:
                cursor.execute(sqlDel)
                db.commit()
                QMessageBox.information(self, "Information", "Information:Deleted %d Data" % (response1),QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            except:
                db.rollback()
        cursor.close()
        db.close()

    #home_create:
    def home_create(self):
        home_id = self.home_homeid_input_lineEdit.text()
        house_id = self.home_houseid_input_lineEdit.text()
        name = self.home_name_input_lineEdit.text()
        animals = self.home_animals_input_lineEdit.text()
        home_dict = {"home_id": home_id,
                     "name": name,
                     "num_of_animals": animals,
                     "house_id": house_id}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(home_dict["home_id"])==0 or len(home_dict["house_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlInsert="insert into pub_home("
            for i in home_dict:
                sqlInsert=sqlInsert+i+","
            list_sqlInsert=list(sqlInsert)
            del(list_sqlInsert[-1])
            sqlInsert="".join(list_sqlInsert)
            sqlInsert=sqlInsert+") values ("
            for i in home_dict:
                if len(home_dict[i])!=0:
                    sqlInsert=sqlInsert+"'"+home_dict[i]+"',"
                else:
                    sqlInsert=sqlInsert+"null,"
            list_sqlInsert=list(sqlInsert)
            del(list_sqlInsert[-1])
            sqlInsert="".join(list_sqlInsert)
            sqlInsert=sqlInsert+")"
            try:
                cursor.execute(sqlInsert)
                db.commit()
                QMessageBox.information(self, "Information", "Information:Create Data Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            except:
                db.rollback()
        cursor.close()
        db.close()

    #home_update:
    def home_update(self):
        home_id = self.home_homeid_input_lineEdit.text()
        house_id = self.home_houseid_input_lineEdit.text()
        name = self.home_name_input_lineEdit.text()
        animals = self.home_animals_input_lineEdit.text()
        home_dict = {"home_id": home_id,
                     "name": name,
                     "num_of_animals": animals,
                     "house_id": house_id}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        if len(home_dict["home_id"])==0:
            QMessageBox.warning(self, "Warning", "Error:Lack Necessary Information!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlSelect="select home_id from pub_home where home_id='"+home_dict["home_id"]+"'"
            response1=cursor.execute(sqlSelect)
            if response1==0:
                QMessageBox.warning(self, "Warning", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            else:
                sqlUpdate="update pub_home set "
                for i in home_dict:
                    if len(home_dict[i])!=0 and i!="home_id":
                        tempstr=i+"='"+home_dict[i]+"',"
                        sqlUpdate=sqlUpdate+tempstr
                list_sqlUpdate=list(sqlUpdate)
                del(list_sqlUpdate[-1])
                sqlUpdate="".join(list_sqlUpdate)
                sqlUpdate=sqlUpdate+" where home_id='"+home_dict["home_id"]+"'"
                try:
                    cursor.execute(sqlUpdate)
                    db.commit()
                    QMessageBox.information(self, "Information", "Information:Update Successfully!",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                except:
                    db.rollback()
        cursor.close()
        db.close()


    #user_page:
    #personalInformation_page:
    def personalInformation_save(self):
        passenger_id=self.personalInformation_idDisplay_lineEdit.text()
        password=self.personalInformation_passwordDisplay_lineEdit.text()
        gender=self.personalInformation_genderDisplay_comboBox.currentText()
        if gender=="unknown":
            gender=""
        age=self.personalInformation_ageDisplay_lineEdit.text()
        name=self.personalInformation_nameDisplay_lineEdit.text()
        guide_id=self.personalInformation_guideIdDisplay_lineEdit.text()
        passenger_dict={"passenger_id":passenger_id,
                        "gender":gender,
                        "name":name,
                        "age":age,
                        "guide_id":guide_id,
                        "password":password}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor=db.cursor()
        if len(passenger_dict["passenger_id"])!=11 or len(passenger_dict["password"])==0:
            QMessageBox.warning(self,"Warning","Error:Your Id or Password Unqualified!",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            sqlUpdate="update pub_passenger set "
            sqlSelect="select "
            for i in passenger_dict:
                if i!="passenger_id":
                    if len(passenger_dict[i])!=0:
                        tempstr=i+"='"+passenger_dict[i]+"',"
                    else:
                        tempstr=i+"=null,"
                    sqlUpdate=sqlUpdate+tempstr
            list_sqlUpdate=list(sqlUpdate)
            del(list_sqlUpdate[-1])
            sqlUpdate="".join(list_sqlUpdate)
            sqlUpdate=sqlUpdate+" where passenger_id='"+passenger_dict["passenger_id"]+"'"
            try:
                cursor.execute(sqlUpdate)
                db.commit()
                QMessageBox.information(self,"Information","Information:Save successfully",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            except:
                db.rollback()
        cursor.close()
        db.close()

    #personalInformationDisplay:
    def informationDisplay(self):
        self.stackedWidget_3.setCurrentIndex(0)
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor=db.cursor()
        passenger_id=self.login_account_lineEdit.text()
        sqlSelect="select * from pub_passenger where passenger_id='"+passenger_id+"'"
        response1=cursor.execute(sqlSelect)
        if response1==0:
            pass
        else:
            data=cursor.fetchall()
            self.personalInformation_idDisplay_lineEdit.setText(data[0][0])
            self.personalInformation_idDisplay_lineEdit.setReadOnly(True)
            self.personalInformation_genderDisplay_comboBox.setCurrentText(data[0][1])
            self.personalInformation_nameDisplay_lineEdit.setText(data[0][2])
            self.personalInformation_ageDisplay_lineEdit.setText(str(data[0][3]))
            self.personalInformation_guideIdDisplay_lineEdit.setText(data[0][4])
            self.personalInformation_guideIdDisplay_lineEdit.setReadOnly(True)
            self.personalInformation_passwordDisplay_lineEdit.setText(data[0][5])
        cursor.close()
        db.close()

    #viewAnimals_page:
    def viewAnimal_search(self):
        animal_id=self.viewAnimal_animalid_input_lineEdit.text()
        keeper_id=self.viewAnimal_keeperid_input_lineEdit.text()
        home_id=self.viewAnimal_homeid_input_lineEdit.text()
        age=self.viewAnimal_age_input_lineEdit.text()
        gender=self.viewAnimal_gender_input_comboBox.currentText()
        if gender=="unknown":
            gender=""
        name=self.viewAnimal_name_input_lineEdit.text()
        species=self.viewAnimal_species_input_lineEdit.text()
        animal_dict={"animal_id":animal_id,
                     "age":age,
                     "species":species,
                     "home_id":home_id,
                     "animal_name":name,
                     "keeper_id":keeper_id,
                     "gender":gender}
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='20020911Zjl',
                             database='zoo_manage_sysytem',
                             charset='utf8')
        cursor = db.cursor()
        sqlSelect = "select * from pub_animals where "
        tempsqlSelect = sqlSelect
        for i in animal_dict:
            if len(animal_dict[i]) != 0:
                tempstr = i + "='" + animal_dict[i] + "' And "
                sqlSelect = sqlSelect + tempstr
        if tempsqlSelect == sqlSelect:
            sqlSelect = "select * from pub_animals"
        else:
            list_sqlSelect = list(sqlSelect)
            for i in range(-5, 0, 1):
                del (list_sqlSelect[i])
            sqlSelect = ''.join(list_sqlSelect)
        response1 = cursor.execute(sqlSelect)
        if response1 == 0:
            self.viewAnimal_animalDisplay_tableWidget.setRowCount(0)
            QMessageBox.warning(self, "Error", "Error:No Such Data Exists!", QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            self.viewAnimal_animalDisplay_tableWidget.setRowCount(0)
            data = cursor.fetchall()
            for i in range(len(data)):
                row_count = self.viewAnimal_animalDisplay_tableWidget.rowCount()
                self.viewAnimal_animalDisplay_tableWidget.insertRow(row_count)
                for j in range(len(data[i])):
                    self.viewAnimal_animalDisplay_tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))
        cursor.close()
        db.close()