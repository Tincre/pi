# pi

Using the Gauss-Legendre Algorithm to calculate Pi.

## Usage

```
 Usage: pi.py [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.           │
│ --show-completion             Show completion for the current shell, to copy it   │
│                               or customize the installation.                      │
│ --help                        Show this message and exit.                         │
╰───────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────╮
│ calculate-pi                 Returns the correct value of Pi up to the given      │
│                              digits.                                              │
│ calculate-pi-gauss-legendre  This implements the Gauss-Legendre algorithm to      │
│                              calculate the value of Pi. Because it is memory      │
│                              intensive, practitioners typically do not implement  │
│                              this algorithm for actually calculating Pi.          │
│ truncate-decimal             Truncates a Decimal value to a specified number of   │
│                              decimal places.                                      │
╰───────────────────────────────────────────────────────────────────────────────────╯
```

To calcualte Pi to 39 digits:

```bash
python pi.py calculate-pi 39
```

## Happy Pi Day 2024

[tincre.com](https://tincre.com) made this to represent Pi day 2024 (March 14th, 2024). This library is entirely inconsequential but we're happy to accept contributions.
