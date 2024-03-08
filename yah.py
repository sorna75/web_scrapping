import csv
from selenium import webdriver

# Replace 'path/to/chromedriver' with the path to your chromedriver executable
driver = webdriver.Edge()

# Open a website
driver.get(r'https://finance.yahoo.com/quote/%5ENSEI/history/')

# Replace 'your_table_xpath' with the XPath of the entire table
table_xpath = '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table'
table = driver.find_element('xpath', table_xpath)

# Extract data from the table
table_rows = table.find_elements('xpath', './/tr')  # Use find_elements to get all rows
print(len(table_rows))

data = []

#Extract header row
header_row = table_rows[0]
headers = [header.text for header in header_row.find_elements('xpath', './/th')]
data.append(headers)

for row in table_rows:
    row_data = [cell.text for cell in row.find_elements('xpath', './/td')]  # Use find_elements for cells
    data.append(row_data)

# Close the browser window
driver.quit()

# Store the data as a CSV file
csv_file_path = 'table_data.csv'

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f'Table data has been saved to {csv_file_path}')
