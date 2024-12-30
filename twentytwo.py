class PhoneFactory:
    model: None
    color: None
    is_android: None
    def _int_(self, model, color, is_android):
        self.model = model
        self.color = color
        self.is_android = is_android
        print("Phone created")
    def _str_(self):
        return f"{self.model} - {self.color}"
    def check_os(self):
        if self.is_android:
            print("Android")
        else:
            print("iOS")

oppo_phone_1 = PhoneFactory("A53", "black", True)
print(oppo_phone_1)            