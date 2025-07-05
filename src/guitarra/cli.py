"""Guitar CLI main command interface."""

import click

from guitarra.blues import TwelveBarBlues
from guitarra.scales import Scale, GuitarFretboard


@click.group()
def main():
    """Guitar practice CLI tool."""
    pass


@main.command()
@click.option("--shell", type=click.Choice(["bash", "zsh", "fish"]), help="Shell type")
def install_completion(shell):
    """Install tab completion for the current shell."""
    import os

    if not shell:
        shell = os.environ.get("SHELL", "").split("/")[-1]
        if shell not in ["bash", "zsh", "fish"]:
            shell = "zsh"  # Default to zsh on macOS

    click.echo(f"Installing tab completion for {shell}...")

    try:
        if shell == "zsh":
            # Generate completion script and add to .zshrc
            completion_script = """
#compdef guitar
_guitar() {
  local -a completions
  local -a completions_with_descriptions
  local -a response
  (( ! $+commands[guitar] )) && return 1

  response=("${(@f)$(env COMP_WORDS="${words[*]}" COMP_CWORD=$((CURRENT-1)) _GUITAR_COMPLETE=zsh_complete guitar)}")

  for type key descr in ${response}; do
    if [[ "$type" == "plain" ]]; then
      if [[ "$descr" == "_" ]]; then
        completions+=("$key")
      else
        completions_with_descriptions+=("$key":"$descr")
      fi
    elif [[ "$type" == "dir" ]]; then
      _path_files -/
    elif [[ "$type" == "file" ]]; then
      _path_files -f
    fi
  done

  if [ "$completions_with_descriptions" ]; then
    _describe -V unsorted completions_with_descriptions -U
  fi

  if [ "$completions" ]; then
    compadd -U -V unsorted -a completions
  fi
}

if [[ "$(basename -- ${(%):-%x})" != "_guitar" ]]; then
  compdef _guitar guitar
fi
"""
            zshrc_path = os.path.expanduser("~/.zshrc")

            # Check if already exists
            if os.path.exists(zshrc_path):
                with open(zshrc_path) as f:
                    content = f.read()
                    if "_guitar" in content:
                        click.echo("Tab completion already installed!")
                        return

            # Add completion script
            with open(zshrc_path, "a") as f:
                f.write(completion_script)

            click.echo("Tab completion installed successfully!")
            click.echo("Run: source ~/.zshrc")
        else:
            click.echo(f"Shell {shell} not supported yet. Use --shell zsh")

    except Exception as e:
        click.echo(f"Error installing completion: {e}", err=True)


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


@main.command()
@click.argument("root", type=str)
@click.argument("scale_name", type=click.Choice(Scale.get_available_scales()))
@click.option("--start", "-s", type=int, default=0, help="Start fret position")
@click.option("--end", "-e", type=int, default=12, help="End fret position")
@click.option(
    "--degrees", "-d", is_flag=True, help="Show scale degrees instead of note names"
)
def scale(root: str, scale_name: str, start: int, end: int, degrees: bool):
    """Display guitar scale on fretboard.

    Args:
        root: Root note (e.g., A, C#, Bb)
        scale_name: Name of the scale
        start: Starting fret position
        end: Ending fret position
        degrees: Show scale degrees instead of note names
    """
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
        click.echo(scale_display)

    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        if "Invalid root note" in str(e):
            click.echo("Valid notes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B", err=True)
            click.echo("You can also use flat notation: Db, Eb, Gb, Ab, Bb", err=True)
        elif "Unknown scale" in str(e):
            click.echo(
                f"Available scales: {', '.join(Scale.get_available_scales())}", err=True
            )


if __name__ == "__main__":
    main()
