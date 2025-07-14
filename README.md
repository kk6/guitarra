# Guitarra

A command-line tool for guitar practice, featuring 12 bar blues chord progressions and guitar scale visualization.

## Features

- Generate 12 bar blues chord progressions in any key (major and minor)
- Display guitar scales on ASCII fretboard diagrams
- Support for 13 different scales (major, minor, pentatonic, blues, modes, etc.)
- Tab completion for commands and scale names
- Customizable fret range display
- Optional Roman numeral degree display for music theory learning

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd guitarra

# Install dependencies and the package
uv sync
uv pip install -e .
```

## Quick Start

### Blues Progressions

```bash
# Generate major blues progression in A
guitar blues A

# Generate minor blues progression with Roman numerals
guitar blues A --minor --degrees
```

### Guitar Scales

```bash
# Display C major scale on fretboard
guitar scale C major

# Display A blues scale from 5th to 10th fret
guitar scale A blues --start=5 --end=10
```

### Tab Completion

Tab completion is automatically enabled when you install the package and provides intelligent suggestions for commands, scale names, and options.

## Usage Examples

**Blues Chord Progression:**
```
12 Bar Blues in A major (I-IV-V):

|    A |    A |    A |    A |
|    D |    D |    A |    A |
|    E |    D |    A |    A |
```

**Guitar Scale Visualization:**
```
C Major Scale (Frets 0-12):

E|-E--F-----G-----A-----B--C-----D-----E-
B|-B--C-----D-----E--F-----G-----A-----B-
G|-G-----A-----B--C-----D-----E--F-----G-
D|-D-----E--F-----G-----A-----B--C-----D-
A|-A-----B--C-----D-----E--F-----G-----A-
E|-E--F-----G-----A-----B--C-----D-----E-
   0  1  2  3  4  5  6  7  8  9 10 11 12
```

## Available Commands

### Blues Progressions
- `guitar blues <root>` - Generate 12 bar blues progression
  - `--minor, -m` - Generate minor blues progression
  - `--degrees, -d` - Show Roman numeral degrees

### Guitar Scales
- `guitar scale <root> <scale_name>` - Display guitar scale on fretboard
  - `--start, -s` - Start fret position (default: 0)
  - `--end, -e` - End fret position (default: 12)
  - `--degrees, -d` - Show scale degrees instead of note names

### Available Scales
- **Basic**: major, minor, pentatonic_major, pentatonic_minor, blues
- **Modes**: dorian, phrygian, lydian, mixolydian, aeolian, locrian
- **Advanced**: harmonic_minor, melodic_minor

## Development

For detailed development guidelines, testing instructions, and project structure, see the [Development Guide](docs/development.md).

Quick development setup:
```bash
uv sync
python -m pytest tests/
python -m guitarra.cli blues A
```

## Documentation

- [Development Guide](docs/development.md) - Detailed development setup and workflow
- [Requirements Document](docs/requirements.md) - Project specifications (Japanese)
- [Tab Completion Documentation](docs/tab-completion.md) - Technical details (Japanese)

## License

This project is licensed under the MIT License.
