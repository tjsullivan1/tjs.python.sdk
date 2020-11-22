import os
import pprint
import requests
import base64
import json


def build_headers(personal_access_token=os.environ['AZDO_FULL_PAT']):
    with_colon = ":" + personal_access_token
    message_bytes = with_colon.encode('utf8')
    base64_bytes = base64.b64encode(message_bytes)
    token = base64_bytes.decode('utf8')

    headers = {
      'Authorization': f'Basic {token}'
    }

    return headers


def list_projects(organization=os.environ['AZDO_ORG'], headers=build_headers(),
                  api_version='6.1-preview.4', verb="GET", payload={}):

    url = f"https://dev.azure.com/{organization}/_apis/projects?api-version={api_version}"
    response = requests.request(verb, url, headers=headers, data=payload)
    projects = response.text

    return json.loads(projects).get('value')


#TODO: Fix this function. It currently returns a 400 and doesn't show the org in URI. Tested with postman too to no avail.
# currently doeesn't work
# def list_work_items(project, organization='tjsullivan1', headers=build_headers(),
#                   api_version='6.1-preview.3', verb="GET", payload={}):
#     url = f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems?api-version={api_version}"
#     response = requests.request(verb, url, headers=headers, data=payload)
#     work_items = response.text
#
#     return work_items


def list_teams(project_id, organization='tjsullivan1', headers=build_headers(),
                   api_version='6.1-preview.3', verb="GET", payload={}):
    url = f"https://dev.azure.com/{organization}/_apis/projects/{project_id}/teams?api-version={api_version}"

    response = requests.request(verb, url, headers=headers, data=payload)
    teams = response.text

    return json.loads(teams).get('value')