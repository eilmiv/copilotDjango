# Copilot Instructions

## Project Overview
This is a Django web application that demonstrates a "Hello World" concept where users can create "worlds" and send hello messages to them. The app tracks how many hello messages each world has received.

## Architecture
- **Framework**: Django 4.2+
- **Database**: SQLite (development), configurable for PostgreSQL in production
- **Frontend**: Bootstrap 5 via CDN
- **Project layout**: `config/` for project settings, `helloworld/` for the main app

## Key Components

### Models
- `World`: Has `name` (unique CharField), `hello_count` (PositiveIntegerField), and `created_at` (DateTimeField). The `send_hello()` method increments the count.

### Views
- `WorldListView`: Lists all worlds with their hello counts
- `WorldDetailView`: Shows a single world and its count, with a button to send hello
- `WorldCreateView`: Form to create a new world
- `send_hello`: POST endpoint that increments a world's hello count

### URLs
- `/` → world list
- `/world/new/` → create world
- `/world/<pk>/` → world detail
- `/world/<pk>/hello/` → send hello (POST only recommended)

## Development Guidelines
- Follow Django best practices and PEP 8
- Write tests for all new features in `helloworld/tests.py`
- Use class-based views for CRUD operations
- Use function-based views for simple actions like `send_hello`
- Templates extend `helloworld/base.html`
- Run `python manage.py test helloworld` to run tests

## Project Log
Every pull request must include a new project log entry in the `project-log/` directory.

### Naming convention
Files are named `YYYY-MM-DD_HH-MM-SS.md` using the UTC merge timestamp so that entries sort chronologically when listed alphabetically.

### Format
Each log file is a Markdown file of bullet points:
- Start with one or more **broad, abstract** top-level bullets describing the overall goal of the PR (e.g., "Add greeting animation when sending hello to a world")
- Under each abstract bullet, add **indented sub-bullets** that concretise the change (e.g. which feature was introduced)
- Under those, add further **indented sub-bullets** listing detailed code changes (files added/modified, specific symbols changed)
- Keep bullets precise but minimal — no complete sentences
- If a concrete change serves multiple abstract goals, introduce a new top-level bullet that references the relevant prior bullets instead of duplicating it under each one

## Testing
Run tests with:
```bash
python manage.py test helloworld
```

## Common Commands
```bash
# Start development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```
