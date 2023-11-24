class NfValidation:

    _erros = []

    def __init__(self):

        self.validate(self)

    def validate(self):

        if True:
            self._erros.append('SEFAZ nao funcionou')

    def get_erros(self):

        return self._erros