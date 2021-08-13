from database.database import DataBase


class WordsDict():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not WordsDict.__instance:
            WordsDict.__instance = object.__new__(cls)
            self = cls.__instance
            data = DataBase()
            data.put("words_dict", {})

            self.__word_data_base = data.get("words_dict")
        return WordsDict.__instance

    def get(self, key, default=None):
        return self.__word_data_base.get(key, default)

    def put(self, key, value):
        if key in self.__word_data_base:
            self.__word_data_base[key].add(value)
        else:
            self.__word_data_base[key] = {value}

    def get_words_database(self):
        return self.__word_data_base
