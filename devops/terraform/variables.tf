variable "region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region"
}

variable "environment" {
  type        = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "environment must be dev, staging or prod"
  }
}

variable "instance_count" {
  type    = number
  default = 2
}

variable "allowed_cidrs" {
  type    = list(string)
  default = ["10.0.0.0/8"]
}
