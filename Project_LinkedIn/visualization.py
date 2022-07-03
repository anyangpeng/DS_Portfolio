import pandas as pd
import os
import folium
import webbrowser


class ds_canada_vis():

    __slots = "_path"

    def __init__(self):
        """This function inialize necessary parameters"""
        self._path = os.path.join(os.getcwd(), "ds_canada.csv")

    def load_data(self):
        """This funciton load the csv file into a DataFrame"""
        self._data = pd.read_csv(self._path, sep="\t", index_col=0)
        print("\n Showing DataFrame Head: \n")
        print(self._data.head())
        print("\n Showing Data Information: \n")
        print(self._data.info())

    def clear_data(self):
        self._data.drop(
            self._data[self._data['Location'] == "Canada"].index, inplace=True)

        self._data.Location.replace({"Greater Toronto Area, Canada": "Toronto, ON", "Toronto, Ontario, Canada": "Toronto, ON",
                                     "Ontario, Canada": "ON", "Edmonton, Alberta, Canada": "Edmonton, AB", "Montreal, Quebec, Canada": "Montreal, QC",
                                     "Montréal-Est, QC": "Montreal, QC", "British Columbia, Canada": "BC", "Algoma, Unorganized, North Part, Ontario, Canada": "Algoma, ON",
                                     "Greater Vancouver, BC": "Vancouver, BC", "Greater Montreal Metropolitan Area": "Montreal, QC", "Greater Calgary Metropolitan Area": "Calgary, AB",
                                     "Regina, Saskatchewan, Canada": "Regina, SK", "Fairford (Part) 50, MB": "Fairford, MB", "Vaughan, Ontario, Canada": "Vaughan, ON",
                                     "Quebec, Canada": "Québec, QC", "Permanent North American Gaeltacht, ON": "ON", "Alberta, Canada": "AB"}, inplace=True)
        self._data.Location = self._data.Location.apply(
            lambda x: x.split(",")[-1].strip())
        self._data.Location.replace({
            "AB": "Alberta",
            "BC": "British Columbia",
            "MB": "Manitoba", "NB": "New Brunswick",
            "NL": "Newfoundland and Labrador",
            "NT": "Northwest Territories",
            "NS": "Nova Scotia",
            "NU": "Nunavut",
            "ON": "Ontario",
            "PE": "Prince Edward Island",
            "QC": "Quebec",
            "SK": "Saskatchewan",
            "YT": "Yukon"
        }, inplace=True)
        self._unique_position = len(self._data.Location.value_counts())
        self._unique_title = len(self._data.Title.value_counts())
        print(self._unique_position, self._unique_title)
        self._results = pd.DataFrame({"State": self._data.Location.value_counts(
        ).index, "Count": self._data.Location.value_counts().values})

    def ploting(self):
        """This funciton plot the Job Density in canada"""
        canada = folium.Map(
            location=[66.1304, -85.3438], zoom_start=3.5)
        folium.Choropleth(
            geo_data=os.path.join(os.getcwd(), "canada.geojson"),  # json
            name='choropleth',
            data=self._results,
            columns=['State', 'Count'],  # columns to work on
            key_on='feature.properties.prov_name_en',
            fill_color='YlOrRd',  # I passed colors Yellow,Green,Blue
            fill_opacity=0.7,
            line_opacity=0.2
            #    legend_name = "Unemployment scale"
        ).add_to(canada)

        return canada


if __name__ == "__main__":
    plot = ds_canada_vis()
    plot.load_data()
    plot.clear_data()
    canada = plot.ploting()
    canada
