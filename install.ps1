$ErrorActionPreference = "Stop"

$TargetDir = "$env:LOCALAPPDATA\pilu"
if (-not (Test-Path $TargetDir)) { New-Item -ItemType Directory -Path $TargetDir | Out-Null }

$RawBaseUrl = "https://raw.githubusercontent.com/mrpeng4/File-system/main"
$Files = @("main.py", "functions.py", "Root.pilu", "User_data.pilu")

Write-Host "Downloading pilu system files..." -ForegroundColor Cyan
foreach ($File in $Files) {
    Invoke-WebRequest -Uri "$RawBaseUrl/$File" -OutFile "$TargetDir\$File"
}

$BatContent = "@echo off`r`ncd /d `"$TargetDir`"`r`npython main.py %*"
Set-Content -Path "$TargetDir\pilu.bat" -Value $BatContent

$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($UserPath -notlike "*$TargetDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$UserPath;$TargetDir", "User")
}

Write-Host "✅ All files installed successfully! Restart your terminal and type 'pilu' to start." -ForegroundColor Green
