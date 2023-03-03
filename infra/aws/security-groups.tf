# Create the Security Group
resource "aws_security_group" "app_sg" {
  name_prefix = "${var.name_prefix}-sg"
  vpc_id = aws_vpc.app_vpc.id

  # Ingress rules
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Egress rules
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.name_prefix}-sg"
  }
}