import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QRadioButton, QComboBox

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("User Registration Form")
        self.setGeometry(200, 200, 500, 500)
        
        layout = QVBoxLayout()
        
        identitas = QGroupBox("Identitas")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama: Muh. Ressa Arsy Ma'rif"))
        identitas_layout.addWidget(QLabel("NIM: F1D022137"))
        identitas_layout.addWidget(QLabel("Kelas: C"))
        identitas.setLayout(identitas_layout)
        layout.addWidget(identitas)
        
        nav_group = QGroupBox("Navigation")
        nav_layout = QHBoxLayout()
        home_btn = QPushButton("Home")
        about_btn = QPushButton("About")
        contact_btn = QPushButton("Contact")
        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(about_btn)
        nav_layout.addWidget(contact_btn)
        nav_group.setLayout(nav_layout)
        layout.addWidget(nav_group)
        
        form_group = QGroupBox("User Registration")
        form_layout = QFormLayout()
        
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()
        
        form_layout.addRow("Full Name:", self.name_input)
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Phone:", self.phone_input)
        
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        form_layout.addRow("Gender:", gender_layout)
        
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select", "Amerika", "Belanda", "Indonesia", "Zimbabwe"])
        form_layout.addRow("Country:", self.country_combo)
        
        form_group.setLayout(form_layout)
        layout.addWidget(form_group)
        
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        action_layout.addWidget(submit_btn)
        action_layout.addWidget(cancel_btn)
        action_group.setLayout(action_layout)
        layout.addWidget(action_group)
        
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.show()
    sys.exit(app.exec_())
