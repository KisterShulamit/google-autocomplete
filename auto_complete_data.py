class AutoCompleteData:
    def __init__(self, complete_sentence: str, source_file: str, offset: int, score=0):

        self.complete_sentence = complete_sentence
        self.source_file = source_file
        self.offset = offset
        self.score = score



