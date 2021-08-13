from database.auto_complete_database import AutoCompleteDatabase
import os


class ReadFiles():
    def __init__(self, directory_path):
        self.__directory_path = directory_path
        self.__database = AutoCompleteDatabase()

    def run(self):
        for root, dirs, files in os.walk(self.__directory_path):
            for file in files:
                self.read_from_file(os.path.join(root, file))

    def clean_word(self, word):
        ''.join(e for e in word if e.isalnum())

    def read_from_file(self, file_name):
        index_line = 1
        with open(file_name, encoding="utf8") as f:
            lines = f.readlines()
        for line in lines:
            index = self.__database.insert_sentence(line, file_name, index_line)
            for word in line.split():
                self.__database.insert_word(word.lower(), index)
