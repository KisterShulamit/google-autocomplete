from database.sentence_dict import SentenceDict
from database.words_dict import WordsDict


class AutoCompleteDatabase(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not AutoCompleteDatabase.__instance:
            AutoCompleteDatabase.__instance = object.__new__(cls)
            self = cls.__instance
            self.__word_dict = WordsDict()
            self.__sentence_database = SentenceDict()
        return AutoCompleteDatabase.__instance

    def insert_word(self, word, sen_index):
        self.__word_dict.put(word, sen_index)

    def insert_sentence(self, sentence, file_name, line_num):
        self.__sentence_database.put({"sentence":sentence,"file_name": file_name, "line_num": line_num})
        return len(self.__sentence_database)-1

    def get_word(self, word):
        return self.__word_dict.get(word,{})

    def get_sen(self, index):
        return self.__sentence_database.get(index)