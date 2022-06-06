# Assuming the project directory name is LocalAzureFuncProject
$root = $pwd

$appName = "contactApp"
Set-Location app/$appName
func azure functionapp publish alexeifa

Set-Location $root

