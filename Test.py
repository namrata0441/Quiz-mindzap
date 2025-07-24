from question.Question import QuestionCollection
import pickle
import random


class TestCollection:
    """A wrapper around a dictionary of Tests"""

    def __init__(self):
        self.__tests = {}

    def add(self, test):
        if not test in self.__tests.values():
            self.__tests[test.ident] = test
            return True
        return False

    def __len__(self):
        return len(self.__tests)

    def getTests(self):
        return self.__tests


class TestBank(TestCollection):
    """Singleton to create ONE list of tests"""
    __instance = None

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            try:
                # try and load from filesystem
                with open('data/testBank.txt', 'rb') as qb:
                    cls.__instance = pickle.load(qb)
            except Exception:
                # new up a test bank
                cls.__instance = TestBank()
        return cls.__instance

    def save(self):
        # pickle and save to filesystem
        with open('data/testBank.txt', 'wb') as qb:
            pickle.dump(self.__instance, qb, pickle.HIGHEST_PROTOCOL)


class Test(QuestionCollection):
    __identifiers = []
    __name = ''
    __currentDate = None
    __currentClass = None
    __results = None
    __runBy = None
    __history = None

    def __init__(self, ident=''):
        super().__init__()

        if ident:
            self.__ident = ident
        else:
            ident = random.randint(1000, 9999)
            while ident in type(self).__identifiers:
                ident = random.randint(1000, 9999)
            type(self).__identifiers += [ident]
            self.__ident = "test" + str(ident)

    @property
    def ident(self):
        return self.__ident

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getCurrentDate(self):
        return self.__currentDate

    def setCurrentDate(self, value):
        self.__currentDate = value

    def getCurrentClass(self, ):
        return self.__currentClass

    def setCurrentClass(self, value):
        self.__currentClass = value

    def getResults(self):
        return self.__results

    def setResults(self, value):
        self.__results = value

    def getRunBy(self):
        return self.__runBy

    def setRunBy(self, value):
        self.__runBy = value

    def getHistory(self):
        return self.__history

    def setHistory(self, value):
        self.__history = value


class TestHistory:
    def __init__(self):
        self.usedBy = None
        self.previousResults = None

