from datetime import datetime

# Sample attendance data
attendance_data = [
    {"employee_name": "Rajesh Deshpande", "attendance": {
        "2024-08-15": ("09:00", "17:00"),
        "2024-08-16": ("09:15", "17:10")
    }},
    {"employee_name": "Anjali Sharma", "attendance": {
        "2024-08-15": ("08:45", "17:00"),
        "2024-08-16": ("09:00", "17:05")
    }},
    # Add more employees as needed
]

def calculate_total_hours(clock_in, clock_out):
    format = "%H:%M"
    clock_in_time = datetime.strptime(clock_in, format)
    clock_out_time = datetime.strptime(clock_out, format)
    total_time = clock_out_time - clock_in_time
    return total_time.total_seconds() / 3600  # convert seconds to hours

def analyze_attendance(data):
    attendance_summary = {}

    for entry in data:
        employee_name = entry["employee_name"]
        attendance = entry["attendance"]

        total_hours = 0
        perfect_attendance_days = 0
        absent_days = 0

        for date, times in attendance.items():
            clock_in, clock_out = times
            total_hours += calculate_total_hours(clock_in, clock_out)

            if clock_in == "09:00" and clock_out == "17:00":
                perfect_attendance_days += 1

        attendance_summary[employee_name] = {
            "total_hours": total_hours,
            "perfect_attendance_days": perfect_attendance_days,
            "absent_days": absent_days  # This can be calculated if there's a known total workdays count
        }

    return attendance_summary

def main():
    summary = analyze_attendance(attendance_data)

    for employee, details in summary.items():
        print(f"Employee: {employee}")
        print(f"Total Hours Worked: {details['total_hours']:.2f} hours")
        print(f"Perfect Attendance Days: {details['perfect_attendance_days']}")
        print(f"Absent Days: {details['absent_days']}\n")

if __name__ == "__main__":
    main()
