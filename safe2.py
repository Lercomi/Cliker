import shelve as sh


class SaveScore:
    SCORE_KEY = 'score-key'
    STEP_KEY = 'buff1-key'

    def __init__(self):
        self.file = sh.open('.data/clicker_score')

    def save_score(self, score):
        self.file[self.SCORE_KEY] = score
        self.file['Number'] = 52

    def get_score(self):
        #num = self.file['Number']
        #print(num)
        if self.SCORE_KEY not in self.file:
            return 0
        print(self.file[self.SCORE_KEY])
        return self.file[self.SCORE_KEY]

    def save_step(self, buff1):
        self.file[self.STEP_KEY] = buff1

    def get_step(self):
        if self.STEP_KEY not in self.file:
            return 1
        print(self.file[self.STEP_KEY])
        return self.file[self.STEP_KEY]

    def __del__(self):
        self.file.close()














