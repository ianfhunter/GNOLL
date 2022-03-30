import sys
import os
import subprocess
import importlib
import importlib.util as iu

GRAMMAR_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/grammar'))
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src/python/dicetower/'))
MK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

def get_roll():

    # We are explicitly using the local module here as we modify the yacc in order to mock our tests.
    # This ugly logic is to bypass the fact that you might have the pip package installed
    # and thus a name conflict
    m = os.path.join(SRC_DIR, "parser.py")
    spec = iu.spec_from_file_location("dt", m)
    dt = iu.module_from_spec(spec)
    spec.loader.exec_module(dt)
    dice_tower_roll = dt.roll
    return dice_tower_roll


def roll(s, mock_random=None):



    target_file = os.path.join(GRAMMAR_DIR, "dice.yacc")

    cmd = "make clean -s -C " + MK_DIR
    cleanup = subprocess.Popen(cmd, shell=True)
    cleanup.communicate()
    if cleanup.returncode:
        raise ValueError


    with open(target_file,'r',encoding='utf-8') as file:
        yacc = file.readlines()

    if mock_random is not None:
        # print("MOCKING!")

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
                        printf("Mocking! %d: \\n", {x});
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
        # print("NO MOCKING!")
        pass

    target_file = os.path.join(GRAMMAR_DIR, "test_dice.yacc")
    with open(target_file,'w+', encoding='utf-8') as test_yacc:
        test_yacc.writelines(yacc)

    print("Target File:", target_file)
    assert(os.path.exists(target_file))

    cmd = "make mock -s -C " + MK_DIR
    parser = subprocess.Popen(cmd, shell=True)
    parser.communicate()
    if parser.returncode:
        raise ValueError


    # Get module now - post make
    dice_tower_roll = get_roll()
    exit_code, result = dice_tower_roll(s)

    if exit_code:
        print("Failing Case stdout:", parser.stdout)
        print("             stderr:", parser.stderr)
        raise ValueError
    return result