import configparser
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent


def save_config_file(data):
    dir_path = PROJECT_DIR
    config_path = f'{dir_path}\\settings.ini'
    config = configparser.ConfigParser()
    config.add_section('SETTINGS')
    config.set('SETTINGS', 'default_port', data['default_port'])
    config.set('SETTINGS', 'address', data['address'])
    config.set('SETTINGS', 'database_name', data['database_name'])
    config.set('SETTINGS', 'database_pass', data['database_pass'])
    config.set('SETTINGS', 'database_user', data['database_user'])
    with open(config_path, 'w') as configfile:
        config.write(configfile)


def load_config():
    dir_path = PROJECT_DIR
    config_path = f'{dir_path}\\settings.ini'
    config = configparser.ConfigParser()
    config.read(config_path)

    if 'SETTINGS' in config:
        return config
    else:
        return False


if __name__ == '__main__':
    load_config()
