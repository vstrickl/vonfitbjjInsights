### This file defines the application's image content ###

FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Setup working directory
WORKDIR /app

# Install dependencies
COPY /app/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN python -m django --version

# Copy project
COPY . /app/
RUN ls -a /app/

# Expose the application port
EXPOSE 8000

# Start the Django server
ENTRYPOINT ["/app/cmd/run"]