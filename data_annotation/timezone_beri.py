def generate_schedule_html(month, day, jinja2=None):
    # Dictionary containing sample schedule for a specific date
    schedules = {
        1: {
            "8:00 AM": "Breakfast",
            "9:00 AM": "Work",
            "12:00 PM": "Lunch",
            "1:00 PM": "Work",
            "5:00 PM": "Go home",
            "6:00 PM": "Dinner",
            "7:00 PM": "Relax",
        },
        15: {
            "9:00 AM": "Work",
            "11:00 AM": "Break",
            "12:00 PM": "Lunch",
            "1:00 PM": "Work",
            "4:00 PM": "Attend Meeting",
            "6:00 PM": "Dinner",
            "7:30 PM": "Exercise",
        }
    }

    import calendar

    # Check if the input date is valid
    if month < 1 or month > 12 or day < 1 or day > calendar.monthrange(2023, month)[1]:
        print(f"Invalid date: {month}/{day}")
        return

    template = """<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
   border: 1px solid black;
   border-collapse: collapse;
}
th, td {
   padding: 15px;
}
</style>
</head>
<body>
   <h1>Schedule for {{month}}/{{day}}</h1>
<table>
   <tr>
     <th>Time</th>
     <th>Activity</th>
   </tr>
   {% for time, activity in schedule.items() %}
   <tr>
       <td>{{time}}</td>
       <td>{{activity}}</td>
    </tr>
   {% endfor %}
</table>
</body>
</html>"""

    from jinja2 import Environment, FileSystemLoader

    #if the date is valid, retrieve the schedule for that date
    schedule = schedules.get(day, None)

    if schedule is None:
        print(f"No schedule found for {month}/{day}")
        return

    # Use Jinja2 to render the HTML template
    env = Environment(loader=FileSystemLoader(""))
    template = env.from_string(template)
    output = template.render(month=month, day=day, schedule=schedule)

    # Display the generated HTML
    print(output)