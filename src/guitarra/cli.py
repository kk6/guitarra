"""Guitar CLI main command interface."""

from typing import Annotated

import typer

from guitarra.blues import TwelveBarBlues
from guitarra.scales import GuitarFretboard, Scale


def complete_scale_name(incomplete: str):
    """Autocomplete function for scale names."""
    scale_names = Scale.get_available_scales()
    return [name for name in scale_names if name.startswith(incomplete.lower())]


def complete_root_note(incomplete: str):
    """Autocomplete function for root notes."""
    notes = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
        "Db",
        "Eb",
        "Gb",
        "Ab",
        "Bb",
    ]
    return [note for note in notes if note.upper().startswith(incomplete.upper())]


app = typer.Typer(help="Guitar practice CLI tool")


@app.command()
def blues(
    root: Annotated[
        str,
        typer.Argument(
            help="Root note (e.g., A, C#, Bb)", autocompletion=complete_root_note
        ),
    ],
    minor: Annotated[
        bool, typer.Option("--minor", "-m", help="Generate minor blues progression")
    ] = False,
    degrees: Annotated[
        bool, typer.Option("--degrees", "-d", help="Show Roman numeral degrees")
    ] = False,
):
    """Generate 12 bar blues chord progression."""
    try:
        blues_gen = TwelveBarBlues(root)

        if minor:
            progression = blues_gen.get_minor_progression()
            typer.echo(f"12 Bar Blues in {root} minor (i-iv-V):")
        else:
            progression = blues_gen.get_major_progression()
            typer.echo(f"12 Bar Blues in {root} major (I-IV-V):")

        typer.echo()
        typer.echo(blues_gen.format_progression(progression, show_degrees=degrees))
        typer.echo()

    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        typer.echo("Valid notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B", err=True)
        typer.echo("You can also use flat notation: Db, Eb, Gb, Ab, Bb", err=True)


@app.command()
def scale(
    root: Annotated[
        str,
        typer.Argument(
            help="Root note (e.g., A, C#, Bb)", autocompletion=complete_root_note
        ),
    ],
    scale_name: Annotated[
        str,
        typer.Argument(help="Name of the scale", autocompletion=complete_scale_name),
    ],
    start: Annotated[
        int, typer.Option("--start", "-s", help="Start fret position")
    ] = 0,
    end: Annotated[int, typer.Option("--end", "-e", help="End fret position")] = 12,
    degrees: Annotated[
        bool,
        typer.Option(
            "--degrees", "-d", help="Show scale degrees instead of note names"
        ),
    ] = False,
):
    """Display guitar scale on fretboard."""
    try:
        # Validate fret range
        if start < 0 or end < 0:
            raise ValueError("Fret positions must be non-negative")
        if start > end:
            raise ValueError("Start fret must be less than or equal to end fret")
        if end - start > 24:
            raise ValueError("Fret range too large (max 24 frets)")

        # Create scale and fretboard
        guitar_scale = Scale(root, scale_name)
        fretboard = GuitarFretboard()

        # Display scale
        scale_display = fretboard.display_scale(
            guitar_scale, start_fret=start, end_fret=end, show_degrees=degrees
        )
        typer.echo(scale_display)

    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        if "Invalid root note" in str(e):
            typer.echo("Valid notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B", err=True)
            typer.echo("You can also use flat notation: Db, Eb, Gb, Ab, Bb", err=True)
        elif "Unknown scale" in str(e):
            typer.echo(
                f"Available scales: {', '.join(Scale.get_available_scales())}", err=True
            )


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
