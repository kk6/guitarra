# Guitarra

A command-line tool for guitar practice, starting with 12 bar blues chord progressions.

## Features

- Generate 12 bar blues chord progressions in any key
- Support for both major and minor blues progressions
- Clean, formatted output showing chord progression chart
- Optional Roman numeral degree display for music theory learning
- Support for sharp and flat notation (F#, Bb, etc.)

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

### Basic Usage

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

### Output Examples

**Basic Output:**
```
12 Bar Blues in A major (I-IV-V):

|    A |    A |    A |    A |
|    D |    D |    A |    A |
|    E |    D |    A |    A |
```

**With Roman Numeral Degrees:**
```
12 Bar Blues in A major (I-IV-V):

|    A |    A |    A |    A |
|    I |    I |    I |    I |

|    D |    D |    A |    A |
|   IV |   IV |    I |    I |

|    E |    D |    A |    A |
|    V |   IV |    I |    I |
```

### Available Commands

- `guitar blues <root>` - Generate 12 bar blues progression
  - `<root>` - Root note (A, B, C, D, E, F, G with optional # or b)
  - `--minor, -m` - Generate minor blues progression instead of major
  - `--degrees, -d` - Show Roman numeral degrees for music theory learning

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
│       └── cli.py            # CLI interface
├── tests/
│   ├── __init__.py
│   └── test_blues.py         # Test suite
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

### Supported Notes

- **Natural notes**: C, D, E, F, G, A, B
- **Sharp notes**: C#, D#, F#, G#, A#
- **Flat notes**: Db, Eb, Gb, Ab, Bb (converted to sharp equivalents)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License.
