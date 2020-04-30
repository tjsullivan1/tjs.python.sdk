import requests
import logging
import json
import os
# This is a general utility file that I created for myself.
import utilities.general, utilities.azure_common, utilities.azure_consumption


def main(client_id=os.environ['AZURE_CLIENT_ID'],
         client_secret=os.environ['AZURE_CLIENT_SECRET'],
         tenant_id=os.environ['AZURE_TENANT_ID'],
         subscription_id=os.environ['AZURE_SUBSCRIPTION_ID']):

    utilities.general.init_logging(log_file='test_new_log.txt')
    logging.info("Started create budget script")
    logging.info(client_id)
    logging.info(client_secret)
    logging.info(tenant_id)

    credentials = utilities.azure_common.get_credentials_for_sp(client_id, client_secret, tenant_id)
    token = utilities.azure_common.get_bearer_token(credentials)

    usage_string = query_usage_details(subscription_id, token)
    usage_object = json.loads(usage_string)['value']

    logging.debug(usage_object)
    count = 0
    debug = False  # Debug setting
    for obj in usage_object:
        # obj is dictionary (usage object was a list), but it contains another dictionary (properties)
        selected = obj['properties']
        fieldnames = list(obj['properties'].keys())
        # selected, fieldnames = utilities.azure_consumption.format_data(obj, debug, count)
        utilities.general.write_to_json(selected, "test.json")
        utilities.general.write_to_csv(selected, "test.csv", fieldnames)
        count += 1

    return 0


def query_usage_details(subscription, token, api_version='2019-04-01-preview', verb="GET",
                        provider="Microsoft.Consumption", resource="usageDetails"):
    url = f"https://management.azure.com/subscriptions/{subscription}/providers/{provider}/{resource}" \
          f"?api-version={api_version}"

    payload = {}
    headers = {
      'Authorization': f'Bearer {token}'
    }

    response = requests.request(verb, url, headers=headers, data=payload)

    return response.text


if __name__ == '__main__':
    main()