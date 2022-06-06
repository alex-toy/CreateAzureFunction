"###############################################################"
"Now running : " + $MyInvocation.MyCommand.Path
"###############################################################"


################################################################
"CREATE A COLLECTION :"

az cosmosdb mongodb collection create `
    --resource-group $RGName `
    --account-name $CDBDatabaseAccount `
    --database-name $CDBName `
    --name users `
    # [--analytical-storage-ttl]
    # [--idx]
    # [--max-throughput]
    # [--shard]
    # [--throughput]





az cosmosdb mongodb collection create `
    --resource-group $RGName `
    --account-name $CDBDatabaseAccount `
    --database-name $CDBName `
    --name contacts `
    # [--analytical-storage-ttl]
    # [--idx]
    # [--max-throughput]
    # [--shard]
    # [--throughput]