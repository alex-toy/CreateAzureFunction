


az webapp webjob continuous start `
    --resource-group $RGName `
    --webjob-name alexeiwj `
    --name $WAName
    # [--ids]
    # [--slot]

az webapp webjob triggered run `
    --resource-group $RGName `
    --webjob-name alexeiwjtest1 `
    --name $WAName
    [--ids]
    [--slot]