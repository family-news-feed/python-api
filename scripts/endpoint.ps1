param ($name)

if (
    "$name" -eq ""
) {
    Write-Output "no endpoint name supplied"
    exit 1
} elseif (
    Test-Path -Path ".\src\endpoints\$name"
) {
    Write-Output "not creating - endpoint already exists"
    exit 1
}

Copy-Item -Path .\src\_template_ -Destination .\src\endpoints\$name -Recurse
Write-Output "created new endpoint $name"