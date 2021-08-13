from database.auto_complete_database import AutoCompleteDatabase

import re

from get_best_k_completions.menipulation import Menipulation


class Scores:
    def __init__(self):
        self.__database = AutoCompleteDatabase()
        self.__scores = {}
        self.__sen_content = {}
        self.__regex = re.compile('[^a-zA-Z0-9]')

    def clean_sentence(self, sen):
        return self.__regex.sub('', sen).lower()

    def get_clean_sentence(self, sen_id):
        return self.clean_sentence(self.__database.get_sen(sen_id)['sentence'])

    @staticmethod
    def insert_efficient_score(sentence, index, new_score, word_scores, word_indexes):
        if sentence not in word_scores:
            word_scores[sentence] = new_score
            word_indexes[sentence] = index
        else:
            if new_score > word_scores[sentence]:
                word_scores[sentence] = new_score
                word_indexes[sentence] = index

    def manipulation_word_scores(self, manipulation, manipulation_score, word_scores, word_indexes):
        sens_contain_manipulation = self.__database.get_word(manipulation.lower())
        for sen_contain_manipulation in sens_contain_manipulation:
            self.insert_efficient_score(sen_contain_manipulation, manipulation, manipulation_score, word_scores,
                                        word_indexes)

    def manipulations_word_scores(self, word, word_scores={}, word_indexes={}):
        word_manipulation = Menipulation().menipulation(word)
        for man_word, score in word_manipulation.items():
            self.manipulation_word_scores(man_word, score, word_scores, word_indexes)
        return word_scores, word_indexes

    def get_best_k_completions(self, query: str):
        self.__scores = {}
        self.__sen_content = {}
        query_words = query.split()
        query_length = len(query_words)
        for i in range(len(query_words)):
            word = query_words[i]
            word_scores, word_indexes = self.manipulations_word_scores(word, {}, {})
            for sen_contain_word_man, contain_word_man_score in word_scores.items():
                if sen_contain_word_man in self.__scores:
                    self.__scores[sen_contain_word_man] += contain_word_man_score
                    self.__sen_content[sen_contain_word_man].append(word_indexes[sen_contain_word_man])
                else:
                    self.__scores[sen_contain_word_man] = contain_word_man_score
                    self.__sen_content[sen_contain_word_man] = [word_indexes[sen_contain_word_man]]
                if i == query_length and len(self.__sen_content[sen_contain_word_man]) == len(query_words):
                    cleaned_query = self.clean_sentence(query)
                    cleaned_sentence = self.get_clean_sentence(sen_contain_word_man)
                    if cleaned_query in cleaned_sentence:
                        self.__scores[sen_contain_word_man] += 2 * len(query)
        return [self.__database.get_sen(item) for item in
                sorted(self.__scores, key=self.__scores.get, reverse=True)[:5]]
