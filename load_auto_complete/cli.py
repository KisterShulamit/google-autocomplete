from load_auto_complete.read_directory import ReadFiles
from get_best_k_completions.get_best_k_completions import Scores


class CLI:
    def __init__(self):
        self.__get_best_k_completions = Scores().get_best_k_completions

    def do(self, query):

        complete_suggests = self.__get_best_k_completions(query)
        print("You have 5 suggests:")
        for suggest in complete_suggests:
            print(suggest)

    def run(self):
        print("Loading the files and preparing the program....")
        ReadFiles('2021-archive').run()
        print("The program is ready")
        # while True:
        #     query = input("Enter your sentence: ")
        #     complete_suggests = self.__get_best_k_completions(query)

        query = input("Enter your sentence: ")
        temp = ''
        while True:
            if temp + '#' == query:
                query = input("Enter your sentence: ")
            temp = query
            if query[-1] == '#':
                query = query[:-1]
            complete_suggests = self.__get_best_k_completions(query)

            print("You have {} suggests:".format(len(complete_suggests)))
            count = 1
            for suggest in complete_suggests:
                file_name = suggest['file_name'].split('\\')
                print(
                    str(count) + " " + suggest['sentence'].replace("\n", "") + " " + "(" + file_name[-1].partition('.')[
                        0] + " " + str(suggest['line_num']) + ")")
                count += 1

            if temp[-1] != '#':
                query = query + input(query)

            if temp[-1] == '#':
                query = input("Enter your sentence: ")
