import sys
import os
import subprocess

PY_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/python'))
GRAMMAR_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/grammar'))
sys.path.append(PY_DIR)
from yacc_wrapper import roll as dice_tower_roll


def roll(s, mock_random=None):
    target_file = os.path.join(GRAMMAR_DIR, "dice.yacc")

    cmd = "make clean -s"
    cleanup = subprocess.Popen(cmd, shell=True)
    cleanup.wait()

    with open(target_file,'r',encoding='utf-8') as file:
        yacc = file.readlines()

    if mock_random is not None:
        print("MOCKING!")

        replacements = [
            "return rand()%(big+1-small)+small;",
            "return rand()%(length_of_symbolic_array);"
        ]
        if isinstance(mock_random, tuple):
            new_code = ""
            for i, x in enumerate(mock_random):
                new_code += f"""
                    if(random_mock_count == {i}){{
                        random_mock_count++;
                        return {x};
                    }}
                """
        else:
            new_code = f"return {mock_random};"

        for x in range(len(yacc)):
            for r in replacements:
                if r in yacc[x]:
                    yacc[x] = new_code
    else:
        print("NO MOCKING!")

    target_file = os.path.join(GRAMMAR_DIR, "test_dice.yacc")
    with open(target_file,'w+', encoding='utf-8') as test_yacc:
        test_yacc.writelines(yacc)

    print("Target File:", target_file)
    assert(os.path.exists(target_file))

    cmd = "make mock -s"
    parser = subprocess.Popen(cmd, shell=True)
    parser.wait()

    exit_code, result = dice_tower_roll(s)

    if exit_code:
        print("Failing Case stdout:", parser.stdout)
        print("             stderr:", parser.stderr)
        raise ValueError
    return result