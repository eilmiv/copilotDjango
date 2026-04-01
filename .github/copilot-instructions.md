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
- `WorldListView`: Lists all worlds with their hello counts; also handles inline world creation via POST (uses `FormMixin`)
- `WorldDetailView`: Shows a single world and its count, with a button to send hello
- `send_hello`: POST endpoint that increments a world's hello count

### URLs
- `/` → world list (also handles inline world creation via POST)
- `/world/<pk>/` → world detail
- `/world/<pk>/hello/` → send hello (POST only recommended)

## Development Guidelines
- Follow Django best practices and PEP 8
- Write tests for all new features in `helloworld/tests.py`
- Use class-based views for CRUD operations
- Use function-based views for simple actions like `send_hello`
- Templates extend `helloworld/base.html`
- Run `python manage.py test helloworld` to run tests
- **When replacing a feature or UI flow with an alternative implementation, remove all code that is no longer reachable**: views, URLs, templates, tests, and update these instructions and `README.md`. Leaving dead code behind causes future Copilot sessions to work on it thinking it is still active.

## Project Log
Every pull request must include a new project log entry in the `project-log/` directory.

### Naming convention
Files are named `YYYY-MM-DD_HH-MM-SS_short-summary.md` where:
- `YYYY-MM-DD_HH-MM-SS` is the **UTC merge timestamp** so entries sort chronologically when listed alphabetically
- `short-summary` is a brief kebab-case description of the PR, similar to Django migration names (e.g., `add-greeting-animation`, `inline-world-creation`)

### Two-commit workflow
Because the log entry should link to the exact lines that contain the code changes:
1. **Commit 1** — all code changes for the PR
2. **Commit 2** — the project log entry referencing the SHA(s) from commit 1, with line-level links where possible

### Format
Each log file is a Markdown file of bullet points:
- Start with one or more **broad, abstract** top-level bullets describing the overall goal of the PR; include a link to the PR (e.g., `[PR #5](https://github.com/eilmiv/copilotDjango/pull/5)`)
- Under each abstract bullet, add **indented sub-bullets** that concretise the change — the parent bullet implicitly states *why* the child changes were made
- Continue nesting as many levels as needed (there is no fixed maximum) down to individual file and symbol changes
- Each leaf-level change must include a link to the relevant **line(s)** at the specific commit (`[path/to/file#L42](https://github.com/eilmiv/copilotDjango/blob/<sha>/path/to/file#L42)`); fall back to a file link or bare commit link only when a line number is not meaningful (e.g. a new file, a deletion, or a migration)
- Keep bullets precise but minimal — no complete sentences
- Describe the **final state** of the PR only — write as if everything was done in a single pass; do not mention intermediate commits, iterations, or the order in which changes were made during the PR
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
