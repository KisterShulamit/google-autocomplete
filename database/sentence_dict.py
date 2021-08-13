from database.database import DataBase


class SentenceDict():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SentenceDict.__instance:
            SentenceDict.__instance = object.__new__(cls)
            self = cls.__instance
            data = DataBase()
            data.put("sentence_dict", [])
            self.__sentences_database = data.get("sentence_dict")
        return SentenceDict.__instance

    def get_sentences_database(self):
        return self.__sentences_database

    def put(self, value):
        self.__sentences_database.append(value)

    def __len__(self):
        return len(self.__sentences_database)

    def get(self, index):
        return self.__sentences_database[index]
