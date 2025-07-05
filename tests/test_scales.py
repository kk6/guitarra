"""Tests for guitar scale functionality."""

import pytest

from guitarra.scales import GuitarFretboard, Scale


class TestScale:
    """Test cases for Scale class."""

    def test_major_scale_notes(self):
        """Test major scale note generation."""
        # Arrange
        scale = Scale("C", "major")

        # Act
        notes = scale.get_scale_notes()

        # Assert
        expected = ["C", "D", "E", "F", "G", "A", "B"]
        assert notes == expected

    def test_minor_scale_notes(self):
        """Test minor scale note generation."""
        # Arrange
        scale = Scale("A", "minor")

        # Act
        notes = scale.get_scale_notes()

        # Assert
        expected = ["A", "B", "C", "D", "E", "F", "G"]
        assert notes == expected

    def test_pentatonic_major_scale(self):
        """Test pentatonic major scale."""
        # Arrange
        scale = Scale("G", "pentatonic_major")

        # Act
        notes = scale.get_scale_notes()

        # Assert
        expected = ["G", "A", "B", "D", "E"]
        assert notes == expected

    def test_blues_scale(self):
        """Test blues scale."""
        # Arrange
        scale = Scale("E", "blues")

        # Act
        notes = scale.get_scale_notes()

        # Assert
        expected = ["E", "G", "A", "A#", "B", "D"]
        assert notes == expected

    def test_flat_note_normalization(self):
        """Test flat note conversion to sharp."""
        # Arrange & Act
        scale = Scale("Bb", "major")

        # Assert
        assert scale.root == "A#"
        expected = ["A#", "C", "D", "D#", "F", "G", "A"]
        assert scale.get_scale_notes() == expected

    def test_invalid_root_note(self):
        """Test invalid root note raises error."""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="Invalid root note"):
            Scale("X", "major")

    def test_invalid_scale_name(self):
        """Test invalid scale name raises error."""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="Unknown scale"):
            Scale("C", "invalid_scale")

    def test_get_available_scales(self):
        """Test getting available scale names."""
        # Arrange & Act
        scales = Scale.get_available_scales()

        # Assert
        assert "major" in scales
        assert "minor" in scales
        assert "pentatonic_major" in scales
        assert "blues" in scales
        assert len(scales) >= 10  # Should have at least 10 scales

    def test_scale_degrees(self):
        """Test scale degree generation."""
        # Arrange
        scale = Scale("C", "major")

        # Act
        degrees = scale.get_scale_degrees()

        # Assert
        expected = [1, 2, 3, 4, 5, 6, 7]
        assert degrees == expected


class TestGuitarFretboard:
    """Test cases for GuitarFretboard class."""

    def test_note_at_fret_calculation(self):
        """Test note calculation at specific fret."""
        # Arrange
        fretboard = GuitarFretboard()

        # Act & Assert
        # E string (6th string, index 0), 3rd fret should be G
        assert fretboard._get_note_at_fret(0, 3) == "G"

        # A string (5th string, index 1), 2nd fret should be B
        assert fretboard._get_note_at_fret(1, 2) == "B"

        # High E string (1st string, index 5), 5th fret should be A
        assert fretboard._get_note_at_fret(5, 5) == "A"

    def test_display_scale_basic(self):
        """Test basic scale display."""
        # Arrange
        scale = Scale("C", "major")
        fretboard = GuitarFretboard()

        # Act
        display = fretboard.display_scale(scale, 0, 5)

        # Assert
        assert "C Major Scale" in display
        assert "Frets 0-5" in display
        assert "E|" in display  # Should show string names
        assert " 0 " in display  # Should show fret numbers

    def test_display_scale_with_degrees(self):
        """Test scale display with degrees."""
        # Arrange
        scale = Scale("C", "major")
        fretboard = GuitarFretboard()

        # Act
        display = fretboard.display_scale(scale, 0, 3, show_degrees=True)

        # Assert
        assert "C Major Scale" in display
        assert "1" in display  # Should show degrees
        assert "2" in display
        assert "3" in display

    def test_display_pentatonic_scale(self):
        """Test pentatonic scale display."""
        # Arrange
        scale = Scale("A", "pentatonic_minor")
        fretboard = GuitarFretboard()

        # Act
        display = fretboard.display_scale(scale, 0, 12)

        # Assert
        assert "A Pentatonic Minor Scale" in display
        assert "Frets 0-12" in display

    def test_display_blues_scale(self):
        """Test blues scale display."""
        # Arrange
        scale = Scale("E", "blues")
        fretboard = GuitarFretboard()

        # Act
        display = fretboard.display_scale(scale, 0, 12)

        # Assert
        assert "E Blues Scale" in display
        assert "Frets 0-12" in display
