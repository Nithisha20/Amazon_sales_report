import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reading file
file_path="Amazon Sale Report.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Reading columns
print(data.columns)

# Verify if the Date column is correctly parsed
print(data[['Order ID', 'Date']].head())


# im droping last two columns beacuse its a empty column
data.drop(['New',"PendingS"], axis=1, inplace=True)

# checking whether it have null values
print(data.isnull().sum())

status_mapping = {
    'Cancelled': 'Cancelled',
    'Shipped - Delivered to Buyer': 'Delivered',
    'Pending - Waiting for Pick Up':'Awaiting Pickup',
    'Pending': 'Awaiting Shipment',
    'Shipped': 'Shipped',
    'Shipped - Picked Up': 'Picked up',
    'Shipped - Damaged': 'Damaged in Transit',
    'Shipped - Lost in Transit': 'Lost in Transit',
    'Shipped - Returned to Seller': 'Shipment Returned',
    'Shipped - Returning to Seller': 'Returning to Seller',
    'Shipped - Rejected by Buyer': 'Rejected by Buyer',
    'Shipping':'Shipped',
    'Shipped - Out for Delivery':'Out for delivery'

}

# Update the 'Courier Status' based on the mapping
data['Courier Status'] = data['Status'].map(status_mapping)

# rows for each status category
for status in status_mapping.keys():
    filtered_data = data[data['Status'] == status]
    if not filtered_data.empty:  # Check if there's any data to display
        print(filtered_data[['Order ID', 'Status', 'Courier Status']].head())
        print("-----")


data.loc[data['Courier Status']=='Cancelled','fulfilled-by']='Cancelled'
# print(data[['Order ID', 'Status', 'fulfilled-by']])

data.loc[data['Courier Status']=='Awaiting Shipment','fulfilled-by']='Amazon'
# print(data[['Order ID', 'Status', 'fulfilled-by']])

data.loc[(data['Status'] == 'Shipped') &
         (data['Courier Status'] == 'Shipped') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])

data.loc[(data['Status'] == 'Shipped - Damaged') &
         (data['Courier Status'] == 'Damaged in Transit') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])

data.loc[(data['Status'] == 'Shipped - Lost in Transit') &
         (data['Courier Status'] == 'Lost in Transit') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])


data.loc[(data['Status'] == 'Shipped - Picked Up') &
         (data['Courier Status'] == 'Picked Up') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'

# Fulfilled by Merchant
data.loc[(data['Status'] == 'Shipped - Picked Up') &
         (data['Courier Status'] == 'Picked Up') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])

# Fulfilled by Amazon
data.loc[(data['Status'] == 'Shipped - Out for Delivery') &
         (data['Courier Status'] == 'Shipped') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'

# Fulfilled by Merchant
data.loc[(data['Status'] == 'Shipped - Out for Delivery') &
         (data['Courier Status'] == 'Shipped') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])

