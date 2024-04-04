# Emotion Based Song Recommendation System
## Overview

This Django web application utilizes AWS Rekognition service to detect users' emotions through facial images captured via a webcam. Users can create accounts, select preferred artists, and receive personalized song recommendations based on their emotions and artist preferences. The song data is collected through the Spotify API using an ETL (Extract, Transform, Load) pipeline.

![](https://github.com/asus1210/emotion_based_songs/blob/main/a3b7d140-4d97-45fe-8138-19d5c5027cdf.gif)

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/asus1210/emotion_based_song.git
   cd emotion-based-song
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up AWS credentials:

   Create a file named `.env` and add your AWS access and secret keys:

   ```ini
   [default]
   aws_access_key_id = YOUR_ACCESS_KEY
   aws_secret_access_key = YOUR_SECRET_KEY
   ```

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Usage

1. Open the application in your web browser.

2. Create an account or log in with your credentials.

3. Set your preferred artists in your profile.

4. Allow the application to access your webcam for emotion detection.

5. Enjoy personalized song recommendations based on your emotions and artist preferences.

## Dependencies

- Django
- AWS SDK for Python (Boto3)
- OpenCV
- Spotify API Wrapper (Spotipy)

Install these dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```
