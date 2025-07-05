"""Guitar CLI main command interface."""

import click

from guitarra.blues import TwelveBarBlues


@click.group()
def main():
    """Guitar practice CLI tool."""
    pass


@main.command()
@click.argument("root", type=str)
@click.option("--minor", "-m", is_flag=True, help="Generate minor blues progression")
@click.option("--degrees", "-d", is_flag=True, help="Show Roman numeral degrees")
def blues(root: str, minor: bool, degrees: bool):
    """Generate 12 bar blues chord progression.

    Args:
        root: Root note (e.g., A, C#, Bb)
        minor: Generate minor blues progression
        degrees: Show Roman numeral degrees
    """
    try:
        blues_gen = TwelveBarBlues(root)

        if minor:
            progression = blues_gen.get_minor_progression()
            click.echo(f"12 Bar Blues in {root} minor (i-iv-V):")
        else:
            progression = blues_gen.get_major_progression()
            click.echo(f"12 Bar Blues in {root} major (I-IV-V):")

        click.echo()
        click.echo(blues_gen.format_progression(progression, show_degrees=degrees))
        click.echo()

    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        click.echo("Valid notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B", err=True)
        click.echo("You can also use flat notation: Db, Eb, Gb, Ab, Bb", err=True)


if __name__ == "__main__":
    main()
