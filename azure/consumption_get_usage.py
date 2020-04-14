import logging
import os

from azure.mgmt.consumption import ConsumptionManagementClient

# This is a general utility file that I created for myself.
import utilities.general, utilities.azure_common, utilities.azure_consumption


def main(client_id=os.environ['AZURE_CLIENT_ID'],
         client_secret=os.environ['AZURE_CLIENT_SECRET'],
         tenant_id=os.environ['AZURE_TENANT_ID']):
    utilities.general.init_logging(log_file='test_new_log.txt')
    logging.info("Started create budget script")
    logging.info(client_id)
    logging.info(client_secret)
    logging.info(tenant_id)

    credentials = utilities.azure_common.get_credentials_for_sp(client_id, client_secret, tenant_id)
    usage_object = get_usage(credentials)
    logging.debug(usage_object)
    count = 0
    debug = True  # Debug setting
    for obj in usage_object:
        selected, fieldnames = format_data(obj, debug, count)
        utilities.general.write_to_json(selected, "test.json")
        utilities.general.write_to_csv(selected, "test.csv", fieldnames)
        count += 1

    return 0


def format_data(data_object, debug_state, count):
    if debug_state:
        selected = utilities.azure_consumption.get_all_properties_as_dict(data_object, count)
        fieldnames = ["count_id", "additional_properties", "id", "name", "type", "tags", "billing_account_id",
                      "billing_account_name", "billing_period_start_date", "billing_period_end_date",
                      "billing_profile_id", "billing_profile_name", "account_owner_id", "account_name",
                      "subscription_id", "subscription_name", "date_property", "product", "part_number",
                      "meter_id", "meter_details", "quantity", "effective_price", "cost", "unit_price",
                      "billing_currency", "resource_location", "consumed_service", "resource_id", "resource_name",
                      "service_info1", "service_info2", "additional_info", "invoice_section", "cost_center",
                      "resource_group", "reservation_id", "reservation_name", "product_order_id",
                      "product_order_name",
                      "offer_id", "is_azure_credit_eligible", "term", "publisher_name", "publisher_type",
                      "plan_name",
                      "charge_type", "frequency", ]
    else:
        selected = utilities.azure_consumption.get_selected_properties_as_dict(data_object, count)
        fieldnames = ["id", "billing_period_start_date", "billing_period_end_date", "subscription_id",
                      "subscription_name", "quantity", "effective_price", "cost", "unit_price", "billing_currency",
                      "resource_id", "resource_name", "resource_id", "resource_name", "tags", ]

    return selected, fieldnames


def get_usage(credentials=None, subscription_id=os.environ['AZURE_SUBSCRIPTION_ID'], resource_group_name=None):
    if resource_group_name:
        scope = "/subscriptions/" + subscription_id + "/resourceGroups/" + resource_group_name
    else:
        scope = "/subscriptions/" + subscription_id
    logging.debug(scope)

    client = ConsumptionManagementClient(credentials, subscription_id)

    usage_object = client.usage_details.list(scope)

    logging.debug(usage_object)
    return usage_object


if __name__ == '__main__':
    main()
