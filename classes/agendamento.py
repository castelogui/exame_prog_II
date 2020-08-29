from cliente import Cliente

class Agendamento():
    __slots__ = [
        '_id',
        '_descricao',
        '_data',
        '_hora',
        '_cliente',
        '_status'
    ]
    def __init__(self, id=0, descricao='', data='', hora='', cliente='', status=''):
        self.id = id  
        self.descricao = descricao
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, hora):
        self._hora = hora
        
    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = Cliente.cpf
        
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def print_agendamento(self):
        print('------AGENDAMENTO--------')
        print('id: {}'.format(self.id))
        print('descricao: {}'.format(self.descricao))
        print('Data/Hora: {} - {}'.format(self.data, self.hora))
        print('Cliente: {}, {}'.format(Cliente.cpf, Cliente.nome))
        print('Status: {}'.format(self.status))