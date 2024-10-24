# Start from the desired Python version
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for Cloud Run's expected port
ENV PORT 8080

# Command to run the application
CMD ["python", "app.py"]
