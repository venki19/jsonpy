Connect-AzAccount

function checkstatus {
  
    $obj = Get-AzServiceBusQueue -ResourceGroupName tranrg -Name fileuplaod -Namespace transervicebus
    $value =  $obj.CountDetails.ActiveMessageCount
    return $value

}

while(1)
{
    $count = checkstatus
    if($count -eq 0){
    Start-Sleep 5 
    $count = checkstatus
    if($count -eq 0){
        Write-host "count is zero"
        start-sleep 5 
    }
    }  
    if($count -ne 0){
    write-host "count is present $count"
    }
    start-sleep 10
} 

