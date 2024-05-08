# cleaner.py
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class CleanerMlUtilMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CleanerMlUtil(metaclass=CleanerMlUtilMeta):
    def __init__(self):
        nltk.download("stopwords")
        nltk.download("punkt")
        nltk.download("wordnet")
        # inicializo el lematizador y stopwords en espanol
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords_ = set(stopwords.words("spanish"))

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        # ...
    def print_text(self, sample, clean):
        print(f"Before: {sample}")
        print(f"After: {clean}")

    def clean_words(self, sample_text):
        #convertir a minusculas
        sample_text = sample_text.lower()
        #eliminar texto entre corchetes, caracteres especiales, y digitos
        sample_text = re.sub(r'\[.*?\]', '', sample_text)
        sample_text = re.sub(r'[^a-zA-Z\s]', '', sample_text)
        sample_text = re.sub(r'\d+', '', sample_text)

        #tokenizar el texto
        #tokens = sample_text.split()
        tokens = nltk.word_tokenize(sample_text)

        words = [self.lemmatizer.lemmatize(t) for t in tokens if t not in self.stopwords_]
        cleaned_text = " ".join(words)
        #self.print_text(sample_text, cleaned_text)
        return cleaned_text




    #limpieza de texto conversacion whatsapp
    def remove_chat_metadata(self, chat_export_file):
        date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "9/16/22, 06:34"
        dash_whitespace = r"\s-\s"  # " - "
        username = r"([\w\s]+)"  # e.g. "Martin"
        metadata_end = r":\s"  # ": "
        pattern = date_time + dash_whitespace + username + metadata_end

        with open(chat_export_file, "r") as corpus_file:
            content = corpus_file.read()
        cleaned_corpus = re.sub(pattern, "", content)
        return tuple(cleaned_corpus.split("\n"))




if __name__ == "__main__":
    #print(remove_chat_metadata("chat.txt"))
    s1 = CleanerMlUtil()
    s1.clean_words("Hola mundo en esta prueba :)")