# Fulfilled by Amazon
data.loc[(data['Status'] == 'Shipped - Delivered to Buyer') &
         (data['Courier Status'] == 'Delivered') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'

# Fulfilled by Merchant
data.loc[(data['Status'] == 'Shipped - Delivered to Buyer') &
         (data['Courier Status'] == 'Delivered') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'

# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])


# Fulfilled by Amazon
data.loc[(data['Status'] == 'Shipped - Returned to Seller') &
         (data['Courier Status'] == 'Shipment Returned') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'

# Fulfilled by Merchant
data.loc[(data['Status'] == 'Shipped - Returned to Seller') &
         (data['Courier Status'] == 'Shipment Returned') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])
# Fulfilled by Amazon
data.loc[(data['Status'] == 'Shipped - Returning to Seller') &
         (data['Courier Status'] == 'Returning to Seller') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'

# Fulfilled by Merchant
data.loc[(data['Status'] == 'Shipp - Returning to Seller') &
         (data['Courier Status'] == 'Returning to Seller') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])

data.loc[(data['Status'] == 'shipping')&
         (data['Courier Status'] == 'shipped') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'

# Fulfilled by Merchant
data.loc[(data['Status'] == 'shipping') &
         (data['Courier Status'] == 'shipped') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'

# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])

data.loc[(data['Status'] == 'Shipping') &
         (data['Courier Status'] == 'Unshipped'), 'Courier Status'] = 'Shipped'


# Fulfilled by Amazon
data.loc[(data['Status'] == 'Shipping') &
         (data['Fulfilment'] == 'Amazon'), 'fulfilled-by'] = 'Amazon'

# Fulfilled by Merchant
data.loc[(data['Status'] == 'Shipping') &
         (data['Fulfilment'] == 'Merchant'), 'fulfilled-by'] = 'Merchant'
# print(data[['Order ID', 'Status', 'Courier Status', 'Fulfilment', 'fulfilled-by']])


data['Order ID'] = data['Order ID'].astype(str).str.strip()
data['ship-state'] = data['ship-state'].astype(str).str.strip()
data['ship-city'] = data['ship-city'].astype(str).str.strip()
data['ship-postal-code'] = data['ship-postal-code'].astype(str).str.strip()
data['ship-country'] = data['ship-country'].astype(str).str.strip()

print("Missing values after filling and before replacing :")

print(data.isnull().sum())

fill_value="INR"
data['currency'].fillna('INR', inplace=True)
print(data.isnull().sum())

data['Amount'] = data.groupby('Category')['Amount'].transform(lambda x: x.fillna(x.mean()))
print(data.isnull().sum())



data = pd.DataFrame(data)
total_sales = data['Amount'].sum()
average_order_value = data['Amount'].mean()
print(f"Total Sales: {total_sales}")
print(f"Average Order Value: {average_order_value}")
# Since each order_id is unique, i can simply list them with their corresponding order values
aggregated_orders = data.groupby('Order ID')['Amount'].sum().reset_index()
print(aggregated_orders)



category_sales = data.groupby('Category')['Amount'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=category_sales, x='Category', y='Amount')
plt.xticks(rotation=45)
plt.title("Sales by Category")
plt.show()

fulfillment_sales = data.groupby('fulfilled-by')['Amount'].sum().reset_index()

plt.figure(figsize=(8, 6))
sns.barplot(data=fulfillment_sales, x='fulfilled-by', y='Amount')
plt.title("Sales by Fulfillment Type")
plt.show()

city_sales = data.groupby('ship-city')['Amount'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=city_sales, x='ship-city', y='Amount')
plt.xticks(rotation=45)
plt.title("Top 10 Cities by Sales")
plt.show()



return_data = data[data['Courier Status'].isin(['Lost in Transit', 'Shipment Returned', 'Damaged in Transit'])]
total_loss = return_data['Amount'].sum()
print(f"Total Loss due to Returns and Damages: {total_loss}")

repeat_customers_by_postal_code = data.groupby('ship-postal-code')['Order ID'].nunique().reset_index()
repeat_customers_by_postal_code.columns = ['ship-postal-code', 'Order Count']
repeat_customers_by_postal_code = repeat_customers_by_postal_code[repeat_customers_by_postal_code['Order Count'] > 1]

print("Repeat Purchases by Postal Code:")
print(repeat_customers_by_postal_code)

average_order_frequency_by_postal_code = data.groupby('ship-postal-code')['Order ID'].nunique().mean()

print(f"Average Order Frequency per Postal Code: {average_order_frequency_by_postal_code:.2f}")

courier_status_counts = data['Courier Status'].value_counts()
courier_status_percentages = data['Courier Status'].value_counts(normalize=True) * 100

# Combine counts and percentages into a single DataFrame
courier_status_summary = pd.DataFrame({
    'Count': courier_status_counts,
    'Percentage': courier_status_percentages
})

# Display the summary DataFrame
print("Courier Status Breakdown:")
print(courier_status_summary)

# breakdown with a pie chart
plt.figure(figsize=(8, 6))
courier_status_summary['Percentage'].plot.pie(autopct='%1.1f%%', startangle=90, cmap='Pastel1')
plt.ylabel('')
plt.title("Courier Status Breakdown")
plt.show()

