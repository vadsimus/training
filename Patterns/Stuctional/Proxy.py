class Databse:
    def get_result(self, parameter):
        pass


class RealDatabase(Databse):
    def get_result(self, parameter):
        return f'calculated result from db{parameter}'


class ProxyDtabase(Databse):
    _cashe = {}

    def get_result(self, parameter):
        if parameter in self._cashe:
            return f'Cashed: {self._cashe[parameter]}'
        else:
            result = RealDatabase().get_result(parameter)
            self._cashe.update({parameter: result})
            return result


pdb = ProxyDtabase()
print(pdb.get_result(1))
print(pdb.get_result(2))
print(pdb.get_result(3))
print(pdb.get_result(1))
print(pdb.get_result(1))
