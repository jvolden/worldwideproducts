"""Console script for world_wide_products_inc."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for world_wide_products_inc."""
    click.echo("Replace this message by putting your code into "
               "world_wide_products_inc.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
