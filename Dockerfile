### This file defines the application's image content ###

FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Setup working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Start the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.vonfitbjjInsights.wsgi:application"]