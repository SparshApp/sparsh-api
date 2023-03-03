# Create the ECS Cluster
resource "aws_ecs_cluster" "app_ecs_cluster" {
  name = "${var.name_prefix}-ecs-cluster"
}

# Create the Task Definition
resource "aws_ecs_task_definition" "app_ecs_task" {
  family = "${var.name_prefix}-ecs-task"
  container_definitions = jsonencode([
    {
      name = "app"
      image = var.app_image
      # port_mappings {
      #   container_port = var.app_port
      #   host_port = var.app_port
      # }
      environment = [
        {
          name = "DATABASE_URL"
          value = var.database_url
        },
        {
          name = "AWS_REGION"
          value = var.region
        }
      ]
    }
  ])
  cpu = var.task_cpu
  memory = var.task_memory
}