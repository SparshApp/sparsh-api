terraform {
  required_version = ">= 1.0"
}

variable "aws_region" {
  description = "The AWS region to use"
  type        = string
  default     = "us-west-2"
}

provider "aws" {
  region = var.aws_region
}

# resource "aws_instance" "example" {
#   ami           = "ami-0c55b159cbfafe1f0"
#   instance_type = "t2.micro"
# }