"""Tests for blues chord progression generator."""

import pytest

from guitarra.blues import TwelveBarBlues


class TestTwelveBarBlues:
    """Test TwelveBarBlues class."""

    def test_major_progression_c(self):
        """Test major blues progression in C."""
        # Arrange
        blues = TwelveBarBlues("C")

        # Act
        progression = blues.get_major_progression()

        # Assert
        expected = ["C", "C", "C", "C", "F", "F", "C", "C", "G", "F", "C", "C"]
        assert progression == expected

    def test_major_progression_a(self):
        """Test major blues progression in A."""
        # Arrange
        blues = TwelveBarBlues("A")

        # Act
        progression = blues.get_major_progression()

        # Assert
        expected = ["A", "A", "A", "A", "D", "D", "A", "A", "E", "D", "A", "A"]
        assert progression == expected

    def test_minor_progression_a(self):
        """Test minor blues progression in A."""
        # Arrange
        blues = TwelveBarBlues("A")

        # Act
        progression = blues.get_minor_progression()

        # Assert
        expected = [
            "Am",
            "Am",
            "Am",
            "Am",
            "Dm",
            "Dm",
            "Am",
            "Am",
            "E",
            "Dm",
            "Am",
            "Am",
        ]
        assert progression == expected

    def test_sharp_note_handling(self):
        """Test handling of sharp notes."""
        # Arrange
        blues = TwelveBarBlues("F#")

        # Act
        progression = blues.get_major_progression()

        # Assert
        expected = ["F#", "F#", "F#", "F#", "B", "B", "F#", "F#", "C#", "B", "F#", "F#"]
        assert progression == expected

    def test_flat_note_conversion(self):
        """Test conversion of flat notes to sharp notation."""
        # Arrange
        blues = TwelveBarBlues("Bb")

        # Act
        progression = blues.get_major_progression()

        # Assert
        expected = [
            "A#",
            "A#",
            "A#",
            "A#",
            "D#",
            "D#",
            "A#",
            "A#",
            "F",
            "D#",
            "A#",
            "A#",
        ]
        assert progression == expected

    def test_invalid_root_note(self):
        """Test error handling for invalid root notes."""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="Invalid root note"):
            TwelveBarBlues("X")

    def test_format_progression(self):
        """Test progression formatting."""
        # Arrange
        blues = TwelveBarBlues("C")
        progression = blues.get_major_progression()

        # Act
        formatted = blues.format_progression(progression)

        # Assert
        expected_lines = [
            "|    C |    C |    C |    C |",
            "|    F |    F |    C |    C |",
            "|    G |    F |    C |    C |",
        ]
        assert formatted == "\n".join(expected_lines)

    def test_case_insensitive_input(self):
        """Test that input is case insensitive."""
        # Arrange
        blues_lower = TwelveBarBlues("a")
        blues_upper = TwelveBarBlues("A")

        # Act
        progression_lower = blues_lower.get_major_progression()
        progression_upper = blues_upper.get_major_progression()

        # Assert
        assert progression_lower == progression_upper

    def test_format_progression_with_degrees_major(self):
        """Test progression formatting with degrees for major blues."""
        # Arrange
        blues = TwelveBarBlues("C")
        progression = blues.get_major_progression()

        # Act
        formatted = blues.format_progression(progression, show_degrees=True)

        # Assert
        expected_lines = [
            "|    C |    C |    C |    C |",
            "|    I |    I |    I |    I |",
            "",
            "|    F |    F |    C |    C |",
            "|   IV |   IV |    I |    I |",
            "",
            "|    G |    F |    C |    C |",
            "|    V |   IV |    I |    I |",
        ]
        assert formatted == "\n".join(expected_lines)

    def test_format_progression_with_degrees_minor(self):
        """Test progression formatting with degrees for minor blues."""
        # Arrange
        blues = TwelveBarBlues("A")
        progression = blues.get_minor_progression()

        # Act
        formatted = blues.format_progression(progression, show_degrees=True)

        # Assert
        expected_lines = [
            "|   Am |   Am |   Am |   Am |",
            "|    i |    i |    i |    i |",
            "",
            "|   Dm |   Dm |   Am |   Am |",
            "|   iv |   iv |    i |    i |",
            "",
            "|    E |   Dm |   Am |   Am |",
            "|    V |   iv |    i |    i |",
        ]
        assert formatted == "\n".join(expected_lines)
