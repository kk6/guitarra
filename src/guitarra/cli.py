"""Guitar CLI main command interface."""

from typing import Annotated

import metronome_rs
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


@app.command()
def metronome(
    bpm: Annotated[int, typer.Argument(help="Beats per minute (BPM)")],
    beats: Annotated[int, typer.Option("--beats", "-b", help="Beats per measure")] = 4,
    duration: Annotated[
        int,
        typer.Option("--duration", "-d", help="Duration in seconds (0 for infinite)"),
    ] = 0,
    subdivisions: Annotated[
        str,
        typer.Option(
            "--subdivisions",
            "-s",
            help="Subdivision type: quarter, eighth, sixteenth, triplets",
        ),
    ] = "quarter",
    style: Annotated[
        str,
        typer.Option(
            "--style", "-st", help="Metronome style: simple, practice, performance"
        ),
    ] = "practice",
):
    """Start a metronome with customizable settings."""
    try:
        # Validate BPM
        if bpm < 30 or bpm > 300:
            raise ValueError("BPM must be between 30 and 300")

        # Validate beats per measure
        if beats < 1 or beats > 16:
            raise ValueError("Beats per measure must be between 1 and 16")

        typer.echo(
            f"Starting metronome: {bpm} BPM, {beats}/4 time, {subdivisions} notes"
        )
        typer.echo("Press Ctrl+C to stop")
        typer.echo()

        # Choose metronome function based on style and subdivisions
        if duration > 0:
            duration_ms = duration * 1000
            if subdivisions == "quarter":
                metronome_rs.py_play_metronome_for_duration(bpm, beats, duration_ms)
            else:
                accent_config = _get_accent_config(subdivisions, style)
                metronome_rs.py_play_custom_metronome_for_duration(
                    bpm, beats, accent_config, duration_ms
                )
        else:
            if style == "simple":
                metronome_rs.py_start_simple_metronome(bpm)
            elif subdivisions == "eighth":
                metronome_rs.py_start_metronome_with_eighth_notes(bpm, beats)
            elif subdivisions == "sixteenth":
                metronome_rs.py_start_metronome_with_sixteenth_notes(bpm, beats)
            elif subdivisions == "triplets":
                metronome_rs.py_start_metronome_with_triplets(bpm, beats)
            elif style == "performance":
                metronome_rs.py_start_performance_metronome(bpm, beats)
            else:
                metronome_rs.py_start_practice_metronome(bpm, beats)

            # Keep running until Ctrl+C
            try:
                import time

                while True:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                metronome_rs.py_stop_global_metronome()
                typer.echo("\nMetronome stopped.")

    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
    except KeyboardInterrupt:
        metronome_rs.py_stop_global_metronome()
        typer.echo("\nMetronome stopped.")


def _get_accent_config(subdivisions: str, style: str):
    """Get accent configuration based on subdivisions and style."""
    if style == "performance":
        base_config = metronome_rs.PyAccentConfig.strong()
    elif style == "simple":
        base_config = metronome_rs.PyAccentConfig.default()
    else:
        base_config = metronome_rs.PyAccentConfig.subtle()

    if subdivisions == "eighth":
        return metronome_rs.PyAccentConfig.with_eighth_notes()
    elif subdivisions == "sixteenth":
        return metronome_rs.PyAccentConfig.with_sixteenth_notes()
    elif subdivisions == "triplets":
        return metronome_rs.PyAccentConfig.with_triplets()
    else:
        return base_config


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
