

# Sticky Notes App

## Run locally with venv
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

## Run with Docker
1. docker build -t sticky_notes .
2. docker run -p 8000:8000 sticky_notes

## Notes
- Do NOT commit secrets.
- Add your own `.env` file for sensitive info.
"# sticky_notes" 
