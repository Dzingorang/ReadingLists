import json
import os
from datetime import datetime

def get_data_from_file(file_path):
    json_file = open(file_path)
    product_list = json.load(json_file)
    return product_list
        
def prepare_text_to_be_read(close_to_expire_product_list):
    text = ''

    if len(close_to_expire_product_list) == 0:
        text = 'There is no product with close expiration date!'
    else:
        for row in close_to_expire_product_list:
            days_to_expire_text = ''
            if int(row[1]) > 1:
                days_to_expire_text = '{} days. '.format(row[1])
            else:
                days_to_expire_text = '{} day. '.format(row[1])

            text += '{} will expire in {}! '.format(row[0], days_to_expire_text)

    return text

def get_products_with_close_expiration_date(product_list, days_to_exp = 5):
        close_to_expire_product_list = []
        current_date = datetime.now().date()
        for product in product_list:
            exp_date = datetime.strptime(product[1],'%d.%m.%Y').date()
            date_difference = (exp_date - current_date).days
            if date_difference <= days_to_exp:
                close_to_expire_product_list.append([product[0],date_difference])
        return close_to_expire_product_list