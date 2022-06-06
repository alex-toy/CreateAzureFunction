# Assuming the project directory name is LocalAzureFuncProject
$root = $pwd
Set-Location app

$appName = "contactApp"
func init $appName --python
Set-Location $appName
# func new --name getContacts --template "HTTP trigger" --authlevel "anonymous"
# func new --name getContact --template "HTTP trigger" --authlevel "anonymous"
# func new --name serviceBusFunction --template "Azure Service Bus Queue trigger" 

func new --name testFunction --template "HTTP trigger" --authlevel "anonymous"

# View the list of available templates 
# func templates list -l python

Set-Location $root