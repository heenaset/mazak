import ru # local file,локальный файл
import eng # also a local file, тоже локальный файл
class Mazak:
    def __init__(self):
        self.version = "0.0.3"
    def query(self, text):
        text = text.upper()
        if text.isascii():
            return eng.Query(text)
        else:
            return ru.Query(text)



