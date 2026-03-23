import html
import csv
from pathlib import Path
from dataclasses import dataclass

@dataclass
class LogEntry:
    timestamp: str
    level: str
    module: str
    message: str


def parse_dlt_log(path: Path) -> list[LogEntry]:
    entries = []

    with path.open("r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # split example line
            # 2026-03-02 10:01:02 [INFO] Display: Backlight initialized

            timestamp, rest = line.split(" [", 1)
            level, rest = rest.split("] ", 1)
            module, message = rest.split(": ", 1)

            entry = LogEntry(timestamp, level, module, message)
            entries.append(entry)

    return entries
    
    
def summarize_entries(entries):
    """
    Summarizes DLT log entries.
    Returns a dictionary:
    {
        'ModuleName': {'INFO': count, 'WARNING': count, 'ERROR': count}
    }
    """
    summary = {}

    for e in entries:
        if e.module not in summary:
            summary[e.module] = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        summary[e.module][e.level] += 1

    return summary    
    
    
def export_summary_to_html(summary: dict, path: Path):
    """
    Exports the summary dictionary to a simple HTML table.
    """
    # Start HTML document
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DLT Log Summary</title>
    <style>
        table {border-collapse: collapse; width: 60%; margin: 20px;}
        th, td {border: 1px solid black; padding: 8px; text-align: center;}
        th {background-color: #f2f2f2;}
        .ERROR {background-color: #f8d7da;}      /* red-ish for errors */
        .WARNING {background-color: #fff3cd;}    /* yellow-ish for warnings */
        .INFO {background-color: #d1e7dd;}       /* green-ish for info */
    </style>
</head>
<body>
    <h2>DLT Log Summary per Module</h2>
    <table>
        <tr>
            <th>Module</th><th>INFO</th><th>WARNING</th><th>ERROR</th>
        </tr>
"""

    # Add table rows
    for module, counts in summary.items():
        html_content += f"""
        <tr>
            <td>{html.escape(module)}</td>
            <td class="INFO">{counts['INFO']}</td>
            <td class="WARNING">{counts['WARNING']}</td>
            <td class="ERROR">{counts['ERROR']}</td>
        </tr>
"""

    # Close HTML
    html_content += """
    </table>
</body>
</html>
"""

    # Write to file
    with path.open("w", encoding="utf-8") as f:
        f.write(html_content)    
        
        
        
        
 
def export_summary_to_csv(summary: dict, path: Path):
    """
    Export summary to CSV file.
    Each row = one module
    """
    fieldnames = ["Module", "INFO", "WARNING", "ERROR"]

    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        for module, counts in summary.items():
            row = {
                "Module": module,
                "INFO": counts["INFO"],
                "WARNING": counts["WARNING"],
                "ERROR": counts["ERROR"]
            }
            writer.writerow(row) 