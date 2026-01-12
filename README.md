# monarch-uv-example

A barebones example of using [torchmonarch](https://github.com/pytorch-labs/monarch) with [uv](https://github.com/astral-sh/uv).

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Installing uv

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd monarch-uv
   ```

2. **Run the example:**
   ```bash
   uv run example.py
   ```

   uv will automatically create a virtual environment and install dependencies.

## Manual Setup

If you prefer to set up the environment manually:

```bash
# Install dependencies
uv sync

# Run the example
python example.py
```
