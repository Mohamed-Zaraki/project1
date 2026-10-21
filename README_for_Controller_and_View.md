# Weather EDA – Model handover (for Controller + View)

The Model is finished. It analysed `weatherHistory.csv` and stored every result in **`weather.db`** (SQLite).
You do **not** need to re-run the analysis, the CSV, pandas or matplotlib. You only need:

```
weather_db.py     # the reader (uses only the Python standard library)
weather.db        # the data (results + 29 plots stored as PNG images)
```

Put both in the same folder and open the database with a path tied to the script's folder:

```python
from pathlib import Path
from weather_db import WeatherDB

db  = WeatherDB(Path(__file__).resolve().parent / "weather.db")
rid = db.latest_report_id()
```

## What the Controller calls

| Call | Returns |
|---|---|
| `db.latest_report_id()` | id of the newest report (string) |
| `db.list_reports()` | list of `{report_id, dataset, generated_at, n_rows, n_cols, date_column}` |
| `db.get_report(rid)` | the whole report as a dict (images included as base64) |
| `db.get_report(rid, include_images=False)` | same, without base64 (small and fast) |
| `db.get_section(rid, "noise")` | one section only (load tabs lazily) |
| `db.get_plot_png(rid, "correlation_heatmap")` | raw PNG bytes -> return with `Content-Type: image/png` |
| `db.get_plot_base64(rid, name)` | base64 string -> `<img src="data:image/png;base64,...">` |
| `db.query("SELECT ...")` | any read-only SQL, list of dicts |

Recommended: load the report with `include_images=False` for the page data, and serve each image through
its own URL with `get_plot_png` (images are 17-360 KB each).

## Report structure (what the View displays)

`report` has: `meta`, 7 sections, and `plots`. **Every section** has:

- `description` – one sentence explaining the section (show it as a subtitle)
- `insights` – list of ready-to-display sentences (show them as bullet points)
- `plots` – names of the plots that belong to this section (use with `get_plot_png`)

Sections, in display order, and their main data:

| Section | Main content |
|---|---|
| `description` | `info.columns` (dtype, non_null, n_unique), `head` (10 rows), `describe_numeric`, `describe_categorical`, `constant_columns` |
| `missing_duplicates` | `missing.columns` [{name, count, percent}], `duplicates` {count, percent} |
| `outliers` | `features` [{feature, q1, q3, lower_fence, upper_fence, iqr_outliers, iqr_percent, z_outliers, z_percent}] |
| `noise` | `dataset_summary` {has_noise, has_errors, noisy_features, error_features}, `features` [{feature, verdict, noise_to_signal, snr_db, spikes, spike_percent, out_of_range, has_noise, has_errors, noise_reasons, error_reasons}], `method` (definitions), `thresholds` |
| `monthly_trends` | `monthly_stats` {feature: [{month, mean, low, high, std}]}, `seasonality` {feature: {month_name: mean}} |
| `correlation` | `pearson`, `spearman` (matrices), `pairs` [{a, b, pearson, spearman, strength, direction}], `by_category` |
| `kde` | `features` [{feature, mean, median, std, skew, kurtosis, n_peaks, shape}] |

Noise `verdict` values: `negligible`, `low`, `moderate`, `high` (suggested colours: green, light green, orange, red).

Each plot entry in `report["plots"]`: `{name, title, section, mime, file, base64?}`.
Show plots grouped by `section`, with `title` as the caption.

## Tables for direct SQL (e.g. a "Noise" table or filters)

```sql
SELECT feature, verdict, noise_to_signal, spike_percent, has_noise, has_errors FROM noise_features;
SELECT feature_a, feature_b, pearson, strength FROM correlation_pairs ORDER BY abs(pearson) DESC;
SELECT feature, count, percent FROM missing_columns WHERE count > 0;
SELECT feature, iqr_outliers, iqr_percent, z_outliers FROM outlier_stats;
SELECT section, name, title FROM plots;           -- list of images to show
```

Run `python inspect_db.py` to print everything stored in the database.

## Minimal example (Flask)

```python
from pathlib import Path
from flask import Flask, jsonify, Response, abort
from weather_db import WeatherDB

app = Flask(__name__)
db  = WeatherDB(Path(__file__).resolve().parent / "weather.db")

@app.route("/api/report")
def report():
    return jsonify(db.get_report(db.latest_report_id(), include_images=False))

@app.route("/api/section/<name>")
def section(name):
    try:
        return jsonify(db.get_section(db.latest_report_id(), name))
    except KeyError:
        abort(404)

@app.route("/plots/<name>.png")
def plot(name):
    try:
        return Response(db.get_plot_png(db.latest_report_id(), name), mimetype="image/png")
    except KeyError:
        abort(404)
```
(`get_section` / `get_plot_png` raise `KeyError` for an unknown name, so catch it and answer 404.)
The page then loads `/api/report` and uses `<img src="/plots/<name>.png">`.

## Notes
- `None`/`null` in the data means "not defined" (e.g. a missing value or an undefined ratio).
- The Model is read-only for you: never write to `weather.db`.
- To analyse a new CSV, the Model owner runs `python weather_db.py new_file.csv`; the new report is added and
  `latest_report_id()` will return it.
