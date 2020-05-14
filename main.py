import json
import file_reader
import google_home_integration

relay_service_local_address = 'http://192.168.0.111:3000/assistant'
product_list_storage_file_path = 'product_list.json'

test_data = [['Milk', '20.05.2020'], ['Butter', '17.05.2020']]

with open(product_list_storage_file_path, 'w') as f:
  json.dump(test_data, f, ensure_ascii=False)

product_list_from_file = file_reader.get_data_from_file(product_list_storage_file_path)
close_to_expire_products_list = file_reader.get_products_with_close_expiration_date(product_list_from_file)
text_to_be_read = file_reader.prepare_text_to_be_read(close_to_expire_products_list)
google_home_integration.read_on_google_home_mini(relay_service_local_address,text_to_be_read)