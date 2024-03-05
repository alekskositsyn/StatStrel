import configparser
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent


def config_load():
    dir_path = PROJECT_DIR
    config_path = f'{dir_path}\\settings.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    if 'SETTINGS' in config:
        return config
    else:
        config.add_section('SETTINGS')
        config.set('SETTINGS', 'default_port', '')
        config.set('SETTINGS', 'listen_address', '')
        config.set('SETTINGS', 'database_name', '')
        config.set('SETTINGS', 'database_pass', '')
        config.set('SETTINGS', 'database_user', '')
        with open(config_path, 'w') as configfile:
            config.write(configfile)



if __name__ == '__main__':
    config_load()
