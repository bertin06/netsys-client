import sys
from gateway import Gateway

def main():

    gateway = Gateway()

    try:

        args = sys.argv[1].split('?')[1].split('&')

        arg_dict = {}
            
        for arg in args:

            parametros = arg.split('=')

            arg_dict[parametros[0]] = parametros[1]

        if arg_dict['class'] == 'conf':

            gateway.change_config(arg_dict)

        if arg_dict['class'] == 'getprinters':

            gateway.search_printers()

    except:

        gateway.set_erro('URL incorreta!')

if __name__ == '__main__':
    main()