from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import os
import pprint


def connect_azdo(personal_access_token, organization):
    # Create a connection to the org
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)

    # Get a client (the "core" client provides access to projects, teams, etc)
    return connection.clients.get_core_client()


def list_projects(core_client):
    # Get the first page of projects
    get_projects_response = core_client.get_projects()
    index = 0
    while get_projects_response is not None:
        for project in get_projects_response.value:
            pprint.pprint("[" + str(index) + "] " + project.name)
            pprint.pprint("[" + str(index) + "] " + project.id)
            index += 1
        if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
            # Get the next page of projects
            get_projects_response = core_client.get_projects(
                continuation_token=get_projects_response.continuation_token)
        else:
            # All projects have been retrieved
            get_projects_response = None

    return 0


def list_teams(core_client, project_id):
    teams = core_client.get_teams(project_id)

    for team in teams:
        pprint.pprint(team.name)
        pprint.pprint(team.id)

    return 0

# Fill in with your personal access token and org URL
personal_access_token = os.environ['AZDO_FULL_PAT']
organization_url = os.environ['AZDO_ORG']

core_client = connect_azdo(personal_access_token, organization_url)
list_projects(core_client)
my_project = ''
list_teams(core_client, my_project)
my_team = ''
