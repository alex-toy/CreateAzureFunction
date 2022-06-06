Create an Azure Function
=
In this project, we will be creating an Azure function triggered by an HTTP. It will include an Azure Service Bus.


## Steps
1. Run **commands\steps.ps1**.
2. Run **commands\publish_functions.ps1**.
3. Modify existing functions or create new ones by modifying according to your needs and then running **commands\create_local_function.ps1** and then republish them with **commands\publish_functions.ps1**.


## General explanations
1. Create a Function App named ReviewFunctionApp with one function Review
2. Update the __init__.py file with the contents of this file.
3. Run the function application locally and ensure no errors
4. Deploy the function to Azure
    - Function App: myreviewapp
    - Language: Python
    - Hosting Plan: Consumption Plan

Test your Azure function with the Azure URL on the browser.