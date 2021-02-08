# unset globals
Remove-Item env:DJANGO_SETTINGS_MODULE -ErrorAction SilentlyContinue
Remove-Item env:DJANGO_SECRET_KEY -ErrorAction SilentlyContinue

# call global func `deactivate` created by activate script
deactivate