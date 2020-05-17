import click


@click.command()   # adding this makes it a command. So upon completion, it exits
@click.option('--count', default=2, help='Count of greeting message')
@click.option('--name', prompt='Enter your name: ', help='Name to be greeted')
def hello(name, count):
    for _ in range(count):
        click.echo(f"Hello Mr {name} ! Welcome")


#@click.command()
def jello(name='Ashish', count=2):
    for _ in range(count):
        print(f"Hello Mr {name} ! Welcome to Jello")


if __name__ == '__main__':
    jello()
    hello() # would not have run if jello was a command :)
