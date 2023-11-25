
# Use the official Python 3.11 image as the base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install the required dependencies
RUN apt-get update && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN python -m pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
