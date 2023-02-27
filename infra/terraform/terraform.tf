terraform {
  backend "s3" {
    bucket  = "my-terraform-state-bucket"
    key     = "terraform.tfstate"
    region  = "us-west-2"
  }
}

provider "aws" {
  region = "us-west-2"
}