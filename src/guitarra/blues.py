"""12 bar blues chord progression generator."""


class TwelveBarBlues:
    """Generate 12 bar blues chord progressions."""

    # Major blues progression (I-IV-V)
    MAJOR_PATTERN = ["I", "I", "I", "I", "IV", "IV", "I", "I", "V", "IV", "I", "I"]

    # Minor blues progression (i-iv-V)
    MINOR_PATTERN = ["i", "i", "i", "i", "iv", "iv", "i", "i", "V", "iv", "i", "i"]

    # Chromatic note progression
    CHROMATIC = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def __init__(self, root: str):
        """Initialize with root note.

        Args:
            root: Root note (e.g., 'A', 'C#', 'Bb')
        """
        self.root = self._normalize_root(root)
        self.root_index = self._get_root_index()

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

    def _get_chord_note(self, interval: int) -> str:
        """Get note at specified interval from root."""
        return self.CHROMATIC[(self.root_index + interval) % 12]

    def get_major_progression(self) -> list[str]:
        """Get major 12 bar blues progression."""
        chord_mapping = {
            "I": self.root,  # Root (0 semitones)
            "IV": self._get_chord_note(5),  # Perfect 4th (5 semitones)
            "V": self._get_chord_note(7),  # Perfect 5th (7 semitones)
        }
        return [chord_mapping[roman] for roman in self.MAJOR_PATTERN]

    def get_minor_progression(self) -> list[str]:
        """Get minor 12 bar blues progression."""
        chord_mapping = {
            "i": self.root + "m",  # Root minor
            "iv": self._get_chord_note(5) + "m",  # 4th minor
            "V": self._get_chord_note(7),  # 5th major (dominant)
        }
        return [chord_mapping[roman] for roman in self.MINOR_PATTERN]

    def format_progression(self, progression: list[str], show_degrees: bool = False) -> str:
        """Format progression as a readable chart."""
        bars = []

        if show_degrees:
            # Get the roman numeral pattern for degrees
            degrees = self.MINOR_PATTERN if any("m" in chord for chord in progression) else self.MAJOR_PATTERN

            for i in range(0, 12, 4):
                # Format chord line
                chord_line = " | ".join(f"{chord:>4}" for chord in progression[i : i + 4])
                bars.append(f"| {chord_line} |")

                # Format degree line
                degree_line = " | ".join(f"{degree:>4}" for degree in degrees[i : i + 4])
                bars.append(f"| {degree_line} |")

                # Add separator line except for the last group
                if i < 8:
                    bars.append("")
        else:
            for i in range(0, 12, 4):
                bar_line = " | ".join(f"{chord:>4}" for chord in progression[i : i + 4])
                bars.append(f"| {bar_line} |")

        return "\n".join(bars)
