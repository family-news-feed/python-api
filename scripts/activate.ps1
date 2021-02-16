param($djangoenv)

# Allowed envs are 'prod', 'staging', 'dev', and 'ci'
if (
    "$djangoenv" -notmatch "(prod|staging|dev|ci)"
) {
    Write-Output @"
Usage: activate.ps1 [prod|staging|dev|ci]
        expected 'dev', 'staging', 'prod', or 'ci'. got '$djangoenv'
"@
    exit 1;
}

# Activate virtualenv
.\venv\Scripts\activate.ps1

# Activate django settings module
$env:DJANGO_SETTINGS_MODULE="configs.$djangoenv"

# Set environment variables for use with os.environ.get()
$env:DJANGO_SECRET_KEY=''
$env:DJANGO_FHIR_APP_ID=''
$env:DJANGO_FHIR_API_BASE=''
$env:DJANGO_FHIR_CLIENT_ID=''
$env:DJANGO_FHIR_REDIRECT_URI=''
