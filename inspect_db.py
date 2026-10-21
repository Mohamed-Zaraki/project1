"""inspect_db.py - print what is stored in weather.db (read-only).
Usage:  python inspect_db.py [weather.db]
"""
import sys
import sqlite3
from pathlib import Path

db_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "weather.db"
if not db_path.exists():
    sys.exit(f"Database not found: {db_path}")

con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)     # read-only: cannot change anything
con.row_factory = sqlite3.Row
q = lambda sql, p=(): [dict(r) for r in con.execute(sql, p)]


def show(title, rows, width=26):
    print(f"\n--- {title}")
    if not rows:
        print("   (empty)")
        return
    cols = list(rows[0])
    print("   " + " | ".join(c[:width].ljust(12) for c in cols))
    for r in rows:
        print("   " + " | ".join(str(round(v, 3) if isinstance(v, float) else v)[:width].ljust(12) for v in r.values()))


print(f"DATABASE: {db_path}  ({db_path.stat().st_size / 1e6:.1f} MB)")

print("\n=== 1. TABLES AND ROW COUNTS")
for t in [r["name"] for r in q("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]:
    print(f"   {t.ljust(20)} {q(f'SELECT count(*) n FROM {t}')[0]['n']} rows")

show("2. REPORTS (one row per analysis run)",
     q("SELECT report_id, dataset, n_rows, n_cols, date_column FROM reports"))

rid = q("SELECT report_id FROM reports ORDER BY generated_at DESC LIMIT 1")
if not rid:
    sys.exit()
rid = rid[0]["report_id"]

show("3. SECTIONS", q("SELECT position, name, substr(description,1,60) AS description FROM sections "
                       "WHERE report_id=? ORDER BY position", (rid,)))
show("4. PLOTS (image size = bytes stored in the database)",
     q("SELECT section, name, length(image) AS image_bytes FROM plots WHERE report_id=? ORDER BY position", (rid,)))
show("5. MISSING VALUES (only columns with missing data)",
     q("SELECT feature, count, percent FROM missing_columns WHERE report_id=? AND count>0", (rid,)))
show("6. OUTLIER STATS",
     q("SELECT feature, iqr_outliers, iqr_percent, z_outliers, z_percent FROM outlier_stats "
       "WHERE report_id=? ORDER BY iqr_percent DESC", (rid,)))
show("7. NOISE VERDICTS",
     q("SELECT feature, verdict, noise_to_signal AS nsr, spike_percent, out_of_range, has_noise, has_errors "
       "FROM noise_features WHERE report_id=? ORDER BY noise_to_signal DESC", (rid,)))
show("8. STRONGEST CORRELATIONS",
     q("SELECT feature_a, feature_b, pearson, strength FROM correlation_pairs WHERE report_id=? "
       "ORDER BY abs(pearson) DESC LIMIT 5", (rid,)))

print("\n--- 9. INSIGHTS (the sentences the website will display)")
for s in q("SELECT section, text FROM insights WHERE report_id=? ORDER BY section, position", (rid,)):
    print(f"   [{s['section']}] {s['text']}")