from PyQt5 import QtCore, QtGui, QtWidgets
import string

class Ui_hesap_makinesi(object):
    def setupUi(self, hesap_makinesi):
        hesap_makinesi.setObjectName("hesap_makinesi")
        hesap_makinesi.resize(361, 588)
        hesap_makinesi.setStyleSheet("""
            QMainWindow {
                background-color: #22252D;
            }
            QLabel {
                background-color: #22252D;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton {
                background-color: #2A2D37;
                color: white;
                border: none;
                border-radius: 37px;
                font-size: 24px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #363B4B;
            }
            QPushButton:pressed {
                background-color: #2A2D37;
            }
            #CButton, #sil_Button, #yuzde_Button {
                background-color: #272B33;
                color: #26F4CE;
            }
            #arti_Button, #eksi_Button, #carpi_Button, #bolme_Button, #esittir_Button {
                background-color: #272B33;
                color: #26F4CE;
            }
            #esittir_Button {
                background-color: #26F4CE;
                color: #22252D;
            }
            #esittir_Button:hover {
                background-color: #1CD6B4;
            }
        """)
        self.centralwidget = QtWidgets.QWidget(hesap_makinesi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.yuzde_Button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda:self.click_button("%"))
        self.yuzde_Button.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.yuzde_Button.setFont(font)
        self.yuzde_Button.setObjectName("yuzde_Button")
        self.CButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("C"))
        self.CButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.CButton.setFont(font)
        self.CButton.setObjectName("CButton")
        self.sil_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.sil_button())
        self.sil_Button.setGeometry(QtCore.QRect(185, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sil_Button.setFont(font)
        self.sil_Button.setObjectName("sil_Button")
        self.bolme_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.hesapla("/"))
        self.bolme_Button.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.bolme_Button.setFont(font)
        self.bolme_Button.setObjectName("bolme_Button")
        self.sekiz_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("8"))
        self.sekiz_Button.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sekiz_Button.setFont(font)
        self.sekiz_Button.setObjectName("sekiz_Button")
        self.dokuz_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("9"))
        self.dokuz_Button.setGeometry(QtCore.QRect(185, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dokuz_Button.setFont(font)
        self.dokuz_Button.setObjectName("dokuz_Button")
        self.carpi_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.hesapla("x"))
        self.carpi_Button.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.carpi_Button.setFont(font)
        self.carpi_Button.setObjectName("carpi_Button")
        self.yedi_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("7"))
        self.yedi_Button.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.yedi_Button.setFont(font)
        self.yedi_Button.setObjectName("yedi_Button")
        self.dort_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("4"))
        self.dort_Button.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dort_Button.setFont(font)
        self.dort_Button.setObjectName("dort_Button")
        self.bes_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("5"))
        self.bes_Button.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.bes_Button.setFont(font)
        self.bes_Button.setObjectName("bes_Button")
        self.alti_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("6"))
        self.alti_Button.setGeometry(QtCore.QRect(185, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.alti_Button.setFont(font)
        self.alti_Button.setObjectName("alti_Button")
        self.eksi_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.hesapla("-"))
        self.eksi_Button.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eksi_Button.setFont(font)
        self.eksi_Button.setObjectName("eksi_Button")
        self.arti_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.hesapla("+"))
        self.arti_Button.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arti_Button.setFont(font)
        self.arti_Button.setObjectName("arti_Button")
        self.uc_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("3"))
        self.uc_Button.setGeometry(QtCore.QRect(185, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.uc_Button.setFont(font)
        self.uc_Button.setObjectName("uc_Button")
        self.iki_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("2"))
        self.iki_Button.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.iki_Button.setFont(font)
        self.iki_Button.setObjectName("iki_Button")
        self.bir_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("1"))
        self.bir_Button.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.bir_Button.setFont(font)
        self.bir_Button.setObjectName("bir_Button")
        self.nokta_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.dot_button())
        self.nokta_Button.setGeometry(QtCore.QRect(185, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nokta_Button.setFont(font)
        self.nokta_Button.setObjectName("nokta_Button")
        self.arti_eksi_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.plus_minus_button())
        self.arti_eksi_Button.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arti_eksi_Button.setFont(font)
        self.arti_eksi_Button.setObjectName("arti_eksi_Button")
        self.sifir_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.click_button("0"))
        self.sifir_Button.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sifir_Button.setFont(font)
        self.sifir_Button.setObjectName("sifir_Button")
        self.esittir_Button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.hesapla("="))
        self.esittir_Button.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.esittir_Button.setFont(font)
        self.esittir_Button.setObjectName("esittir_Button")
        hesap_makinesi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hesap_makinesi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menubar.setObjectName("menubar")
        hesap_makinesi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hesap_makinesi)
        self.statusbar.setObjectName("statusbar")
        hesap_makinesi.setStatusBar(self.statusbar)

        self.retranslateUi(hesap_makinesi)
        QtCore.QMetaObject.connectSlotsByName(hesap_makinesi)


    def sil_button(self):
        """
        Sil butonuna tıklama işlemini yönetir.

        Bu fonksiyon, sil butonuna tıklanıldığında etiketin (label) son karakterini siler.
        Eğer etiket boş kalırsa, "0" olarak ayarlanır.

        Parametreler:
        Yok

        Dönüş:
        Yok: Bu fonksiyon bir değer döndürmez, doğrudan hesap makinesinin ekranını günceller.
        """
        if self.label.text() != "":
            self.label.setText(self.label.text()[:-1])
            if self.label.text() == "":
                self.label.setText("0")
    
    def hesapla(self, button):
        """
        Hesaplama işlemlerini yönetir.

        Bu fonksiyon, "=" butonuna tıklanıldığında mevcut ifadeyi değerlendirir ve sonucu gösterir.
        Ayrıca, operatör butonlarına tıklanıldığında mevcut ifadeyi günceller.

        Parametreler:
        button (str): Tıklanan butonun etiketi veya değeri. Özel değer "=" hesaplama işlemini başlatır.

        Dönüş:
        Yok: Bu fonksiyon bir değer döndürmez, doğrudan hesap makinesinin ekranını günceller.
        """
        if button == "=":
            expression = self.label.text().replace("x", "*")  # Çarpma işareti düzeltme
            try:
                if "%" in expression:
                    # Yüzde işlemini handle et
                    parts = expression.split("%")
                    num = float(parts[0])
                    result = str(num / 100)
                else:
                    # Sıfıra bölme kontrolü
                    result = str(eval(expression))
                    # Sonuç tam sayı ise .0'ı kaldır
                    if result.endswith(".0"):
                        result = result[:-2]
                self.label.setText(result)
            except ZeroDivisionError:
                self.label.setText("Sıfıra bölünemez!")
            except Exception as e:
                self.label.setText("Hata")
        elif button in ["+", "-", "x", "/", "%"]:
            current = self.label.text()
            # Eğer son karakter operatör değilse ve ifade içinde operatör varsa
            if not current[-1] in "+-x/%" and any(op in current for op in "+-x/%"):
                try:
                    # Önce mevcut işlemi yap
                    expression = current.replace("x", "*")
                    if "%" in expression:
                        parts = expression.split("%")
                        num = float(parts[0])
                        result = str(num / 100)
                    else:
                        result = str(eval(expression))
                        # Sonuç tam sayı ise .0'ı kaldır
                        if result.endswith(".0"):
                            result = result[:-2]
                    # Sonra yeni operatörü ekle
                    self.label.setText(result + button)
                except ZeroDivisionError:
                    self.label.setText("Sıfıra bölünemez!")
                except Exception as e:
                    self.label.setText("Hata")
            else:
                # Son karakter operatör ise, yeni operatörle değiştir
                if current[-1] in "+-x/%":
                    self.label.setText(current[:-1] + button)
                else:
                    self.label.setText(current + button)

    def plus_minus_button(self):
        """
        Artı/eksi butonuna tıklama işlemini yönetir.

        Bu fonksiyon, artı/eksi butonuna tıklanıldığında mevcut sayının işaretini değiştirir.

        Parametreler:
        Yok

        Dönüş:
        Yok: Bu fonksiyon bir değer döndürmez, doğrudan hesap makinesinin ekranını günceller.
        """
        current = self.label.text()
        if current != "0" and current != "Hata" and current != "Sıfıra bölünemez!":
            if current[0] == "-":
                self.label.setText(current[1:])
            else:
                self.label.setText(f'-{current}')

    def dot_button(self):
        """
        Nokta butonuna tıklama işlemini yönetir.

        Bu fonksiyon, nokta butonuna tıklanıldığında mevcut sayıya bir ondalık nokta ekler.
        Hata durumlarını kontrol eder ve her sayıya yalnızca bir ondalık nokta eklenmesini sağlar.

        Parametreler:
        Yok

        Dönüş:
        Yok: Bu fonksiyon bir değer döndürmez, doğrudan hesap makinesinin ekranını günceller.
        """
        current = self.label.text()
        if current in ["Hata", "Sıfıra bölünemez!"]:
            return
        # Son operatörden sonraki kısmı al
        parts = current.replace("x", "+").replace("/", "+").replace("-", "+").split("+")
        last_number = parts[-1]
        
        if "." not in last_number and not current[-1] in "+-x/%":
            self.label.setText(current + ".")

    def click_button(self, button):
        """
        Buton tıklamalarını yönetir.

        Bu fonksiyon, hesap makinesindeki buton tıklamalarını işler ve ekranı günceller.
        Ekranı temizleme, hata mesajlarını değiştirme ve yeni rakam veya operatör ekleme işlemlerini yönetir.

        Parametreler:
        button (str): Tıklanan butonun etiketi veya değeri. Özel değer 'C' ekranı temizlemek için kullanılır.

        Dönüş:
        Yok: Bu fonksiyon bir değer döndürmez, doğrudan hesap makinesinin ekranını günceller.
        """
        if button == "C":
            self.label.setText("0")
        else:
            current = self.label.text()
            if current in ["Hata", "Sıfıra bölünemez!"]:
                self.label.setText(button)
            elif self.label.text() == "0":
                self.label.setText(button)
            else:
                self.label.setText(f'{self.label.text()}{button}')

    def retranslateUi(self, hesap_makinesi):
        """
        Kullanıcı arayüzünü yeniden çevirir.

        Bu fonksiyon, kullanıcı arayüzündeki metinleri yeniden çevirir ve günceller.

        Parametreler:
        hesap_makinesi (QMainWindow): Hesap makinesi ana penceresi.

        Dönüş:
        Yok: Bu fonksiyon bir değer döndürmez, doğrudan hesap makinesinin ekranını günceller.
        """
        _translate = QtCore.QCoreApplication.translate
        hesap_makinesi.setWindowTitle(_translate("hesap_makinesi", "Modern Hesap Makinesi"))
        self.label.setText(_translate("hesap_makinesi", "0"))
        self.yuzde_Button.setText(_translate("hesap_makinesi", "%"))
        self.CButton.setText(_translate("hesap_makinesi", "C"))
        self.sil_Button.setText(_translate("hesap_makinesi", "Sil"))
        self.bolme_Button.setText(_translate("hesap_makinesi", "/"))
        self.sekiz_Button.setText(_translate("hesap_makinesi", "8"))
        self.dokuz_Button.setText(_translate("hesap_makinesi", "9"))
        self.carpi_Button.setText(_translate("hesap_makinesi", "x"))
        self.yedi_Button.setText(_translate("hesap_makinesi", "7"))
        self.dort_Button.setText(_translate("hesap_makinesi", "4"))
        self.bes_Button.setText(_translate("hesap_makinesi", "5"))
        self.alti_Button.setText(_translate("hesap_makinesi", "6"))
        self.eksi_Button.setText(_translate("hesap_makinesi", "-"))
        self.arti_Button.setText(_translate("hesap_makinesi", "+"))
        self.uc_Button.setText(_translate("hesap_makinesi", "3"))
        self.iki_Button.setText(_translate("hesap_makinesi", "2"))
        self.bir_Button.setText(_translate("hesap_makinesi", "1"))
        self.nokta_Button.setText(_translate("hesap_makinesi", "."))
        self.arti_eksi_Button.setText(_translate("hesap_makinesi", "+/-"))
        self.sifir_Button.setText(_translate("hesap_makinesi", "0"))
        self.esittir_Button.setText(_translate("hesap_makinesi", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hesap_makinesi = QtWidgets.QMainWindow()
    ui = Ui_hesap_makinesi()
    ui.setupUi(hesap_makinesi)
    hesap_makinesi.show()
    sys.exit(app.exec_())
