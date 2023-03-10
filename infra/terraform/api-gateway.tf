provider "aws" {
  region = "us-west-2" # replace with the appropriate region
}

resource "aws_api_gateway_rest_api" "example" {
  name = "sparsh-api"
}

resource "aws_api_gateway_resource" "example" {
  rest_api_id = aws_api_gateway_rest_api.example.id
  parent_id   = aws_api_gateway_rest_api.example.root_resource_id
  path_part   = "api"
}

resource "aws_api_gateway_method" "example" {
  rest_api_id   = aws_api_gateway_rest_api.example.id
  resource_id   = aws_api_gateway_resource.example.id
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "example" {
  rest_api_id = aws_api_gateway_rest_api.example.id
  resource_id = aws_api_gateway_resource.example.id
  http_method = aws_api_gateway_method.example.http_method
  type        = "HTTP_PROXY"
  integration_http_method = "GET"
  uri         = "http://${aws_ecs_task_definition.flask.api_task.container_definitions.0.environment_variables.FLASK_APP}/api"
}

resource "aws_api_gateway_deployment" "example" {
  depends_on = [
    aws_api_gateway_integration.example
  ]
  rest_api_id = aws_api_gateway_rest_api.example.id
  stage_name  = "dev"
}

resource "aws_lambda_permission" "example" {
  action       = "lambda:InvokeFunction"
  function_name = aws_lambda_function.flask.arn
  principal    = "apigateway.amazonaws.com"
  source_arn   = aws_api_gateway_deployment.example.execution_arn
}