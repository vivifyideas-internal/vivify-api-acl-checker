import fire
import json
import requests

"""
api_endpoints_file_path string - path to laravel api JSON file generated with
php artisan route:list --json
"""
def acl(api_endpoints_file_path, api_base_url, token_value=''):
  data = load_api_endpoints(api_endpoints_file_path)
  print('Starting')
  test_api_endpoint_permissions(api_base_url, data, token_value)
  return "Completed"

def load_api_endpoints(api_endpoints_file_path):
  with open(api_endpoints_file_path) as f:
    data = json.load(f)

  return data

def test_api_endpoint_permissions(api_base_url, data, token_value=''):
  # in case you are using session :)
  # jar = requests.cookies.RequestsCookieJar()
  # jar.set('laravel_session', session_cookie_value, domain='.example.com', path='/')
  # jar.set('XSRF-TOKEN', token_value, domain='.example.com', path='/')

  for api_endpoint in data:
    api_method = api_endpoint.get('method').split('|')[0] or 'GET'
    api_path = api_endpoint.get('uri')
    response = requests.request(api_method, f'{api_base_url}{api_path}', headers={'accept': 'application/json', 'authorization': token_value})

    print(f'API endpoint: {api_base_url}{api_path} ({api_method})')
    if response.ok:
      print(f'Response is ok {response.status_code}')
      print(response.content)
    else:
      print(f'Response is {response.status_code}')

    print('- - - - -')

if __name__ == '__main__':
  fire.Fire(acl)
