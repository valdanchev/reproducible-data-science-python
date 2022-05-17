

def subperiod_mobility_trends(data, start_date, end_date):
    """
    Add your mobility data in `data`.

    This function selects a subperiod of the mobility data based on prespecified start data and end date.
    """
    mobility_trends = data[
        data["date"].isin(pd.date_range(start=start_date, end=end_date))
    ]
    return mobility_trends


def rename_mobility_trends(data):
    """
    This function renames the column headings of the six mobility categories.
    """
    mobility_trends_renamed = data.rename(
        columns={
            "retail_and_recreation_percent_change_from_baseline": "Retail_Recreation",
            "grocery_and_pharmacy_percent_change_from_baseline": "Grocery_Pharmacy",
            "parks_percent_change_from_baseline": "Parks",
            "transit_stations_percent_change_from_baseline": "Transit_stations",
            "workplaces_percent_change_from_baseline": "Workplaces",
            "residential_percent_change_from_baseline": "Residential",
        }
    )
    return mobility_trends_renamed
