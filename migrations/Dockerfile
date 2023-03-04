# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variables for the database
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword
ENV MYSQL_HOST=db
ENV MYSQL_PORT=3306

# Install MySQL client
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the Alembic migration scripts to the working directory
COPY alembic alembic

# Expose the port used by the MySQL server
EXPOSE 3306

# Set the entrypoint command to run the Alembic migrations
ENTRYPOINT ["alembic", "upgrade", "head"]