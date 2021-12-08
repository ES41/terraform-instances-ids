data "external" "external_resource" {
  program = ["/usr/bin/python3", "${path.module}/list_instances.py"]

  query = {
    cluster_name = "change_me"
  }
}
output "output" {
  value = data.external.external_resource.result
}
