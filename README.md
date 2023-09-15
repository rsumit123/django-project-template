# AI Health

## Overview

This project aims to develop an interactive voice-enabled system that serves as a mental health support platform. Users in need of counseling can engage in real-time conversations with an AI. The AI is designed to offer reflective and supportive responses, aiding users in introspection and emotional well-being. Additionally, the system will be equipped with diagnostic capabilities to flag signs of serious issues and subsequently recommend consultations with qualified human experts.

## Features

- process_speech API: Generates text from LLM


## Pre-requisites

- Django
- DjangoRestFramework 
- Gunicorn
- Python

## Installation 

- Navigate to the project directory
- Create a virtual environment with `python3 -m venv venv`
- Install the required packages with `pip install -r requirements.txt`
- Perform migrations with  `python manage.py makemigrations && python manage.py migrate`
- Run the app `python manage.py runserver`
- API swagger docs can then be found at `http://localhost:8000/docs`
- Logs can be found at `http://localhost:8000/logs/`