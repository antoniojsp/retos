from datetime import datetime, date, time


def format_row(row, delimiter, primary_key_columns):
    """Serializes data from a database row into a delimited string.

    Args:
        row: A dictionary representing a database row, where keys are column names
             and values are the corresponding data. Data types can include string,
             numeric, date/time, date only, and time only.
        delimiter: A character used to delimit the formatted values in the output
                   string.
        primary_key_columns: A list of column names that constitute the primary key
                             of the row.

    Returns:
        A delimited string containing the formatted primary key and row data.
    """

    def format_value(value):
        if isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            return value
        elif isinstance(value, datetime):
            return str(int(value.timestamp()))
        elif isinstance(value, date):
            return str((value - date(1980, 12, 31)).days)
        elif isinstance(value, time):
            return str(value.hour * 3600 + value.minute * 60 + value.second)
        else:
            raise ValueError(f"Unsupported data type: {type(value)}")

    # Format primary key
    primary_key = delimiter.join(format_value(row[col]) for col in primary_key_columns)

    # Format all columns
    formatted_values = [format_value(row[col]) for col in row]

    # Combine primary key and all columns
    return delimiter.join([primary_key] + formatted_values)


row = {
    'id': 125,
    'name': 'John Doe',
    'balance': 10330.50,
    'created_at': datetime(2021, 10, 27, 10, 0, 0),
    'birthdate': date(1985, 5, 10),
    'last_login': time(13, 30, 0)
}
delimiter = '|'
primary_key_columns = ['id']

formatted_row = format_row(row, delimiter, primary_key_columns)
print(formatted_row)