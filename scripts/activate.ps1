param($djangoenv)

if (
    "$djangoenv" -notmatch "(prod|staging|dev)"
) {
    Write-Output "expected 'dev', 'staging', or 'prod'. aborting"
    exit 1;
}

.\venv\Scripts\activate.ps1
$env:DJANGO_SETTINGS_MODULE="configs.$djangoenv"