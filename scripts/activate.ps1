param($djangoenv)

if (
    "$djangoenv" -notmatch "(prod|staging|dev|ci)"
) {
    Write-Output "expected 'dev', 'staging', 'prod', or 'ci'. aborting"
    exit 1;
}

.\venv\Scripts\activate.ps1
$env:DJANGO_SETTINGS_MODULE="configs.$djangoenv"
$env:DJANGO_SECRET_KEY=''