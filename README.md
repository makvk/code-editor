# Code Editor

A lightweight, cross-platform code editor for Python, built with Python and PyQt6. Designed for quick scripting and educational purposes.

## Project Structure

```
    code-editor/
    ├── core/                 # Core application logic
    │   ├── __init__.py
    │   ├── executor.py      # Python code execution (PythonRunner)
    │   ├── file_manager.py  # File operations (FileManager)
    │   └── syntax.py        # Python syntax highlighter (PythonHighlighter)
    ├── ui/                  # User interface components
    │   ├── __init__.py
    │   ├── main_window.py   # Main application window
    │   ├── editor_widget.py # Code editor widget
    │   ├── output_widget.py # Output/console panel
    │   └── input_widget.py  # Interactive input field
    ├── main.py              # Application entry point
    ├── requirements.txt     # Project dependencies
    └── README.md            # Project documentation
```

## Features

### Already Implemented: ###
- Code Editing
- Modern text editor with monospaced font (Courier New, 14pt)
- Tab support (4 spaces equivalent)
- Line wrap disabled for better code readability
- Python Syntax Highlighting
- Full Python syntax support (keywords, functions, strings, numbers, comments)
- Custom color scheme (dark theme oriented)
- Real-time highlighting as you type
- Run Python code directly from the editor
- Real-time output display (stdout/stderr)
- Interactive input support (handles input() statements)
- Process execution with proper error handling
- Open existing .py files
- Save current file
- Save As to new location
- UTF-8 encoding support
- Clean, minimalistic design
- Split-pane layout (editor above, output below)
- Dark-themed output panel
- Menu bar with all essential functions
- Status bar



## Requirements

- Python 3.9+
- PyQt6

## Installation

1. Clone the repository
2. Install dependencies:
```bash
    pip install -r requirements.txt
```
3. Run the application:
```bash
    python main.py
```

## Documentation ##
- API Documentation: Generated automatically from docstrings using pdoc:

```bash
    pdoc ./core ./ui -o ./docs/api --html
```
- Code Structure: See the Project Structure section above
- Architecture: The editor follows MVC pattern with clear separation between UI (ui/) and business logic (core/)

## Development ##
### Architecture Overview: ###
- Model: file_manager.py, executor.py (business logic)
- View: All files in ui/ (user interface)
- Controller: main_window.py (coordinates model and view)

## License ##
Python Code Editor is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License (GPL) version 3 as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/gpl-3.0.html.

Note: This project uses PyQt6, which is licensed under the GPL. Therefore, this project is also licensed under the GPLv3 to maintain compliance.

## Planned Features: ##
- Multiple tabs/documents
- Code autocompletion
- Integrated debugger
- Plugin system
- Theme customization
- Git integration
- Code formatting (black/autopep8)
