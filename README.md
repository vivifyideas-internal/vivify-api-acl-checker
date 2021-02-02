# Vivify ACL checker

CLI utility you can use to check API endpoints permissions

## NAME
    acl.py

## SYNOPSIS
    acl.py {API_ENDPOINTS_FILE_PATH} {API_BASE_URL} <flags>

## POSITIONAL ARGUMENTS

    API_ENDPOINTS_FILE_PATH - file generated with `php artisan route:list --json`

    API_BASE_URL

## FLAGS

    --token_value=TOKEN_VALUE
        Default: ''


## EXAMPLE

```bash
python src/acl.py ./api_endpoints.json http://example.com/ --token_value="Bearer eyJpdiI6InFXZ285QnEwSm9Fa0VnaWo5a0JLMVE9PSIsInZhbHVlIjoiQTNTN1F5d01Zd3VLOWF4U0o1RlkrVzJEd3p3bTFvd1FiZmUwUjdUNm9TQUZtNzF1R1hyL1hnRFNOMWJBclBtZk5"
```
