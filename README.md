# Django Blog

A simple blog website built with Django. It includes a home page, a page for
all posts, individual post pages, and a custom 404 page.

## Features

- Responsive blog pages styled with custom CSS
- Home page showing the latest posts
- Page listing all blog posts
- Individual post detail pages
- Custom 404 error page
- Automated tests for the main routes

## Built With

- Python 3.14
- Django 5.2
- HTML and CSS

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/syaleng/django-blog.git
   cd django-blog
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install Django:

   ```powershell
   python -m pip install "Django==5.2.17"
   ```

4. Apply the database migrations:

   ```powershell
   python manage.py migrate
   ```

5. Start the development server:

   ```powershell
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

## Run Tests

```powershell
python manage.py test
```

## Author

Created by [syaleng](https://github.com/syaleng).
