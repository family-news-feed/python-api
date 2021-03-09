# unset globals
Remove-Item env:DJANGO_SETTINGS_MODULE -ErrorAction SilentlyContinue
Remove-Item env:DJANGO_SECRET_KEY -ErrorAction SilentlyContinue
Remove-Item env:DJANGO_SESSION_KEY -ErrorAction SilentlyContinue
Remove-Item env:DJANGO_FHIR_APP_ID -ErrorAction SilentlyContinue
Remove-Item env:DJANGO_FHIR_API_BASE -ErrorAction SilentlyContinue
Remove-Item env:DJANGO_FHIR_CLIENT_ID -ErrorAction SilentlyContinue
Remove-Item env:DJANGO_FHIR_REDIRECT_URL -ErrorAction SilentlyContinue

# Deprecated - delete if lingering
Remove-Item env:DJANGO_FHIR_REDIRECT_URI -ErrorAction SilentlyContinue

# call global func `deactivate` created by activate script
deactivate