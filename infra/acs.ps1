$RG_NAME = "ACS-RG"
$RG_LOCATION = "centralus"
$ACS_NAME = "demoAzCommService"
$ACS_LOCATION = "Global"
$DATA_LOCATION = "United States"

az group create --name $RG_NAME --location $RG_LOCATION

az communication create --name $ACS_NAME --location $ACS_LOCATION --data-location  $DATA_LOCATION --resource-group $RG_NAME