import sys
import util.parameter_util as parameter_util
import util.file_util as file_util
import parameters

author = "Gabriel Guimarães de Almeida"
institution = "IFMG"
year = 2021


def main():
    # parameter_util.handle_args(sys.argv[1:len(sys.argv) - 1])
    # parameter_util.show_parameters()
    print("\n Simulador de Máquina de Turing ver 1. 0 \n Desenvolvido como trabalho prático para a disciplina de "
          f"Teoria da Computação \n {author}, {institution}, {year}")
    # parameters.first_word = input("\n Forneça a palavra inicial: ") todo descomentar
    parameters.first_word = 'abba'

    # Retrieve the MT from the text file
    # mt = file_util.retrieve_mt_from_file(sys.argv[len(sys.argv) - 1]) todo descomentar
    mt = file_util.retrieve_mt_from_file('/home/gabriel/Documents/projects/python/touring_machine_simulator/examples/example_01.txt')
    # TODO: submit the first word and apply the needed logic
    mt.accept(parameters.first_word)


if __name__ == '__main__':
    main()
