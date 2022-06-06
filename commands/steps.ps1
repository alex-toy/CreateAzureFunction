################################################################
"resource Group :"

#southcentralus centralus francecentral westus2 eastus centralus 
$Global:RGLocation = "centralus"
$Global:RGName = "migration-rg"


#######################################################################
# Steps :

az group create --name $RGName --location $RGLocation

."commands\CosmosDb\CosmosDb_create.ps1"

."commands\CosmosDb\CosmosDb_proceed.ps1"

."commands\CosmosDb\CosmosDb_populate.ps1"

."commands\StorageAccount\StorageAccount_create.ps1"

."commands\StorageAccount\StorageAccount_keys.ps1"

."commands\ServiceBus\SB_create.ps1"

."commands\FunctionApp\FA_create.ps1"









