# Start from a Python 3.8 base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the test files into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for running tests
ENV APP_ENV=test

# Set the command to run tests
CMD ["python", "-m", "pytest", "--cov-report", "term-missing", "--cov", "app"]