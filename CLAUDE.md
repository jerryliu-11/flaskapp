# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment Setup

This is a Flask web application that requires Python 3 and uses a virtual environment for dependency management.

### Setup Commands
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Activate virtual environment and run the Flask app
source venv/bin/activate && python app.py
```

The application runs on http://127.0.0.1:5000 in debug mode by default.

## Architecture Overview

This is a simple Flask-based todo list application with the following structure:

### Core Components

- **app.py**: Main Flask application file containing all routes and business logic
  - Single-file architecture with in-memory storage (todos list)
  - Todo class for data modeling with auto-incrementing IDs
  - Routes: `/` (index), `/add` (POST), `/complete/<id>`, `/delete/<id>`

- **templates/index.html**: Single HTML template with embedded CSS
  - Jinja2 templating for dynamic content rendering
  - Self-contained styling (no external CSS frameworks)
  - Form for adding todos and action buttons for each todo item

### Data Flow

1. **Todo Storage**: In-memory Python list (data is lost on server restart)
2. **Todo Model**: Simple Python class with id, title, description, completed status, and creation timestamp
3. **ID Generation**: Auto-incremented based on list length + 1
4. **State Management**: Server-side only, no client-side JavaScript

### Key Limitations

- **No Persistence**: All data is stored in memory and lost when the server stops
- **No Database**: Uses a simple Python list for storage
- **Single User**: No user authentication or multi-user support
- **No API**: Traditional form-based web application, not RESTful

This architecture is suitable for development and learning but would need significant changes for production use (database integration, proper ID management, user authentication, etc.).