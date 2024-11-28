# Use the official Python image from the Docker Hub
FROM python:3.12.7-slim-bullseye 

# Set the working directory inside the container
WORKDIR /api

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port that Flask runs on (default is 5000)
EXPOSE 5000

# Command to run your Flask application
CMD ["python", "-m", "flask", "--app", "api", "run", "--host=0.0.0.0"]

