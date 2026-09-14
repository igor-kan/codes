output "vpc_id" {
  description = "ID of the created VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "load_balancer_dns" {
  value     = aws_lb.app.dns_name
  sensitive = false
}
