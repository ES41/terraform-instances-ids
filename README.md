# Terraform-instances-ids

### This small script helps you get your AWS ECS instances id's as a terraform output

Pre-requisites:
- have boto3 moudle imported
- needed AWS permissions 


To customize your cluster name,change this part :
```
# main.tf line 5
 query = {
    cluster_name = "change_me"
  }
}
```

Output examples :

```
terraform apply
```
```
Outputs:

output = tomap({
  "cluster_name" = "change_me"
  "instances_id's" = "['i-xxxxxxxxxxxxxxxx', 'i-xxxxxxxxxxxxxxxx', 'i-xxxxxxxxxxxxxxxx']"
})
```
