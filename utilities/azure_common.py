from azure.common.credentials import ServicePrincipalCredentials


def main():

    return None


def get_credentials_for_sp(client_id, secret, tenant_id):
    credentials = ServicePrincipalCredentials(
        client_id=client_id,
        secret=secret,
        tenant=tenant_id
    )

    return credentials


if __name__ == '__main__':
    main()