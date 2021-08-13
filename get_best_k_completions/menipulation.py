import string

class Menipulation:


    def __init__(self):
        self.mani_word = {}


    def menipulation(self,word):

        # append complete word
        self.mani_word[word] = len(word)*2

        # delete char
        for i in range(len(word)):
            # delete char---------------------------
            # element over 4 character
            if i >= 4:
                score = len(word)*2 - 2
            else:
                score = len(word) * 2 - (10- i*2)
            if score > 0:
                self.mani_word[word[:i] + word[i+1:]] = score

            for char in string.ascii_lowercase:
                # change char------------------------
                temp = list(word)
                temp[i] = char
                temp = "".join(temp)

                # elements over 5 character
                if i >= 5:
                    score = len(word) * 2 - 1
                else:
                    score =len(word) * 2 - (i + 1)
                if score > 0:
                    if temp != word:
                        self.mani_word[temp] = score

                # add char ---------------------------
                # element over 4 character
                if i >= 4:
                    score = len(word) * 2 - 2
                else:
                    score = len(word) * 2 - (10 - i * 2)
                if score > 0:
                    self.mani_word[word[:i] + char + word[i:]] = score

        return self.mani_word


