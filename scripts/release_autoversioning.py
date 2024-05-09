import configparser

def update_version(path, find, replace):
    with open(path, 'r') as f:
        # Get every line
        lines = f.readlines()
        
    with open(path, 'w', encoding='utf_8') as f:
        for line in lines:
            if find in line: 
                f.write(replace)
            else:
                f.write(line)


def update_version_in_files(gnoll_ini_path, setup_cfg_path, project_toml_path):
    # Read version from GNOLL.ini
    config = configparser.ConfigParser()
    config.read(gnoll_ini_path)
    version = config['Meta Information']['version']

    update_version(setup_cfg_path, 'version =',  f'version = "{version}"\n')
    update_version(project_toml_path, 'version =',  f'version = "{version}"\n')
    update_version("src/grammar/dice.yacc", 'printf("GNOLL', f'printf("GNOLL {version}")\n')
    
    
gnoll_ini_path = 'GNOLL.ini'
setup_cfg_path = 'src/python/setup.cfg'
project_toml_path = 'GNOLL/src/julia/GNOLL/Project.toml'
update_version_in_files(gnoll_ini_path, setup_cfg_path, project_toml_path)
