"""Python console app with device flow authentication."""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import pprint
import base64
import mimetypes
import os
import urllib
import webbrowser
import requests
import pyperclip

from adal import AuthenticationContext

CLIENT_ID = # insert it here
RESOURCE = 'https://graph.microsoft.com'
API_VERSION = 'beta'
AUTHORITY_URL = 'https://login.microsoftonline.com/common'

def api_endpoint(url):
    """Convert a relative path such as /me/photo/$value to a full URI based
    on the current RESOURCE and API_VERSION settings in config.py.
    """
    if urllib.parse.urlparse(url).scheme in ['http', 'https']:
        return url # url is already complete
    return urllib.parse.urljoin(f'{RESOURCE}/{API_VERSION}/',
                                url.lstrip('/'))


def device_flow_session(client_id, auto=False):
    """Obtain an access token from Azure AD (via device flow) and create
    a Requests session instance ready to make authenticated calls to
    Microsoft Graph.

    client_id = Application ID for registered "Azure AD only" V1-endpoint app
    auto      = whether to copy device code to clipboard and auto-launch browser

    Returns Requests session object if user signed in successfully. The session
    includes the access token in an Authorization header.

    User identity must be an organizational account (ADAL does not support MSAs).
    """
    ctx = AuthenticationContext(AUTHORITY_URL, api_version=None)
    device_code = ctx.acquire_user_code(RESOURCE,
                                        client_id)

    # display user instructions
    if auto:
        pyperclip.copy(device_code['user_code']) # copy user code to clipboard
        webbrowser.open(device_code['verification_url']) # open browser
        print(f'The code {device_code["user_code"]} has been copied to your clipboard, '
              f'and your web browser is opening {device_code["verification_url"]}. '
              'Paste the code to sign in.')
    else:
        print(device_code['message'])

    token_response = ctx.acquire_token_with_device_code(RESOURCE,
                                                        device_code,
                                                        client_id)
    if not token_response.get('accessToken', None):
        return None

    print(f'{token_response["accessToken"]}')

    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {token_response["accessToken"]}',
                            'SdkVersion': 'sample-python-adal',
                            'x-client-SKU': 'sample-python-adal'})
    return session


def test_graph(session):
    print('\nGet user profile ---------> https://graph.microsoft.com/beta/me')
    user_profile = session.get(api_endpoint('me'))
    print(28*' ' + f'<Response [{user_profile.status_code}]>', f'bytes returned: {len(user_profile.text)}\n')
    if not user_profile.ok:
        pprint.pprint(user_profile.json()) # display error
        return
    user_data = user_profile.json()

    print(user_data)

    return None


if __name__ == '__main__':
    GRAPH_SESSION = device_flow_session(CLIENT_ID, True)
    if GRAPH_SESSION:
        test_graph(GRAPH_SESSION)
