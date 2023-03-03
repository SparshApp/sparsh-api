FROM ubuntu:latest

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget https://releases.hashicorp.com/terraform/1.0.10/terraform_1.0.10_linux_amd64.zip && \
    unzip terraform_1.0.10_linux_amd64.zip && \
    mv terraform /usr/local/bin && \
    rm terraform_1.0.10_linux_amd64.zip && \
    apt-get remove -y wget unzip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /infra

# Copy the Terraform code to the container
COPY . .

# Call terraform init
RUN terraform init

# Call terraform apply
CMD ["terraform", "apply", "-auto-approve"]