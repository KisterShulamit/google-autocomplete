class DataBase():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not DataBase.__instance:
            DataBase.__instance = object.__new__(cls)
            self = cls.__instance
            self.__dict = {}
        return DataBase.__instance

    @staticmethod
    def get_instance():
        return DataBase.__instance

    def get_data(self):
        return self.__dict

    def get(self, key, default=None):
        return self.__dict.get(key, default)

    def put(self, key, value):
        self.__dict[key] = value
