import click

@click.group()
def cli():
    pass


@cli.command()
@click.option('--count', default=2, help='Count of greeting message')
@click.option('--name', default='Ashish', help='Name to be greeted')
def hello(count, name):
    for _ in range(count):
        click.echo(f"Hello Mr {name} ! Welcome by hello")


@cli.command()
def jello(name='Ashish', count=2):
    for _ in range(count):
        print(f"Hello Mr {name} ! Welcome to Jello")


if __name__ == '__main__':
    cli()
