from django.shortcuts import render
import pandas as pd
import json
# Create your views here.

def index(request):
    # Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
    # Sample Header to extract

    # Manufacturer,Model,Sales in thousands,4-year resale value,Vehicle type,Price in thousands,Engine size,Horsepower,Wheelbase,Width,Length,Curb weight,Fuel capacity,Fuel efficiency,Latest Launch
    # Previous Header already working

    df = pd.read_csv("SalesRecord.csv")
    rs = df.groupby("Country")["Units Sold"].agg("sum")
    rs_pie = df.groupby("Region")["Units Sold"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)
    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values, 'data': data, 'table_data':table_content}
    return render(request, 'index.html', context=context)