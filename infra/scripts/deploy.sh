terraform init
terraform plan -var-file=config-$(DEPLOY_ENV).tfvars
terraform apply -var-file=config-$(DEPLOY_ENV).tfvars