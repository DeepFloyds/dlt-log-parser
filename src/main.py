from pathlib import Path
from parser import parse_dlt_log, summarize_entries, export_summary_to_html

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

if __name__ == "__main__":
    main()