# Library Management System

A Django-based web application for managing a library. This system allows librarians to track books, manage user accounts, and automate book tracking and overdue reminders.

## Features

- User accounts and admin controls
- Automated book tracking
- Overdue reminders
- Efficient management of library resources

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/siddugarlapati/Library_Management_System.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Library_Management_System
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Admin Interface**: Manage books and user profiles at `http://127.0.0.1:8000/admin/`.
- **Book List**: View all books at `http://127.0.0.1:8000/books/`.
- **User Profiles**: View user profiles at `http://127.0.0.1:8000/profiles/`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. 