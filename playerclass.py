
class Contender:
    def __init__(self, name, categoryList):
        self.name = name
        self.score = 0
        self.categories = categoryList
        self.categoryNumbers = {category: index for index, category in enumerate(categoryList)}
        self.table = [[category] for category in categoryList]

    def answer(self, category, response):
        indexNumber = 1
        while True:
            try:
                getattr(self, f'{category}_{indexNumber}')
                indexNumber += 1
            except AttributeError:
                break
        setattr(self, f'{category}_{indexNumber}', response)
        self.table[self.categoryNumbers[category]].append(response)

    def remove_answer(self, category, tour):
        delattr(self, f'{category}_{tour}')
        del self.table[self.categoryNumbers[category]][tour]

    def score_response(self, category, response, score):
        setattr(self, f'{category}_{response}', score)
