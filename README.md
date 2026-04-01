# copilotDjango

A Django "Hello World" application where you can create "worlds" and send hello messages to them. The app counts and displays how many hello messages have been sent to each world.

## Features

- 🌍 **Create Worlds**: Add named worlds to greet
- 👋 **Send Hellos**: Send hello messages to any world
- 📊 **Count Tracking**: See how many hellos each world has received
- 🛠️ **Admin Interface**: Manage worlds via Django admin

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eilmiv/copilotDjango.git
   cd copilotDjango
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. (Optional) Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. **Create a World**: Click "Create World" to add a new world
2. **View Worlds**: The home page shows all worlds and their hello counts
3. **Say Hello**: Click on a world then press "Say Hello!" to increment its counter
4. **Admin**: Visit `/admin/` to manage worlds via the Django admin interface

## Project Structure

```
copilotDjango/
├── config/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── helloworld/          # Main application
│   ├── models.py        # World model
│   ├── views.py         # Views (list, detail, create, send hello)
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin configuration
│   ├── tests.py         # Tests
│   └── templates/       # HTML templates
│       └── helloworld/
│           ├── base.html
│           ├── world_list.html
│           ├── world_detail.html
│           └── world_form.html
├── .github/
│   ├── workflows/
│   │   └── ci.yml       # GitHub Actions CI
│   └── copilot-instructions.md
├── manage.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Running Tests

```bash
python manage.py test helloworld
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
