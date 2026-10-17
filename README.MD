# Dhun

A simple personal music uploader and streamer built with Django.
Upload MP3s from any device on your network, then play or download them.

## Features
- Login
- Upload MP3 files
- Play with seeking
- Download and delete

## Setup
1. `python -m venv venv` then `venv\Scripts\activate`
2. `pip install django`
3. Create `config/local_settings.py` containing `SECRET_KEY = 'your-own-random-key'`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`

## Note
Built for personal use on a private network. Not hardened for the public internet.