# Weather dataset EDA (MVC)

This analysis is built for the project's `Datasets/weather-dataset/weatherHistory.csv` file (hourly Dark Sky weather history). It is not intended as a generic weather dataset loader. It is diagnostic only: it does not modify the CSV, remove rows, impute values, or create a cleaned dataset.

## MVC responsibilities

- `model.py` loads this CSV schema, computes the EDA and data-quality results, and generates chart artifacts.
- `controller.py` runs the workflow and coordinates saving model output and the report view.
- `view.py` formats the report dictionary as a presentation-ready Markdown document; it does not calculate statistics.
- `database.py` stores report JSON and plot image bytes in SQLite and exposes read functions for other views.
- `mysql_database.py` optionally imports the weather observations into a MySQL table so they can be edited in phpMyAdmin and analyzed again.
- `app.py` is a temporary Streamlit inspector for reports and charts in the database. Your friend can replace it with a different view while keeping `database.py` as the data access layer.

## Run

Install the analysis dependencies in your Python environment:

```powershell
& "C:\Users\Moham\AppData\Local\Programs\Python\Python313\python.exe" -m pip install pandas numpy matplotlib seaborn scipy streamlit
```

Then run from this directory:

```powershell
& "C:\Users\Moham\AppData\Local\Programs\Python\Python313\python.exe" controller.py
```

The default output is `eda_output/`: `report.json`, `db_documents.json`, `presentation_report.md`, and chart images under `plots/`. Reports and plot images are also saved in the SQLite database `eda_reports.sqlite3` in this project directory. To choose paths:

```powershell
& "C:\Users\Moham\AppData\Local\Programs\Python\Python313\python.exe" controller.py --dataset "Datasets/weather-dataset/weatherHistory.csv" --output "eda_output" --database "eda_reports.sqlite3"
```

## Inspect saved reports and plots

After running the controller, start Streamlit from this project directory:

```powershell
& "C:\Users\Moham\AppData\Local\Programs\Python\Python313\python.exe" -m streamlit run app.py
```

The page lets you select a saved report and inspect its dataset description, data-quality checks, outliers, noise, correlations, insights, and plots. The app only reads the report database; it does not change the source CSV. To rerun the analysis and add a report to SQLite, run `controller.py` again.

For your friend's view, `database.list_reports(db_path)` lists saved reports and `database.load_report(report_id, db_path)` returns a report dictionary plus its plot metadata and image bytes.

## Use phpMyAdmin to remove a weather row

The report database above remains SQLite. phpMyAdmin cannot edit SQLite files; it edits MySQL/MariaDB tables. To remove an observation through phpMyAdmin, import the CSV into a MySQL/MariaDB table once. This keeps the original CSV untouched.

1. Start MySQL/MariaDB (for example through XAMPP) and open phpMyAdmin. Create a database named `weather_eda`.
2. In the same PowerShell terminal, set the connection values for your MySQL account. Use your actual password; do not commit it to the project:

```powershell
$env:MYSQL_HOST = "127.0.0.1"
$env:MYSQL_PORT = "3306"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "your_mysql_password"
$env:MYSQL_DATABASE = "weather_eda"
```

3. Import the source CSV once. This creates a `weather_records` table with a stable `source_row` key:

```powershell
& "C:\Users\Moham\AppData\Local\Programs\Python\Python313\python.exe" mysql_database.py import
```

4. In phpMyAdmin, open `weather_eda` → `weather_records`, find the observation, and use **Delete** on its row. Keep the `source_row` value to identify rows reliably. The importer will not run again once marked complete, so later imports do not undo your deletion.
5. Re-run the analysis from the edited MySQL table and then view the new report in Streamlit:

```powershell
& "C:\Users\Moham\AppData\Local\Programs\Python\Python313\python.exe" controller.py --source mysql
& "C:\Users\Moham\AppData\Local\Programs\Python\Python313\python.exe" -m streamlit run app.py
```

`--source mysql` reads the current rows in `weather_records`, so a deleted row is absent from the next report. Without that option, the controller analyzes the original CSV again.

## Analysis included

The report includes the data types/non-null counts (`info`), first rows (`head`), descriptive statistics (`describe`), missing values, exact duplicate rows, IQR and Z-score outlier flags, robust temporal noise and spike checks, monthly trends, Pearson and Spearman correlation, distributions, and plots. Outliers are review candidates: seasonal extremes should not be deleted just because a generic threshold flags them.

### Humidity equals zero

In this file, `Humidity` is relative humidity stored as a fraction from 0 to 1, so `0.89` means 89%. A value of exactly zero is physically possible under exceptionally dry conditions, but it is unusual enough to review. The report counts these rows and gives temperature, precipitation type, summary label, and month context when available. That context can identify suspicious clusters, but it cannot prove a sensor failure. The analysis leaves every value and row unchanged and only reports the issue.

`Pressure (millibars)` values at or below zero are separately flagged because zero is not a plausible surface pressure and may be a missing-value sentinel. `Loud Cover` is constant in the provided schema and therefore has no predictive value.

The noise-to-signal method assumes observations are ordered in time and approximately evenly spaced. Wind bearing is skipped by the linear noise check because degrees are circular. Correlations use stored values (including flagged sentinel values), so the pressure zeros can affect pressure correlations. Interpret spike flags alongside timestamp gaps and the plotted local examples: an isolated weather transition can look like a sensor spike. A long run of zero visibility may mean a sensor issue or genuinely severe fog and needs context. Correlation is association, not causation, and weather seasonality can create strong correlations between otherwise indirectly related variables.
