#log_parser.py

from pathlib import Path
import re
from collections import Counter
from datetime import datetime

#generate sample log file
def create_sample_log(path: str = "app.log") -> None:
    """write a realistic app log file for parsing"""
    log_content = [
        "2024-12-01 08:00:01 INFO  Server started on port 8000",
        "2024-12-01 08:01:15 INFO  User alice@example.com logged in",
        "2024-12-01 08:03:22 WARNING  High memory usage: 82%",
        "2024-12-01 08:05:10 INFO  User bob@test.org logged in",
        "2024-12-01 08:07:45 ERROR  Database connection timeout after 30s",
        "2024-12-01 08:09:00 INFO  User carol@company.com logged in",
        "2024-12-01 08:10:33 ERROR  FileNotFoundError: config.yaml not found",
        "2024-12-01 08:12:01 WARNING  API rate limit at 90%",
        "2024-12-01 08:14:55 INFO  Scheduled backup completed successfully",
        "2024-12-01 08:16:20 ERROR  ConnectionRefusedError: Redis unreachable",
        "2024-12-01 08:18:00 INFO  User dave@example.com logged in",
        "2024-12-01 08:20:11 WARNING  Slow query detected: 4.2s",
        "2024-12-01 08:22:30 INFO  Cache cleared",
        "2024-12-01 08:25:00 ERROR  Timeout: external API did not respond",
        "2024-12-01 08:27:45 INFO  User eve@test.org logged in",
        "2024-12-01 08:30:00 INFO  Health check passed",
    ]
    with open(path, "w") as f:
        f.write("\n".join(log_content))
    print(f"sample log written path -> {path}")

#parse each log line into dict
def parse_log_line(line: str) -> dict | None:
    """
    Parse a log line into structured data.

    Expected format:
        YYYY-MM-DD HH:MM:SS LEVEL  Message

    Returns:
        dict with keys: date, time, datetime, level, message
        None if line does not match the expected format.
    """
    pattern = r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(INFO|WARNING|ERROR|DEBUG)\s+(.+)$'
    match = re.match(pattern, line.strip())
    if not match:
        return None
    date_str, time_str, level, message = match.groups()
    return {
        "date"    : date_str,
        "time"    : time_str,
        "datetime": datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S"),
        "level"   : level,
        "message" : message,
    }

#load and parse entire log file
def load_log(path: str) -> list[dict]:
    """Read log file and return list of parsed entry dicts."""
    log_path = Path(path)
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {path}")

    entries = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            parsed = parse_log_line(line)
            if parsed:
                parsed["line_num"] = line_num
                entries.append(parsed)
            else:
                if line.strip():    # ignore blank lines silently
                    print(f"  ⚠️  Line {line_num} skipped (unrecognised format): {line.strip()[:60]}")
    return entries

#analyse parsed entries
def analyse_log(entries: list[dict]) -> dict:
    """Return summary statistics from parsed log entries."""
    if not entries:
        return {}

    level_counts = Counter(e["level"] for e in entries)
    errors       = [e for e in entries if e["level"] == "ERROR"]
    warnings     = [e for e in entries if e["level"] == "WARNING"]
    emails       = []
    for e in entries:
        found = re.findall(r'\b[\w.+-]+@[\w-]+\.[a-z]{2,}\b', e["message"])
        emails.extend(found)

    start = min(e["datetime"] for e in entries)
    end   = max(e["datetime"] for e in entries)

    return {
        "total_entries" : len(entries),
        "level_counts"  : dict(level_counts),
        "error_count"   : level_counts.get("ERROR", 0),
        "warning_count" : level_counts.get("WARNING", 0),
        "info_count"    : level_counts.get("INFO", 0),
        "errors"        : errors,
        "warnings"      : warnings,
        "unique_users"  : list(set(emails)),
        "time_range"    : (start.strftime("%H:%M:%S"), end.strftime("%H:%M:%S")),
        "duration_mins" : round((end - start).seconds / 60, 1),
    }

# ── Step 5: Print a formatted report ─────────────────────────
def print_report(stats: dict) -> None:
    """Pretty-print the log analysis report."""
    print("\n" + "=" * 56)
    print(f"{'📋  LOG FILE ANALYSIS REPORT':^56}")
    print("=" * 56)

    print(f"\n{'📊  Overview'}")
    print("-" * 30)
    print(f"  {'Total entries':<22}: {stats['total_entries']}")
    print(f"  {'Time range':<22}: {stats['time_range'][0]} → {stats['time_range'][1]}")
    print(f"  {'Duration':<22}: {stats['duration_mins']} minutes")

    print(f"\n{'📈  Log Levels'}")
    print("-" * 30)
    bar_chars = {"INFO": "🟢", "WARNING": "🟡", "ERROR": "🔴", "DEBUG": "🔵"}
    for level, count in sorted(stats["level_counts"].items()):
        bar  = bar_chars.get(level, "⚪") * count
        print(f"  {level:<10} {count:>3}   {bar}")

    print(f"\n{'🔴  Errors ({})'.format(stats['error_count'])}")
    print("-" * 30)
    for e in stats["errors"]:
        print(f"  [{e['time']}] {e['message']}")

    print(f"\n{'🟡  Warnings ({})'.format(stats['warning_count'])}")
    print("-" * 30)
    for w in stats["warnings"]:
        print(f"  [{w['time']}] {w['message']}")

    print(f"\n{'👥  Unique Users Detected'}")
    print("-" * 30)
    if stats["unique_users"]:
        for user in sorted(stats["unique_users"]):
            print(f"  • {user}")
    else:
        print("  (none found)")

    print("\n" + "=" * 56)

#save report and filtered errors to file
def save_report(stats: dict, output_dir: str = "logs") -> None:
    """Write error entries and summary report to output files."""
    out = Path(output_dir)
    out.mkdir(exist_ok=True)

    # Save error lines
    errors_path = out / "errors_only.log"
    with open(errors_path, "w", encoding="utf-8") as f:
        f.write(f"# ERROR entries extracted — {len(stats['errors'])} total\n")
        for e in stats["errors"]:
            f.write(f"{e['date']} {e['time']} ERROR  {e['message']}\n")
    print(f"\n💾 Errors saved  → {errors_path}")

    # Save summary report as text
    report_path = out / "summary.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("LOG ANALYSIS SUMMARY\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total entries : {stats['total_entries']}\n")
        f.write(f"Errors        : {stats['error_count']}\n")
        f.write(f"Warnings      : {stats['warning_count']}\n")
        f.write(f"Info          : {stats['info_count']}\n")
        f.write(f"Duration      : {stats['duration_mins']} mins\n")
        f.write(f"Unique users  : {', '.join(sorted(stats['unique_users']))}\n")
    print(f"💾 Summary saved → {report_path}")

#main
# ── Main ──────────────────────────────────────────────────────
if __name__ == "__main__":
    LOG_FILE = "app.log"

    # Generate sample log
    create_sample_log(LOG_FILE)

    # Parse
    print(f"\n📂 Parsing: {LOG_FILE}")
    entries = load_log(LOG_FILE)
    print(f"   Parsed {len(entries)} entries")

    # Analyse
    stats = analyse_log(entries)

    # Report
    print_report(stats)

    # Save outputs
    save_report(stats)