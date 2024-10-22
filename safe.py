import shelve

from Кликер import score


class Save:
    def __init__(self):
        self.file = shelve.open('data')
        self.info = {
            score
        }

    def save_data(self):
        self.file[score] = score
        self.file['Number'] = 52

    def get_data(self, score):
        num = self.file['Number']
        print(num)
        print(self.file[score])

    def __del__(self):
        self.file.close()














