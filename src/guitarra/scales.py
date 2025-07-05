"""Guitar scale definitions and fretboard display functionality."""


class Scale:
    """Base class for musical scales."""

    # Chromatic note progression
    CHROMATIC = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    # Scale interval patterns (semitones from root)
    SCALE_PATTERNS = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "minor": [0, 2, 3, 5, 7, 8, 10],
        "pentatonic_major": [0, 2, 4, 7, 9],
        "pentatonic_minor": [0, 3, 5, 7, 10],
        "blues": [0, 3, 5, 6, 7, 10],
        "dorian": [0, 2, 3, 5, 7, 9, 10],
        "phrygian": [0, 1, 3, 5, 7, 8, 10],
        "lydian": [0, 2, 4, 6, 7, 9, 11],
        "mixolydian": [0, 2, 4, 5, 7, 9, 10],
        "aeolian": [0, 2, 3, 5, 7, 8, 10],  # Same as minor
        "locrian": [0, 1, 3, 5, 6, 8, 10],
        "harmonic_minor": [0, 2, 3, 5, 7, 8, 11],
        "melodic_minor": [0, 2, 3, 5, 7, 9, 11],
    }

    def __init__(self, root: str, scale_name: str):
        """Initialize with root note and scale name.

        Args:
            root: Root note (e.g., 'A', 'C#', 'Bb')
            scale_name: Name of the scale
        """
        self.root = self._normalize_root(root)
        self.scale_name = scale_name.lower()
        self.root_index = self._get_root_index()

        if self.scale_name not in self.SCALE_PATTERNS:
            raise ValueError(f"Unknown scale: {scale_name}")

    def _normalize_root(self, root: str) -> str:
        """Normalize root note notation."""
        root = root.upper()
        # Convert flat notation to sharp
        flat_to_sharp = {"DB": "C#", "EB": "D#", "GB": "F#", "AB": "G#", "BB": "A#"}
        return flat_to_sharp.get(root, root)

    def _get_root_index(self) -> int:
        """Get chromatic index of root note."""
        try:
            return self.CHROMATIC.index(self.root)
        except ValueError:
            raise ValueError(f"Invalid root note: {self.root}")

    def get_scale_notes(self) -> list[str]:
        """Get all notes in the scale."""
        pattern = self.SCALE_PATTERNS[self.scale_name]
        return [
            self.CHROMATIC[(self.root_index + interval) % 12] for interval in pattern
        ]

    def get_scale_degrees(self) -> list[int]:
        """Get scale degrees (1-based)."""
        pattern = self.SCALE_PATTERNS[self.scale_name]
        return [i + 1 for i in range(len(pattern))]

    @classmethod
    def get_available_scales(cls) -> list[str]:
        """Get list of available scale names."""
        return list(cls.SCALE_PATTERNS.keys())


class GuitarFretboard:
    """Guitar fretboard display and scale visualization."""

    # Standard guitar tuning (low to high)
    STANDARD_TUNING = ["E", "A", "D", "G", "B", "E"]

    def __init__(self):
        """Initialize guitar fretboard."""
        self.tuning = self.STANDARD_TUNING.copy()
        self.chromatic = Scale.CHROMATIC

    def _get_note_at_fret(self, string_index: int, fret: int) -> str:
        """Get note at specified string and fret."""
        open_note = self.tuning[string_index]
        open_index = self.chromatic.index(open_note)
        return self.chromatic[(open_index + fret) % 12]

    def display_scale(
        self,
        scale: Scale,
        start_fret: int = 0,
        end_fret: int = 12,
        show_degrees: bool = False,
    ) -> str:
        """Display scale on guitar fretboard.

        Args:
            scale: Scale object to display
            start_fret: Starting fret position
            end_fret: Ending fret position
            show_degrees: Show scale degrees instead of note names

        Returns:
            ASCII representation of the fretboard with scale notes
        """
        scale_notes = scale.get_scale_notes()
        scale_degrees = scale.get_scale_degrees()

        # Create note to degree mapping
        note_to_degree = dict(zip(scale_notes, scale_degrees))

        lines = []

        # Add header
        scale_name_formatted = scale.scale_name.replace("_", " ").title()
        lines.append(
            f"{scale.root} {scale_name_formatted} Scale (Frets {start_fret}-{end_fret}):"
        )
        lines.append("")

        # Build fretboard representation
        for string_index in reversed(range(len(self.tuning))):
            string_name = self.tuning[string_index]
            line = f"{string_name}|"

            for fret in range(start_fret, end_fret + 1):
                note = self._get_note_at_fret(string_index, fret)

                if note in scale_notes:
                    if show_degrees:
                        degree = note_to_degree[note]
                        display_char = str(degree)
                    else:
                        display_char = note

                    # Format to ensure consistent width
                    if len(display_char) == 1:
                        line += f"-{display_char}-"
                    else:
                        line += f"{display_char}-"
                else:
                    line += "---"

            lines.append(line)

        # Add fret numbers
        fret_line = "  "
        for fret in range(start_fret, end_fret + 1):
            fret_str = str(fret)
            if len(fret_str) == 1:
                fret_line += f" {fret_str} "
            else:
                fret_line += f"{fret_str} "

        lines.append(fret_line)

        return "\n".join(lines)
