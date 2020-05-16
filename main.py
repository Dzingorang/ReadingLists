import json
import file_reader
import google_home_integration
import file_helper

relay_service_local_address = 'http://192.168.0.111:3000/assistant'
file_name_to_download = 'product_list.json'
downloaded_file_name = 'downloaded_file.json'

file_helper.get_file_from_ftp('product_list.json', 'downloaded_file.json')

product_list_from_file = file_reader.get_data_from_file(downloaded_file_name)
close_to_expire_products_list = file_reader.get_products_with_close_expiration_date(product_list_from_file)
text_to_be_read = file_reader.prepare_text_to_be_read(close_to_expire_products_list)
google_home_integration.read_on_google_home_mini(relay_service_local_address,text_to_be_read)