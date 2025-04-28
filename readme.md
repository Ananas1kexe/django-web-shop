# Django Web Shop - BookLook

The **django-web-shop**(BookLook) project is a web-based bookshop developed using the Django framework. The project includes functionalities for adding books through the admin panel, as well as user registration and authentication.

## Features

- **User Registration and Authentication**: Users can register on the site and log into their accounts to access the shop’s features.
- **Adding Books through Admin Panel**: Administrators can add books, edit descriptions, prices, and other details via the Django admin panel.
- **Book Management**: Users can browse the book catalog and add items to their cart.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Ananas1kexe/django-web-shop.git
    cd booklook
    ```


2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**:

    - In the `settings.py` file, configure your database settings (e.g., for SQLite or PostgreSQL).
    - Apply the migrations to create the database tables:

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser for the admin panel**:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the on-screen instructions to create the superuser.

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```
## Project Structure

- `booklook/`: The main project folder.
- `main/`: The app responsible for book-related functionality (models, views, forms, etc.).
- `templates/`: Templates for rendering the site pages.
- `requirements.txt`: List of project dependencies.

## Admin Panel

1. Log in to the admin panel via e.g: `http://127.0.0.1:8000/admin/`.
2. Add, edit, and delete books, as well as manage users.

## Technologies

- **Django** — the main framework for building the web application.
- **SQLite** for storing book and user data.
- **HTML, CSS** for the frontend.

## Contribution

If you wish to contribute or make improvements to the project, please fork the repository and submit a pull request. Ensure your changes are tested and do not break existing functionality.

## License

This project is licensed under the [MIT License](https://github.com/Ananas1kexe/django-web-shop/blob/main/LICENSE).