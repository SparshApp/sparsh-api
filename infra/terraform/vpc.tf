# Create the VPC
resource "aws_vpc" "app_vpc" {
  cidr_block = var.vpc_cidr
  tags = {
    Name = "${var.name_prefix}-vpc"
  }
}

# Create the Subnet
resource "aws_subnet" "app_subnet" {
  vpc_id = aws_vpc.app_vpc.id
  cidr_block = var.subnet_cidr
  availability_zone = var.availability_zone
  tags = {
    Name = "${var.name_prefix}-subnet"
  }
}

# Create the Internet Gateway
resource "aws_internet_gateway" "app_igw" {
  vpc_id = aws_vpc.app_vpc.id
  tags = {
    Name = "${var.name_prefix}-igw"
  }
}

# Create the Route Table for the VPC and Internet Gateway
resource "aws_route_table" "app_rt" {
  vpc_id = aws_vpc.app_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.app_igw.id
  }
  tags = {
    Name = "${var.name_prefix}-rt"
  }
}

# Associate the Route Table with the Subnet
resource "aws_route_table_association" "app_rt_association" {
  subnet_id = aws_subnet.app_subnet.id
  route_table_id = aws_route_table.app_rt.id
}