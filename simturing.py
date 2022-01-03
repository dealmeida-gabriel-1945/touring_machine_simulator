import sys
import util.parameter_util as parameter_util
import util.file_util as file_util
import parameters

author = "Gabriel Guimarães de Almeida"
institution = "IFMG"
year = 2021


def main():
    debug = 1

    if debug:
        parameters.last_new_instructions = ['-r', '-s', '40000']
        parameter_util.handle_args(parameters.last_new_instructions)
        print("\n Simulador de Máquina de Turing ver 1. 0 \n Desenvolvido como trabalho prático para a disciplina de "
              f"Teoria da Computação \n {author}, {institution}, {year}")
        parameters.first_word = f'1000+10000000009000='
        print(parameters.first_word)
        mt = file_util.retrieve_mt_from_file('/home/gabriel/Documents/projects/python/touring_machine_simulator/examples/example_02.txt')
        mt.accept(parameters.first_word)
        if parameters.run_resume:
            print(f'Conteúdo final na fita: {mt.get_final_tape_content()}')
    else:
        parameters.last_new_instructions = sys.argv[1:len(sys.argv)]
        parameter_util.handle_args(parameters.last_new_instructions)
        print("\n Simulador de Máquina de Turing ver 1. 0 \n Desenvolvido como trabalho prático para a disciplina de "
              f"Teoria da Computação \n {author}, {institution}, {year}")
        parameters.first_word = input("\n Forneça a palavra inicial: ")

        # Retrieve the MT from the text file
        mt = file_util.retrieve_mt_from_file(sys.argv[1])
        mt.accept(parameters.first_word)
        if parameters.run_resume:
            print(f'Conteúdo final na fita: {mt.get_final_tape_content()}')


if __name__ == '__main__':
    main()
