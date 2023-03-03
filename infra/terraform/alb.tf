# Create a target group for the ECS service
resource "aws_lb_target_group" "ecs_target_group" {
  name     = "ecs-target-group"
  port     = 5000
  protocol = "HTTP"
  vpc_id   = aws_vpc.vpc.id

  health_check {
    path = "/"
  }

  tags = {
    Terraform   = "true"
    Environment = var.environment
  }
}

# Create an ALB listener
resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_lb.load_balancer.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ecs_target_group.arn
  }

  depends_on = [aws_lb_target_group.ecs_target_group]
}

# Attach the target group to the ALB listener
resource "aws_lb_listener_rule" "listener_rule" {
  listener_arn = aws_lb_listener.listener.arn
  priority     = 100

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ecs_target_group.arn
  }

  condition {
    path_pattern {
      values = ["/*"]
    }
  }

  depends_on = [aws_lb_listener.listener, aws_lb_target_group.ecs_target_group]
}