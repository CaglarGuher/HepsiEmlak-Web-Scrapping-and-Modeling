from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from catboost import CatBoostRegressor
import category_encoders
import os




script_dir = os.path.dirname(os.path.abspath(__file__))
encoder_path = os.path.join(script_dir, 'category_encoder.pkl')
model_path = os.path.join(script_dir, 'catboost_model.bin')

with open(encoder_path, 'rb') as file:
    encoder =  pd.read_pickle(file)

model = CatBoostRegressor()

model.load_model(model_path)


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Predict")
        Widget.resize(533, 544)
        self.label = QtWidgets.QLabel(Widget)
        
        self.label.setGeometry(QtCore.QRect(35, 10, 500, 50))
        
        font = QtGui.QFont()
        font.setPixelSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.info1 = QtWidgets.QLabel(Widget)
        self.info1.setGeometry(QtCore.QRect(40, 70, 711, 21))
        self.info1.setObjectName("info1")
        self.info3 = QtWidgets.QLabel(Widget)
        self.info3.setGeometry(QtCore.QRect(40, 110, 401, 21))
        self.info3.setObjectName("info3")
        self.test_The_model = QtWidgets.QLabel(Widget)
        self.test_The_model.setGeometry(QtCore.QRect(200, 170, 111, 16))
        font = QtGui.QFont()
        font.setPixelSize(12)
        self.test_The_model.setFont(font)
        self.test_The_model.setObjectName("test_The_model")
        self.district = QtWidgets.QLabel(Widget)
        self.district.setGeometry(QtCore.QRect(20, 200, 49, 31))
        self.district.setObjectName("district")
        self.neigborhood = QtWidgets.QLabel(Widget)
        self.neigborhood.setGeometry(QtCore.QRect(20, 240, 81, 31))
        self.neigborhood.setObjectName("neigborhood")
        self.number_of_room = QtWidgets.QLabel(Widget)
        self.number_of_room.setGeometry(QtCore.QRect(20, 280, 101, 31))
        self.number_of_room.setObjectName("number_of_room")
        self.area = QtWidgets.QLabel(Widget)
        self.area.setGeometry(QtCore.QRect(20, 320, 61, 31))
        self.area.setObjectName("area")
        self.builtding_age = QtWidgets.QLabel(Widget)
        self.builtding_age.setGeometry(QtCore.QRect(20, 360, 81, 31))
        self.builtding_age.setObjectName("builtding_age")
        self.heat_type = QtWidgets.QLabel(Widget)
        self.heat_type.setGeometry(QtCore.QRect(20, 400, 71, 31))
        self.heat_type.setObjectName("heat_type")
        self.distance_to_subway = QtWidgets.QLabel(Widget)
        self.distance_to_subway.setGeometry(QtCore.QRect(250, 360, 141, 31))
        self.distance_to_subway.setObjectName("distance_to_subway")
        self.number_of_floor = QtWidgets.QLabel(Widget)
        self.number_of_floor.setGeometry(QtCore.QRect(250, 200, 101, 31))
        self.number_of_floor.setObjectName("number_of_floor")
        self.number_of_bathroom = QtWidgets.QLabel(Widget)
        self.number_of_bathroom.setGeometry(QtCore.QRect(250, 240, 131, 31))
        self.number_of_bathroom.setObjectName("number_of_bathroom")
        self.distance_of_university_ = QtWidgets.QLabel(Widget)
        self.distance_of_university_.setGeometry(QtCore.QRect(250, 320, 151, 31))
        self.distance_of_university_.setObjectName("distance_of_university_")
        self.distance_to_mall = QtWidgets.QLabel(Widget)
        self.distance_to_mall.setGeometry(QtCore.QRect(250, 400, 121, 31))
        self.distance_to_mall.setObjectName("distance_to_mall")
        self.floor = QtWidgets.QLabel(Widget)
        self.floor.setGeometry(QtCore.QRect(250, 280, 91, 31))
        self.floor.setObjectName("floor")

        self.number_of_room_input = QtWidgets.QSpinBox(Widget)
        self.number_of_room_input.setGeometry(QtCore.QRect(120, 285, 42, 20))
        self.number_of_room_input.setObjectName("number_of_room_input")
        self.district_info = QtWidgets.QComboBox(Widget)

    


        self.district_info.setGeometry(QtCore.QRect(115, 205, 101, 20))
        self.district_info.setObjectName("district_info")
        self.district_info.addItems(["","Altındağ", "Etimesgut", "Gölbaşı", "Keçiören", "Mamak", "Pursaklar", "Sincan", "Yenimahalle", "Çankaya", "Çubuk"])
        self.district_info.setCurrentIndex(-1)
        self.district_info.removeItem(0)

        self.district_info.currentIndexChanged.connect(self.updateNeigComboBox)



        self.neigborhood_input = QtWidgets.QComboBox(Widget)
        self.neigborhood_input.setGeometry(QtCore.QRect(115, 245, 101, 20))
        self.neigborhood_input.setObjectName("neigborhood_input")
        self.neigborhood_input.setCurrentIndex(-1)
        self.neigborhood_input.removeItem(0)


        self.area_input = QtWidgets.QLineEdit(Widget)
        self.area_input.setGeometry(QtCore.QRect(115, 325, 101, 22))
        self.area_input.setObjectName("area_input")
        self.builtding_age_info = QtWidgets.QLineEdit(Widget)
        self.builtding_age_info.setGeometry(QtCore.QRect(115, 365, 41, 22))
        self.builtding_age_info.setObjectName("builtding_age_info")
        self.heat_type_input = QtWidgets.QComboBox(Widget)
        self.heat_type_input.setGeometry(QtCore.QRect(115, 405, 101, 22))
        self.heat_type_input.setObjectName("heat_type_input")



        self.heat_type_input.addItems(["Kombi","Merkezi (Pay Ölçer)","Merkezi","Yerden Isıtma"])
        self.heat_type_input.setCurrentIndex(-1)
        self.heat_type_input.removeItem(0)

        


        self.nubmer_of_floor_input = QtWidgets.QLineEdit(Widget)
        self.nubmer_of_floor_input.setGeometry(QtCore.QRect(410, 205, 100, 22))
        self.nubmer_of_floor_input.setObjectName("nubmer_of_floor_input")
        self.number_of_bathroom_input = QtWidgets.QLineEdit(Widget)
        self.number_of_bathroom_input.setGeometry(QtCore.QRect(410, 245, 100, 22))
        self.number_of_bathroom_input.setObjectName("number_of_bathroom_input")
        self.distance_to_univer_input = QtWidgets.QLineEdit(Widget)
        self.distance_to_univer_input.setGeometry(QtCore.QRect(410, 325, 100, 22))
        self.distance_to_univer_input.setObjectName("distance_to_univer_input")
        self.distance_to_subway_input = QtWidgets.QLineEdit(Widget)
        self.distance_to_subway_input.setGeometry(QtCore.QRect(410, 365, 100, 22))
        self.distance_to_subway_input.setObjectName("distance_to_subway_input")
        self.distance_to_mall_input = QtWidgets.QLineEdit(Widget)
        self.distance_to_mall_input.setGeometry(QtCore.QRect(410, 405, 100, 22))
        self.distance_to_mall_input.setObjectName("distance_to_mall_input")
        self.floor_input = QtWidgets.QComboBox(Widget)
        self.floor_input.setGeometry(QtCore.QRect(410, 285, 100, 21))
        self.floor_input.setObjectName("floor_input")

        self.floor_input.addItems(["1. Kat",
                           "3. Kat",
                           "2. Kat",
                           "Yüksek Giriş",
                           "4. Kat",
                           "Ara Kat",
                           "Kot 1",
                           "En Üst Kat",
                           "Giriş Katı",
                           "5. Kat",
                           "6. Kat",
                           "Bahçe Katı",
                           "8. Kat",
                           "Kot 2",
                           "7. Kat",
                           "10. Kat",
                           "9. Kat",
                           "Teras Katı",
                           "11. Kat",
                           "12. Kat",
                           "13. Kat",
                           "14. Kat",
                           "15. Kat",
                           "Zemin"])
        self.floor_input.setCurrentIndex(-1)
        self.floor_input.removeItem(0)

        
        self.predict_the_price = QtWidgets.QPushButton(Widget)
        self.predict_the_price.setGeometry(QtCore.QRect(200, 450, 101, 24))
        self.predict_the_price.setObjectName("predict_the_price")
        self.price_output = QtWidgets.QLabel(Widget)
        self.price_output.setGeometry(QtCore.QRect(200, 480, 151, 28))
        self.price_output.setText("")
        self.price_output.setObjectName("price_output")

        self.predict_the_price.clicked.connect(self.predict_the_model)

        self.info2 = QtWidgets.QLabel(Widget)
        self.info2.setGeometry(QtCore.QRect(35, 90, 711, 21))
        self.info2.setObjectName("info2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)


    def updateNeigComboBox(self):
         
        country = self.district_info.currentText()
        self.neigborhood_input.clear()

        # Clear the city ComboBox
        
        # Add new options based on the selected country
        if country == "Çankaya":

            self.neigborhood_input.addItems(["Harbiye", "İlkadım", "Alacaatlı", "Kırkkonaklar", "Yukarı Bahçelievler",
                            "İlkbahar", "Huzur", "Emek", "Birlik", "Keklik Pınarı", "Bahçelievler",
                            "Akpınar", "Naci Çakır", "Sokullu Mehmet Paşa", "Şehit Cengiz Karaca",
                            "Karapınar", "Ata", "Ayrancı", "Mürsel Uluç", "Osman Temiz", "Beytepe",
                            "Aziziye", "Büyükesat", "Şehit Cevdet Özdemir", "Hilal", "Öveçler",
                            "Aydınlar", "Aşağı Öveçler", "Aşıkpaşa", "Seyranbağları", "Yukarı Dikmen",
                            "Cevizlidere", "Maltepe", "Gökkuşağı", "Yaşamkent", "Oran", "Yıldızevler",
                            "Malazgirt", "Kavaklıdere", "Güvenevler", "Bağcılar", "Tınaztepe", "Sancak",
                            "Mutlukent", "Metin Oktay", "Gaziosmanpaşa"])
            
        elif country == "Altındağ":
        

            self.neigborhood_input.addItems(["Karapürçek", "Aydınlıkevler", "Beşikkaya", "Örnek", "Güneşevler","Feridun Çelik","Başpınar"])

        elif country == "Etimesgut":
            self.neigborhood_input.addItems(["Bağlıca",
                                "Topçu",
                                "Piyade",
                                "Yeni Bağlıca",
                                "Süvari",
                                "İstasyon",
                                "Ahi Mesut",
                                "Alsancak",
                                "Elvan",
                                "Yeşilova",
                                "Şehit Osman Avcı",
                                "Göksu",
                                "Şeker"])
            
        elif country == "Gölbaşı":
            self.neigborhood_input.addItems(["İncek",
                                "Kızılcaşar",
                                "Taşpınar",
                                "Karşıyaka",
                                "Bahçelievler",
                                "Seğmenler",
                                "Hacılar"])
        elif country == "Keçiören":
            self.neigborhood_input.addItems(["Etlik",
                                "Ayvalı",
                                "Ovacık",
                                "Atapark",
                                "İncirli",
                                "Yayla",
                                "Yükseltepe",
                                "Karakaya",
                                "Esertepe",
                                "Aşağı Eğlence",
                                "Kanuni",
                                "Şehit Kubilay",
                                "Sancaktepe",
                                "Bağlarbaşı",
                                "Bademlik",
                                "Uyanış",
                                "Kuşcağız",
                                "Tepebaşı",
                                "Adnan Menderes",
                                "Hisar"])
            
        elif country =="Mamak":
            self.neigborhood_input.addItems(["Durali Alıç",
                                "General Zeki Doğan",
                                "Şahintepe",
                                "Mutlu",
                                "Fahri Korutürk",
                                "Cengizhan",
                                "Akşemsettin",
                                "Türközü",
                                "Kutlu",
                                "Ege",
                                "Tuzluçayır",
                                "Misket",
                                "Bahçelerüstü",
                                "Demirlibahçe",
                                "Başak",
                                "Hürel",
                                "Şirintepe",
                                "Şafaktepe",
                                "Peyami Safa",
                                "Aşık Veysel",
                                "Kazım Orbay"])
        elif country == "Pursaklar":
            self.neigborhood_input.addItems(["Merkez",
                                "Mimar Sinan",
                                "Fatih",
                                "Yunus Emre",
                                "Saray Fatih",
                                "Tevfik İleri"])
        elif country == "Sincan":
            self.neigborhood_input.addItems(["Mustafa Kemal",
                                "Mareşal Çakmak",
                                "Akşemsettin",
                                "Tandoğan",
                                "Fevzi Çakmak",
                                "Menderes",
                                "Plevne",
                                "29 Ekim",
                                "Malazgirt",
                                "Atatürk",
                                "Pınarbaşı",
                                "Selçuklu",
                                "İstasyon"])
        elif country == 'Yenimahalle':
            self.neigborhood_input.addItems(["Turgut Özal",
                                "Pamuklar",
                                "Yeni Batı",
                                "Kentkoop",
                                "Yunus Emre",
                                "Işınlar",
                                "Emniyet",
                                "Gazi",
                                "Demetevler",
                                "Mehmet Akif Ersoy",
                                "Çiğdemtepe",
                                "Ata"])
        elif country =="Çubuk":
            self.neigborhood_input.addItems(["Esenboğa Merkez"])


            
    def predict_the_model(self):

        data = pd.DataFrame({
        'District': [self.district_info.currentText()],
        'Neighborhood': [self.neigborhood_input.currentText()],
        'Num_Of_Room': [float(self.number_of_room_input.value())],
        'Area': [float(self.area_input.text())],
        'Age': [float(self.builtding_age_info.text())],
        'Heat_type': [self.heat_type_input.currentText()],
        'Apt_Floor': [float(self.nubmer_of_floor_input.text())],
        'Banyo Sayısı': [float(self.number_of_bathroom_input.text())],
        'Metro_Station': [float(self.distance_to_subway_input.text())],
        'University': [float(self.distance_to_univer_input.text())],
        'Shopping_Mall': [float(self.distance_to_mall_input.text())],
        'Floor': [self.floor_input.currentText()]
    })
        
        encoded_data = encoder.transform(data)
        predictions = model.predict(encoded_data)[0]
        predictions = (predictions // 1000) * 1000
        self.price_output.setText(f"Expected price :{str(predictions)}")

    
    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Predict", "Predict"))
        self.label.setText(_translate("Widget", "HOUSE PREDICTION IN ANKARA"))
        self.info1.setText(_translate("Widget", "Model is built with decision tree.That means any unrealistic or extreme input will not"))
        self.info3.setText(_translate("Widget", "Model is built with more than 19000 house information."))
        self.test_The_model.setText(_translate("Widget", "TEST THE MODEL"))
        self.district.setText(_translate("Widget", "District :"))
        self.neigborhood.setText(_translate("Widget", "Neigborhood :"))
        self.number_of_room.setText(_translate("Widget", "Number of room :"))
        self.area.setText(_translate("Widget", "Area (m2) :"))
        self.builtding_age.setText(_translate("Widget", "Building age :"))
        self.heat_type.setText(_translate("Widget", "Heat Type :"))
        self.distance_to_subway.setText(_translate("Widget", "Distance to Subway (km) :"))
        self.number_of_floor.setText(_translate("Widget", "Number of Floors :"))
        self.number_of_bathroom.setText(_translate("Widget", "Number of Bathroom :"))
        self.distance_of_university_.setText(_translate("Widget", "Distance to University (km) :"))
        self.distance_to_mall.setText(_translate("Widget", "Distance to Mall(km) :"))
        self.floor.setText(_translate("Widget", "Floor :"))
        
        self.predict_the_price.setText(_translate("Widget", "Predict the price"))
        self.info2.setText(_translate("Widget", " give a good results."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    stylesheet = """
        QWidget#centralwidget {
            background-color: #f0f0f0;
        }
        
        QLabel#title_label {
            color: #333333;
        }
        
        QLabel#info1,
        QLabel#info2,
        QLabel#info3,
        QLabel#info4,
        QLabel#district_label,
        QLabel#neighborhood_label,
        QLabel#number_of_rooms_label,
        QLabel#area_label,
        QLabel#building_age_label,
        QLabel#result_label,
        QLabel#price_label {
            color: #555555;
        }
        
        QPushButton#data_info_button,
        QPushButton#predict_button {
            background-color: #007BFF;
            color: #FFFFFF;
            border: 1px solid #007BFF;
            border-radius: 5px;
            padding: 5px;
        }
        
        QPushButton#data_info_button:hover,
        QPushButton#predict_button:hover {
            background-color: #0056b3;
            border: 1px solid #0056b3;
        }
        
        QLineEdit#district_input,
        QLineEdit#neighborhood_input,
        QSpinBox#number_of_rooms_input,
        QSpinBox#area_input,
        QSpinBox#building_age_input {
            background-color: #FFFFFF;
            border: 1px solid #CCCCCC;
            border-radius: 5px;
            padding: 5px;
        }
        
        """
    Widget.setStyleSheet(stylesheet)
    Widget.show()
    sys.exit(app.exec_())
