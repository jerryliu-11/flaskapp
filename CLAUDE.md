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
# Default port (5000)
source venv/bin/activate && python app.py

# Custom port
source venv/bin/activate && python app.py 5001
source venv/bin/activate && python app.py 5002
```

The application runs on http://127.0.0.1:5000 in debug mode by default.

## Architecture Overview

This is a simple Flask-based todo list application with single-file architecture.

### Core Components

- **app.py**: Main Flask application file containing all routes and business logic
  - Single-file architecture with in-memory storage (todos list)
  - Todo class for data modeling with auto-incrementing IDs
  - Routes: `/` (index), `/add` (POST), `/complete/<id>` (GET), `/delete/<id>` (GET)

- **templates/index.html**: Single HTML template with 393 lines of embedded CSS
  - Jinja2 templating for dynamic content rendering
  - Animated gradient backgrounds and hover effects
  - Statistics dashboard showing total/completed/remaining tasks

### Data Flow

1. **Todo Storage**: In-memory Python list (data is lost on server restart)
2. **Todo Model**: Simple Python class with id, title, description, completed status, and creation timestamp
3. **ID Generation**: Auto-incremented based on `len(todos) + 1` (has collision bug when todos deleted)
4. **State Management**: Server-side only, no client-side JavaScript

### Known Issues

- **ID Collision Bug**: Using `len(todos) + 1` in app.py:43 causes ID collisions when todos are deleted. If you have todos [1,2,3] and delete #2, the next todo gets ID 3 (collision).
- **Unsafe HTTP Methods**: `/complete/<id>` and `/delete/<id>` use GET requests for state-changing operations (should use POST/DELETE).
- **No CSRF Protection**: Forms lack security tokens.
- **No Data Persistence**: All data lost on server restart.
- **Embedded CSS**: 393 lines of CSS embedded in HTML template makes maintenance difficult.

### Key Limitations

- **No Persistence**: All data is stored in memory and lost when the server stops
- **No Database**: Uses a simple Python list for storage
- **Single User**: No user authentication or multi-user support
- **No API**: Traditional form-based web application, not RESTful
- **No Tests**: Zero test coverage

## Git Workflow

This project uses git worktrees for parallel feature development:

```bash
# Create feature branches
git checkout -b feature-1
git checkout -b feature-2

# Create worktrees for parallel development
git worktree add /tmp/feature-1 feature-1
git worktree add /tmp/feature-2 feature-2

# List worktrees
git worktree list

# Remove worktrees when done
git worktree remove /tmp/feature-1
git worktree remove /tmp/feature-2
```

This architecture is suitable for development and learning but would need significant changes for production use (database integration, proper ID management, user authentication, etc.).
