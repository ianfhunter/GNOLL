import configparser

def update_version_in_setup_cfg(gnoll_ini_path, setup_cfg_path):
    # Read version from GNOLL.ini
    config = configparser.ConfigParser()
    config.read(gnoll_ini_path)
    version = config['Meta Information']['version']

    # Update version in setup.cfg
    with open(setup_cfg_path, 'r') as f:
        lines = f.readlines()

    with open(setup_cfg_path, 'w') as f:
        for line in lines:
            if line.startswith('version ='):
                f.write(f'version = {version}\n')
            else:
                f.write(line)

gnoll_ini_path = 'GNOLL.ini'
setup_cfg_path = 'src/python/setup.cfg'
update_version_in_setup_cfg(gnoll_ini_path, setup_cfg_path)
