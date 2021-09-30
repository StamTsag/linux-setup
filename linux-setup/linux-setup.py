import subprocess
from importlib.util import find_spec
from json import loads
from os.path import exists
from sys import platform, version_info
from typing import List, Union

import distro

# auto-formatted to .json
required_files: List[str] = ['pkgs']

# ubuntu, fedora, suse, will use when support for more distros is made
distribution_code = -1

def run(cmd: Union[str, List]) -> None:
    """ Convenience function for running commands. """
    # manually convert to list
    subprocess.run(cmd if isinstance(cmd, list) else cmd.split(' '))

def main():
    # exit if not linux
    if platform != 'linux':
        print('Can\'t run on non-linux platform, aborting.')
        exit()

    # not in use till more support comes forth
    if distro.like() in ['ubuntu', 'debian']:
        distribution_code = 'ubuntu'

    else:
        print('Unsupported distribution or live session detected.\nSupported distributions: Ubuntu, Debian')
        exit()

    print(f'Running on {distro.name()} {distro.version()} with Python {version_info.major}.{version_info.minor}')

    # update packages
    print('Updating packages...')
    run('python3 regenerate_files.py')
    print('Packages updated successfully.')

    bloatware = loads(open('pkgs.json', 'r').read())['bloatware'][distribution_code]

    if input(f'Would you like to remove bloatware? [Y/N]: ') in ['Y', 'y', '']:
        print('Removing bloatware apps...')

        for key in loads(open('pkgs.json', 'r').read())['bloatware'][distribution_code]:
            run(f'sudo apt remove {bloatware[key]}')

        print('Bloatware removed.')

    response = ''

    utilities = loads(open('pkgs.json', 'r').read())['utilities']

    while response != 'q':
        available_utilities: List[str] = [f'[{utility[0]}]{utility[1:]}' for utility in utilities]

        response = input(f'Enter each specified letter to install the corresponding app or q to quit {" ".join(map(str, available_utilities))}: ')

        util_found = False

        for i, util in enumerate(available_utilities):
            if response.lower() == util[1].lower():
                util_found = True
                util_name = available_utilities[i].replace('[', '').replace(']', '')

                run(utilities[util_name][distribution_code])
                print(f'Successfully installed {util_name}.')

        if not util_found and response != 'q':
            print('Invalid app specified, please try again.')

if __name__ == '__main__':
    main()
