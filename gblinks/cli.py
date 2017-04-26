# -*- coding: utf-8 -*-

import click
import json
import sys

from gblinks import Gblinks

def check_broken_links(gblinks, verbose):
    broken_links = gblinks.check_broken_links()

    if broken_links:
        if verbose:
            print_links(broken_links)

        click.echo(
            click.style(
                '%d broken links found in the given path' % len(broken_links)
                , fg='red'
            )
        )

        sys.exit(-2)
    else:
        click.echo('No broken links found in the given path')

def list_links(gblinks):
    links = gblinks.get_links()
    print_links(links)
    click.echo('%d links found in the given path' % len(links))

def print_links(links):
    for link in links:
        click.echo(json.dumps(link, sort_keys=True, indent=4))

@click.command()
@click.argument('path')
@click.option('--check/--no-check', default=False)
@click.option('--list/--no-list', default=False)
@click.option('--verbose/--no-verbose', default=False)
def main(path, check, list, verbose):
    try:
        gblinks = Gblinks(path)

        if check:
            check_broken_links(gblinks, verbose)

        if list:
            list_links(gblinks)
    except ValueError, e:
        click.echo(click.style(str(e), fg='red'))
        sys.exit(-1)

if __name__ == "__main__":
    main()
