# Use the official Terraform image as the base image
FROM hashicorp/terraform:latest

# Set the working directory to the app's Terraform directory
WORKDIR /app/infra

# Copy the app's Terraform code into the container
COPY . /app/infra

# Install any additional packages or dependencies needed for the Terraform code
RUN apt-get update && apt-get install -y \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set the entrypoint to the Terraform binary
ENTRYPOINT ["terraform"]