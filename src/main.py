from pathlib import Path
from parser import parse_dlt_log, summarize_entries, export_summary_to_html, export_summary_to_csv

def main():
    entries = parse_dlt_log(Path("example_data/dlt_log.txt"))
    summary = summarize_entries(entries)

    for e in entries:
        print(e)
        
        
    
    print("\nSummary per module:")
    for module, counts in summary.items():
        print(f"{module}: {counts}")    
        
        
        
    export_summary_to_html(summary, Path("example_data/dlt_summary.html"))
    print("Summary exported to HTML.")

    export_summary_to_csv(summary, Path("example_data/dlt_summary.csv"))
    print("Summary exported to CSV.")    

if __name__ == "__main__":
    main()
    