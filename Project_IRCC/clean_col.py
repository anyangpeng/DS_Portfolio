
def clean_col(col):
    """
    This function cleans the column names and add the year information
    """
    if col == 'Unnamed: 0':  # Special case for contry column
        return 'Country'
    elif col[0] == 'U':  # Take care for the annual summary column
        return 'Total, {}'.format(str(int(col.split(':')[1])//17 + 2014))
    elif (len(col.split('.')) == 1) & (col[0] != 'U'):
        return col + ', 2015'
    elif col.split('.')[1] == '1':
        return col.split('.')[0]+', 2016'
    elif col.split('.')[1] == '2':
        return col.split('.')[0]+', 2017'
    elif col.split('.')[1] == '3':
        return col.split('.')[0]+', 2018'
    elif col.split('.')[1] == '4':
        return col.split('.')[0]+', 2019'
    elif col.split('.')[1] == '5':
        return col.split('.')[0]+', 2020'
