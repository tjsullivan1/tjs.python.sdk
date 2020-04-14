def main():

    return None


def get_all_properties_as_dict(consumption_usage_detail, count=0):
    data_as_dict = {
        'count_id': count,
        'additional_properties': consumption_usage_detail.additional_properties,
        'id': consumption_usage_detail.id,
        'name': consumption_usage_detail.name,
        'type': consumption_usage_detail.type,
        'tags': consumption_usage_detail.tags,
        'billing_account_id': consumption_usage_detail.billing_account_id,
        'billing_account_name': consumption_usage_detail.billing_account_name,
        'billing_period_start_date': consumption_usage_detail.billing_period_start_date,
        'billing_period_end_date': consumption_usage_detail.billing_period_end_date,
        'billing_profile_id': consumption_usage_detail.billing_profile_id,
        'billing_profile_name': consumption_usage_detail.billing_profile_name,
        'account_owner_id': consumption_usage_detail.account_owner_id,
        'account_name': consumption_usage_detail.account_name,
        'subscription_id': consumption_usage_detail.subscription_id,
        'subscription_name': consumption_usage_detail.subscription_name,
        'date_property': consumption_usage_detail.date_property,
        'product': consumption_usage_detail.product,
        'part_number': consumption_usage_detail.part_number,
        'meter_id': consumption_usage_detail.meter_id,
        'meter_details': consumption_usage_detail.meter_details,
        'quantity': consumption_usage_detail.quantity,
        'effective_price': consumption_usage_detail.effective_price,
        'cost': consumption_usage_detail.cost,
        'unit_price': consumption_usage_detail.unit_price,
        'billing_currency': consumption_usage_detail.billing_currency,
        'resource_location': consumption_usage_detail.resource_location,
        'consumed_service': consumption_usage_detail.consumed_service,
        'resource_id': consumption_usage_detail.resource_id,
        'resource_name': consumption_usage_detail.resource_name,
        'service_info1': consumption_usage_detail.service_info1,
        'service_info2': consumption_usage_detail.service_info2,
        'additional_info': consumption_usage_detail.additional_info,
        'invoice_section': consumption_usage_detail.invoice_section,
        'cost_center': consumption_usage_detail.cost_center,
        'resource_group': consumption_usage_detail.resource_group,
        'reservation_id': consumption_usage_detail.reservation_id,
        'reservation_name': consumption_usage_detail.reservation_name,
        'product_order_id': consumption_usage_detail.product_order_id,
        'product_order_name': consumption_usage_detail.product_order_name,
        'offer_id': consumption_usage_detail.offer_id,
        'is_azure_credit_eligible': consumption_usage_detail.is_azure_credit_eligible,
        'term': consumption_usage_detail.term,
        'publisher_name': consumption_usage_detail.publisher_name,
        'publisher_type': consumption_usage_detail.publisher_type,
        'plan_name': consumption_usage_detail.plan_name,
        'charge_type': consumption_usage_detail.charge_type,
        'frequency': consumption_usage_detail.frequency,
    }

    return data_as_dict


def get_selected_properties_as_dict(consumption_usage_detail, count=0):
    selected_data = {
        'id': count,
        'billing_period_start_date': consumption_usage_detail.billing_period_start_date,
        'billing_period_end_date': consumption_usage_detail.billing_period_end_date,
        'subscription_id': consumption_usage_detail.subscription_id,
        'subscription_name': consumption_usage_detail.subscription_name,
        'quantity': consumption_usage_detail.quantity,
        'effective_price': consumption_usage_detail.effective_price,
        'cost': consumption_usage_detail.cost,
        'unit_price': consumption_usage_detail.unit_price,
        'billing_currency': consumption_usage_detail.billing_currency,
        'resource_id': consumption_usage_detail.resource_id,
        'resource_name': consumption_usage_detail.resource_name,
        'resource_id': consumption_usage_detail.resource_id,
        'resource_name': consumption_usage_detail.resource_name,
        'tags': consumption_usage_detail.tags,
    }

    return selected_data


if __name__ == '__main__':
    main()