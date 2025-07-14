"""Tests for metronome functionality."""

from unittest.mock import patch

from typer.testing import CliRunner

from guitarra.cli import app


class TestMetronomeCommand:
    """Test metronome command functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_metronome_basic_usage(self):
        """Test basic metronome usage with valid BPM."""
        with patch("metronome_rs.py_start_practice_metronome") as mock_start:
            with patch("time.sleep", side_effect=KeyboardInterrupt):
                with patch("metronome_rs.py_stop_global_metronome") as mock_stop:
                    result = self.runner.invoke(app, ["metronome", "120"])

                    assert result.exit_code == 0
                    assert "Starting metronome: 120 BPM" in result.stdout
                    mock_start.assert_called_once_with(120, 4)
                    mock_stop.assert_called_once()

    def test_metronome_with_custom_beats(self):
        """Test metronome with custom beats per measure."""
        with patch("metronome_rs.py_start_practice_metronome") as mock_start:
            with patch("time.sleep", side_effect=KeyboardInterrupt):
                with patch("metronome_rs.py_stop_global_metronome"):
                    result = self.runner.invoke(
                        app, ["metronome", "100", "--beats", "3"]
                    )

                    assert result.exit_code == 0
                    assert "100 BPM, 3/4 time" in result.stdout
                    mock_start.assert_called_once_with(100, 3)

    def test_metronome_with_duration(self):
        """Test metronome with specified duration."""
        with patch("metronome_rs.py_play_metronome_for_duration") as mock_duration:
            result = self.runner.invoke(app, ["metronome", "80", "--duration", "30"])

            assert result.exit_code == 0
            mock_duration.assert_called_once_with(80, 4, 30000)

    def test_metronome_with_eighth_notes(self):
        """Test metronome with eighth note subdivisions."""
        with patch("metronome_rs.py_start_metronome_with_eighth_notes") as mock_eighth:
            with patch("time.sleep", side_effect=KeyboardInterrupt):
                with patch("metronome_rs.py_stop_global_metronome"):
                    result = self.runner.invoke(
                        app, ["metronome", "120", "--subdivisions", "eighth"]
                    )

                    assert result.exit_code == 0
                    assert "eighth notes" in result.stdout
                    mock_eighth.assert_called_once_with(120, 4)

    def test_metronome_with_performance_style(self):
        """Test metronome with performance style."""
        with patch("metronome_rs.py_start_performance_metronome") as mock_perf:
            with patch("time.sleep", side_effect=KeyboardInterrupt):
                with patch("metronome_rs.py_stop_global_metronome"):
                    result = self.runner.invoke(
                        app, ["metronome", "140", "--style", "performance"]
                    )

                    assert result.exit_code == 0
                    mock_perf.assert_called_once_with(140, 4)

    def test_metronome_simple_style(self):
        """Test metronome with simple style."""
        with patch("metronome_rs.py_start_simple_metronome") as mock_simple:
            with patch("time.sleep", side_effect=KeyboardInterrupt):
                with patch("metronome_rs.py_stop_global_metronome"):
                    result = self.runner.invoke(
                        app, ["metronome", "90", "--style", "simple"]
                    )

                    assert result.exit_code == 0
                    mock_simple.assert_called_once_with(90)

    def test_metronome_invalid_bpm_low(self):
        """Test metronome with BPM too low."""
        result = self.runner.invoke(app, ["metronome", "20"])

        assert result.exit_code == 0
        assert "Error: BPM must be between 30 and 300" in result.stderr

    def test_metronome_invalid_bpm_high(self):
        """Test metronome with BPM too high."""
        result = self.runner.invoke(app, ["metronome", "350"])

        assert result.exit_code == 0
        assert "Error: BPM must be between 30 and 300" in result.stderr

    def test_metronome_invalid_beats(self):
        """Test metronome with invalid beats per measure."""
        result = self.runner.invoke(app, ["metronome", "120", "--beats", "20"])

        assert result.exit_code == 0
        assert "Error: Beats per measure must be between 1 and 16" in result.stderr

    def test_get_accent_config_performance(self):
        """Test accent config for performance style."""
        from guitarra.cli import _get_accent_config

        with patch("metronome_rs.PyAccentConfig.strong") as mock_strong:
            _get_accent_config("quarter", "performance")
            mock_strong.assert_called_once()

    def test_get_accent_config_eighth_notes(self):
        """Test accent config for eighth notes."""
        from guitarra.cli import _get_accent_config

        with patch("metronome_rs.PyAccentConfig.with_eighth_notes") as mock_eighth:
            _get_accent_config("eighth", "practice")
            mock_eighth.assert_called_once()

    def test_get_accent_config_triplets(self):
        """Test accent config for triplets."""
        from guitarra.cli import _get_accent_config

        with patch("metronome_rs.PyAccentConfig.with_triplets") as mock_triplets:
            _get_accent_config("triplets", "practice")
            mock_triplets.assert_called_once()
