class Contact:
    def __init__(self, name, surname, phone, email):
        self._name = name
        self._surname = surname
        self._phone = phone
        self._email = email

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getPhone(self):
        return self._phone

    def getEmail(self):
        return self._email

    def setName(self, name):
        self._name = name

    def setSurname(self, surname):
        self._surname = surname

    def setPhone(self, phone):
        self._phone = phone

    def setEmail(self, email):
        self._email = email
