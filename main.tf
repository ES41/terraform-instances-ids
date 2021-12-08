data "external" "external_resource" {
  program = ["/usr/bin/python3", "${path.module}/list_instances.py"]

  query = {
    cluster_name = "production"
  }
}
output "output" {
  value = data.external.external_resource.result
}
