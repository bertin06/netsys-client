from validation import NfValidation
from methods import NfMethods

class NfController:

    _erros = []

    def __init__(self):

        self.execute()

    def execute(self):

        validation = NfValidation()

        if validation.get_erros():

            self._erros = validation.get_erros()

        else:

            methods = NfMethods()
            methods.metodo1()
            methods.metodo2()