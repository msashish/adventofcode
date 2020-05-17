import os
import click
import sys

from typing import Tuple

print('starting fork_new.py with pid: ', os.getpid())
#print(sys.path)
#print(os.getenv('PYTHONPATH'))


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
@click.argument('command', nargs=-1, required=True)
def trigger(command: Tuple[str,...]):
    #print(command)
    #args = ("testarg", "Hahahahaha")
    env = {"PATH": os.environ.get("PATH"), "xyz_env": "some xyz value", "myname_env": "my name is Ashish"}
    #os.execvpe(file=sys.executable, args=command, env=env)
    os.execvpe(file=command[0], args=command, env=env)


if __name__ == '__main__':
    cli()
