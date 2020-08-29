class Cliente():
    
    __slots__ = [
        '_cpf',
        '_nome',
        '_telefone',
        '_endereco',
        '_renda'
    ]

    def __init__(self, cpf='', nome='', telefone=0, endereco='', renda=''):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.renda = renda

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def renda(self):
        return self._renda

    @renda.setter
    def renda(self, renda):
        self._renda = renda