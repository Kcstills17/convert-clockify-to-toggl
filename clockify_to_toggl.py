import pandas as pd
from datetime import datetime, timedelta
from sys import argv

# -------- CONFIG --------
USER_EMAIL = "Youremail@email.com"
# ------------------------

def to_24_hour(t):
    """Convert to 24-hour format if in AM/PM, else return unchanged."""
    try:
        return datetime.strptime(t.strip(), "%I:%M:%S %p").strftime("%H:%M:%S")
    except:
        return t.strip()

def duration_to_hhmmss(duration_str):
    """Normalize durations like '5:30', '1:02:15', etc. to hh:mm:ss."""
    parts = [int(p) for p in duration_str.strip().split(":")]
    while len(parts) < 3:
        parts.insert(0, 0)  # Pad with zeros
    h, m, s = parts
    return str(timedelta(hours=h, minutes=m, seconds=s))

# -------- MAIN --------
input_csv_path = argv[1]
output_csv_path = "toggl_upload.csv"

# Load Clockify export
df = pd.read_csv(input_csv_path)

# Optional column rename (Clockify-specific)
column_mapping = {
    'Duration (h)': 'Duration',
    'Start Date': 'Start date',
    'Start Time': 'Start time',
    'End Date': 'End date',
    'End Time': 'end time',
    'Category': 'Client',
    'Billable Amount (USD)': 'Amount (USD)'
}
df.rename(columns=column_mapping, inplace=True)

# Normalize
df.columns = [col.strip() for col in df.columns]
df['Start time'] = df['Start time'].apply(to_24_hour)
df['Duration'] = df['Duration'].apply(duration_to_hhmmss)

# Ensure required columns exist
df['Description'] = df.get('Description', '-').fillna('-')
df['Project'] = df.get('Project', '-').fillna('-')

# Final DataFrame — strictly for Toggl
df_toggl = pd.DataFrame({
    'Description': df['Description'],
    'Duration': df['Duration'],
    'User': USER_EMAIL,
    'Email': USER_EMAIL,
    'Project': df['Project'],
    'Tags': '-',
    'Start date': df['Start date'],
    'Start time': df['Start time'],
    # 'Stop time': df['Stop time'] This was causing my import to always fail.
})

# Export only valid Toggl columns
df_toggl.to_csv(output_csv_path, index=False, quoting=1)

print(f"✅ Exported Toggl-compatible file: {output_csv_path}")
