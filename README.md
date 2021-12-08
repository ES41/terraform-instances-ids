# terraform-instances-ids
Pre-requisites:
- have boto3 moudle imported
- needed AWS permissions 


To customize your cluster name,change this part :
```
# line 5
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
