# Guitarra

A command-line tool for guitar practice, featuring 12 bar blues chord progressions and guitar scale visualization.

## Features

### 12 Bar Blues Progressions
- Generate 12 bar blues chord progressions in any key
- Support for both major and minor blues progressions
- Clean, formatted output showing chord progression chart
- Optional Roman numeral degree display for music theory learning

### Guitar Scale Visualization
- Display guitar scales on ASCII fretboard diagrams
- Support for 13 different scales (major, minor, pentatonic, blues, modes, etc.)
- Customizable fret range display
- Option to show scale degrees or note names
- Visual representation of scale patterns across all 6 strings

### Additional Features
- Support for sharp and flat notation (F#, Bb, etc.)
- Tab completion for scale names and commands
- Comprehensive error handling and help messages

## Installation

### Using uv (recommended)

```bash
# Clone the repository
git clone <repository-url>
cd guitarra

# Install dependencies
uv sync

# Install in development mode
uv pip install -e .
```

### Using pip

```bash
# Clone the repository
git clone <repository-url>
cd guitarra

# Install dependencies
pip install -e .
```

## Usage

### Tab Completion Setup (Optional)

Enable tab completion for better user experience:

```bash
# Install tab completion (works on zsh, bash, fish)
guitar install-completion

# For specific shell (optional)
guitar install-completion --shell zsh

# Restart your shell or source your profile
source ~/.zshrc  # or ~/.bashrc for bash users
```

**Note**: Tab completion provides intelligent suggestions for:
- Commands (`blues`, `scale`, `install-completion`)
- Scale names (all 13 supported scales)
- Command options (`--minor`, `--degrees`, `--start`, `--end`)
- Root notes (C, D, E, F, G, A, B with sharps/flats)

### Blues Chord Progressions

```bash
# Generate major blues progression in A
guitar blues A

# Generate minor blues progression in A
guitar blues A --minor

# Use sharp notation
guitar blues F#

# Use flat notation
guitar blues Bb

# Show Roman numeral degrees
guitar blues A --degrees

# Combine options
guitar blues A --minor --degrees
```

### Guitar Scale Visualization

```bash
# Display C major scale on fretboard
guitar scale C major

# Display A minor scale with degrees
guitar scale A minor --degrees

# Display E blues scale from 5th to 10th fret
guitar scale E blues --start=5 --end=10

# Display G pentatonic major scale
guitar scale G pentatonic_major

# Display all available scales
guitar scale C <TAB>  # Press TAB to see all options
```

### Output Examples

**Blues Chord Progression:**
```
12 Bar Blues in A major (I-IV-V):

|    A |    A |    A |    A |
|    D |    D |    A |    A |
|    E |    D |    A |    A |
```

**Blues with Roman Numeral Degrees:**
```
12 Bar Blues in A major (I-IV-V):

|    A |    A |    A |    A |
|    I |    I |    I |    I |

|    D |    D |    A |    A |
|   IV |   IV |    I |    I |

|    E |    D |    A |    A |
|    V |   IV |    I |    I |
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

**Scale with Degrees:**
```
A Minor Scale (Frets 0-12):

E|-5--6-----7-----1-----2--3-----4-----5-
B|-2--3-----4-----5--6-----7-----1-----2-
G|-7-----1-----2--3-----4-----5--6-----7-
D|-4-----5--6-----7-----1-----2--3-----4-
A|-1-----2--3-----4-----5--6-----7-----1-
E|-5--6-----7-----1-----2--3-----4-----5-
   0  1  2  3  4  5  6  7  8  9 10 11 12
```

### Available Commands

#### Blues Progressions
- `guitar blues <root>` - Generate 12 bar blues progression
  - `<root>` - Root note (A, B, C, D, E, F, G with optional # or b)
  - `--minor, -m` - Generate minor blues progression instead of major
  - `--degrees, -d` - Show Roman numeral degrees for music theory learning

#### Guitar Scales
- `guitar scale <root> <scale_name>` - Display guitar scale on fretboard
  - `<root>` - Root note (A, B, C, D, E, F, G with optional # or b)
  - `<scale_name>` - Scale name (major, minor, pentatonic_major, blues, etc.)
  - `--start, -s` - Start fret position (default: 0)
  - `--end, -e` - End fret position (default: 12)
  - `--degrees, -d` - Show scale degrees instead of note names

#### Available Scales
- **Basic**: major, minor, pentatonic_major, pentatonic_minor, blues
- **Modes**: dorian, phrygian, lydian, mixolydian, aeolian, locrian
- **Advanced**: harmonic_minor, melodic_minor

#### Utility Commands
- `guitar install-completion` - Install tab completion for your shell
  - `--shell` - Specify shell type (zsh, bash, fish) - optional, auto-detects if not specified

## Development

### Setup

```bash
# Install development dependencies
uv sync

# Run tests
python -m pytest tests/

# Run CLI in development mode
python -m guitarra.cli blues A
```

### Testing

The project uses pytest with AAA (Arrange-Act-Assert) pattern:

```bash
# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_blues.py
```

### Project Structure

```
guitarra/
├── src/
│   └── guitarra/
│       ├── __init__.py
│       ├── blues.py          # Blues progression logic
│       ├── scales.py         # Guitar scale definitions and fretboard display
│       └── cli.py            # CLI interface
├── tests/
│   ├── __init__.py
│   ├── test_blues.py         # Blues progression tests
│   └── test_scales.py        # Guitar scale tests
├── docs/
│   └── requirements.md       # Detailed requirements (Japanese)
├── pyproject.toml            # Project configuration
└── README.md
```

## Music Theory

### 12 Bar Blues Structure

The 12 bar blues follows this pattern:

**Major Blues (I-IV-V)**
- Bars 1-4: I chord (root)
- Bars 5-6: IV chord (4th)
- Bars 7-8: I chord (root)
- Bar 9: V chord (5th)
- Bar 10: IV chord (4th)
- Bars 11-12: I chord (root)

**Minor Blues (i-iv-V)**
- Same structure but with minor chords for i and iv
- V chord remains major (dominant)

### Guitar Scale Theory

Guitar scales are patterns of notes that create different sounds and moods. This tool displays scales on a standard-tuned guitar fretboard (E-A-D-G-B-E from low to high).

**Scale Categories:**
- **Major scales**: Bright, happy sound (major, lydian, mixolydian)
- **Minor scales**: Darker, more emotional (minor, dorian, phrygian, aeolian, locrian)
- **Pentatonic scales**: Simple, versatile 5-note patterns
- **Blues scales**: Essential for blues, rock, and jazz
- **Advanced scales**: Harmonic minor, melodic minor for jazz and classical

### Supported Notes

- **Natural notes**: C, D, E, F, G, A, B
- **Sharp notes**: C#, D#, F#, G#, A#
- **Flat notes**: Db, Eb, Gb, Ab, Bb (converted to sharp equivalents)

## Requirements

For detailed project requirements and specifications, see the [Requirements Document](docs/requirements.md) (written in Japanese).

Key requirements covered:
- Core functionality specifications
- CLI interface requirements
- Performance and compatibility requirements
- Testing and quality requirements
- Future extension plans

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License.
