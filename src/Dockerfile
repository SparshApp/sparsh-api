# Use the official Python image as the base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY . /app

# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the API endpoint
EXPOSE 5001

# Run app.py when the container launches
CMD ["python3", "app.py"]
