# Weather dataset analysis: weatherHistory.csv

Generated: 2026-10-21T20:06:27

## Dataset overview

- Rows: 96,453
- Columns: 12
- Cleaning performed: no
- Date column: Formatted Date
- Numeric features: Temperature (C), Apparent Temperature (C), Humidity, Wind Speed (km/h), Wind Bearing (degrees), Visibility (km), Pressure (millibars)
- Categorical features: Summary, Precip Type, Daily Summary

### `df.info()`

Memory usage: 32136.76 KB.

| name | dtype | non_null | n_unique |
| --- | --- | --- | --- |
| Formatted Date | object | 96453 | 96429 |
| Summary | object | 96453 | 27 |
| Precip Type | object | 95936 | 2 |
| Temperature (C) | float64 | 96453 | 7574 |
| Apparent Temperature (C) | float64 | 96453 | 8984 |
| Humidity | float64 | 96453 | 90 |
| Wind Speed (km/h) | float64 | 96453 | 2484 |
| Wind Bearing (degrees) | int64 | 96453 | 360 |
| Visibility (km) | float64 | 96453 | 949 |
| Loud Cover | int64 | 96453 | 1 |
| Pressure (millibars) | float64 | 96453 | 4979 |
| Daily Summary | object | 96453 | 214 |

### `df.head()`

| Formatted Date | Summary | Precip Type | Temperature (C) | Apparent Temperature (C) | Humidity | Wind Speed (km/h) | Wind Bearing (degrees) | Visibility (km) | Loud Cover | Pressure (millibars) | Daily Summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2006-04-01 00:00:00.000 +0200 | Partly Cloudy | rain | 9.472222222 | 7.388888889 | 0.89 | 14.1197 | 251 | 15.8263 | 0 | 1015.13 | Partly cloudy throughout the day. |
| 2006-04-01 01:00:00.000 +0200 | Partly Cloudy | rain | 9.355555556 | 7.227777778 | 0.86 | 14.2646 | 259 | 15.8263 | 0 | 1015.63 | Partly cloudy throughout the day. |
| 2006-04-01 02:00:00.000 +0200 | Mostly Cloudy | rain | 9.377777778 | 9.377777778 | 0.89 | 3.9284 | 204 | 14.9569 | 0 | 1015.94 | Partly cloudy throughout the day. |
| 2006-04-01 03:00:00.000 +0200 | Partly Cloudy | rain | 8.288888889 | 5.944444444 | 0.83 | 14.1036 | 269 | 15.8263 | 0 | 1016.41 | Partly cloudy throughout the day. |
| 2006-04-01 04:00:00.000 +0200 | Mostly Cloudy | rain | 8.755555556 | 6.977777778 | 0.83 | 11.0446 | 259 | 15.8263 | 0 | 1016.51 | Partly cloudy throughout the day. |
| 2006-04-01 05:00:00.000 +0200 | Partly Cloudy | rain | 9.222222222 | 7.111111111 | 0.85 | 13.9587 | 258 | 14.9569 | 0 | 1016.66 | Partly cloudy throughout the day. |
| 2006-04-01 06:00:00.000 +0200 | Partly Cloudy | rain | 7.733333333 | 5.522222222 | 0.95 | 12.3648 | 259 | 9.982 | 0 | 1016.72 | Partly cloudy throughout the day. |
| 2006-04-01 07:00:00.000 +0200 | Partly Cloudy | rain | 8.772222222 | 6.527777778 | 0.89 | 14.1519 | 260 | 9.982 | 0 | 1016.84 | Partly cloudy throughout the day. |
| 2006-04-01 08:00:00.000 +0200 | Partly Cloudy | rain | 10.82222222 | 10.82222222 | 0.82 | 11.3183 | 259 | 9.982 | 0 | 1017.37 | Partly cloudy throughout the day. |
| 2006-04-01 09:00:00.000 +0200 | Partly Cloudy | rain | 13.77222222 | 13.77222222 | 0.72 | 12.5258 | 279 | 9.982 | 0 | 1017.22 | Partly cloudy throughout the day. |

### Numeric summary

| feature | count | mean | std | min | 25% | 50% | 75% | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Temperature (C) | 96453.0 | 11.9326784375 | 9.5515463207 | -21.82222222 | 4.688888889 | 12.0 | 18.83888889 | 39.90555556 |
| Apparent Temperature (C) | 96453.0 | 10.8550288742 | 10.6968473921 | -27.71666667 | 2.311111111 | 12.0 | 18.83888889 | 39.34444444 |
| Humidity | 96453.0 | 0.7348989663 | 0.1954727391 | 0.0 | 0.6 | 0.78 | 0.89 | 1.0 |
| Wind Speed (km/h) | 96453.0 | 10.8106401408 | 6.9135710126 | 0.0 | 5.8282 | 9.9659 | 14.1358 | 63.8526 |
| Wind Bearing (degrees) | 96453.0 | 187.5092324759 | 107.3834283807 | 0.0 | 116.0 | 180.0 | 290.0 | 359.0 |
| Visibility (km) | 96453.0 | 10.3473249292 | 4.1921231914 | 0.0 | 8.3398 | 10.0464 | 14.812 | 16.1 |
| Pressure (millibars) | 96453.0 | 1003.2359558541 | 116.9699056826 | 0.0 | 1011.9 | 1016.45 | 1021.09 | 1046.38 |
| Loud Cover | 96453.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

### Categorical summary

| feature | count | unique | top | freq |
| --- | --- | --- | --- | --- |
| Summary | 96453 | 27 | Partly Cloudy | 31733 |
| Precip Type | 95936 | 2 | rain | 85224 |
| Daily Summary | 96453 | 214 | Mostly cloudy throughout the day. | 20085 |


## Missing values and duplicates

Missing cells: 517.

| name | count | percent |
| --- | --- | --- |
| Formatted Date | 0 | 0.0 |
| Summary | 0 | 0.0 |
| Precip Type | 517 | 0.536 |
| Temperature (C) | 0 | 0.0 |
| Apparent Temperature (C) | 0 | 0.0 |
| Humidity | 0 | 0.0 |
| Wind Speed (km/h) | 0 | 0.0 |
| Wind Bearing (degrees) | 0 | 0.0 |
| Visibility (km) | 0 | 0.0 |
| Loud Cover | 0 | 0.0 |
| Pressure (millibars) | 0 | 0.0 |
| Daily Summary | 0 | 0.0 |

Exact duplicate rows: 24.

Key findings:
- 'Precip Type' has 517 missing values (0.536%) - categorical; recorded for review only (no values are filled or rows removed).
- 24 fully duplicated rows (0.025%); reported only, with duplicate rows retained.


## Weather-specific checks

### Humidity

```json
{
  "feature": "Humidity",
  "meaning": "relative humidity as a fraction (0 to 1)",
  "zero_count": 22,
  "zero_percent": 0.0228,
  "out_of_range_count": 0,
  "overall_median": 0.78,
  "zero_readings_context": {
    "Temperature (C)": {
      "median": -15.0,
      "min": -17.77777778,
      "max": 1.111111111
    },
    "Precip Type": {
      "top_values": {
        "snow": 21,
        "rain": 1
      }
    },
    "Summary": {
      "top_values": {
        "Foggy": 8,
        "Overcast": 6,
        "Clear": 4,
        "Partly Cloudy": 3,
        "Mostly Cloudy": 1
      }
    },
    "UTC_month_counts": {
      "1": 1,
      "2": 18,
      "12": 3
    }
  }
}
```

### Pressure (millibars)

```json
{
  "feature": "Pressure (millibars)",
  "zero_count": 1288,
  "nonpositive_count": 1288,
  "zero_percent": 1.3354
}
```

Key findings:
- Humidity is recorded as a fraction: 22 rows (0.0228%) are exactly 0. A true 0% relative humidity is physically possible but exceptionally dry; treat these as suspect readings and inspect their weather/date context. They are reported for review only; this analysis does not replace readings, impute values, or remove rows.
- Context: 21 of 22 zero-humidity records are labeled snow; their median temperature is -15.0 °C. This suggests a cold-weather cluster worth investigating; it does not establish that the measurements are correct.
- Pressure has 1,288 nonpositive readings. Zero millibars is not a plausible surface weather observation; investigate whether it is a missing-value sentinel before analysis or modeling.
- Loud Cover is constant (all observed values are 0 in this dataset), so it carries no predictive information and is excluded from correlation and modeling features.


## Outlier screening

| feature | physically_invalid | iqr_outliers | iqr_percent | z_outliers | z_percent |
| --- | --- | --- | --- | --- | --- |
| Temperature (C) | 0 | 44 | 0.046 | 39 | 0.04 |
| Apparent Temperature (C) | 0 | 22 | 0.023 | 40 | 0.041 |
| Humidity | 0 | 46 | 0.048 | 28 | 0.029 |
| Wind Speed (km/h) | 0 | 3020 | 3.131 | 1208 | 1.252 |
| Wind Bearing (degrees) | 0 | 0 | 0.0 | 0 | 0.0 |
| Visibility (km) | 0 | 0 | 0.0 | 0 | 0.0 |
| Pressure (millibars) | 1288 | 3284 | 3.451 | 721 | 0.758 |


Key findings:
- Most outlier-prone feature: 'Pressure (millibars)' (3284 IQR outliers, 3.451%).
- No IQR outliers in: ['Wind Bearing (degrees)', 'Visibility (km)'].


## Noise diagnostics

| feature | verdict | noise_to_signal | snr_db | spikes | out_of_range | stuck_sensor |
| --- | --- | --- | --- | --- | --- | --- |
| Temperature (C) | negligible | 0.042344042864639796 | 27.456359620115137 | 1301 | 0 | False |
| Apparent Temperature (C) | negligible | 0.04799638140158887 | 26.365813906813603 | 1462 | 0 | False |
| Humidity | low | 0.11664236870396097 | 18.603380065709928 | 1077 | 0 | False |
| Wind Speed (km/h) | moderate | 0.3291304047150523 | 9.15469694778582 | 714 | 0 | False |
| Visibility (km) | moderate | 0.1749635530559416 | 15.006023505691836 | 6027 | 0 | True |
| Pressure (millibars) | negligible | 0.019870492013740658 | 34.034112492074385 | 2313 | 1288 | False |


Noise check skipped for Wind Bearing (degrees): circular direction; linear noise and spike distances are not valid for angles.
Key findings:
- YES - noise detected in 6 of 6 features: ['Temperature (C)', 'Apparent Temperature (C)', 'Humidity', 'Wind Speed (km/h)', 'Visibility (km)', 'Pressure (millibars)'].
- Noisiest: 'Wind Speed (km/h)' (noise/signal 0.33); cleanest: 'Pressure (millibars)' (0.02).
- 'Temperature (C)': 1301 isolated spikes (1.349%).
- 'Apparent Temperature (C)': 1462 isolated spikes (1.516%).
- 'Humidity': 1077 isolated spikes (1.117%).
- 'Wind Speed (km/h)': moderate random fluctuation (noise is 33% of the signal's std); 714 isolated spikes (0.74%).
- 'Visibility (km)': moderate random fluctuation (noise is 17% of the signal's std); 6027 isolated spikes (6.249%); stuck at 0 for 193 consecutive readings.
- 'Pressure (millibars)': 2313 isolated spikes (2.431%); 1288 physically impossible values (valid range 850 to 1090).
- These are diagnostic flags only. No readings are changed, imputed, or removed by this workflow.


## Seasonal and monthly trends

Key findings:
- 'Temperature (C)' averages highest in July (22.97) and lowest in January (0.82).
- 'Humidity' averages highest in December (0.87) and lowest in August (0.64).
- Most variable month for 'Temperature (C)': 2013-04 (std 7.22).
- Most variable month for 'Humidity': 2015-08 (std 0.23).


## Correlation and relationships

| a | b | pearson | spearman | strength | direction |
| --- | --- | --- | --- | --- | --- |
| Temperature (C) | Apparent Temperature (C) | 0.9926285641920605 | 0.9959740439738328 | very strong | positive |
| Temperature (C) | Humidity | -0.6322546750264331 | -0.588105803952852 | strong | negative |
| Apparent Temperature (C) | Humidity | -0.6025709955719697 | -0.572550687569767 | strong | negative |
| Temperature (C) | Visibility (km) | 0.39284657172499376 | 0.3944419715867043 | weak | positive |
| Apparent Temperature (C) | Visibility (km) | 0.38171847046456714 | 0.37867550449645215 | weak | positive |
| Humidity | Visibility (km) | -0.3691725005980121 | -0.4320750289143059 | weak | negative |
| Humidity | Wind Speed (km/h) | -0.224951455879778 | -0.2619800711588459 | weak | negative |
| Wind Speed (km/h) | Visibility (km) | 0.10074928406778529 | 0.10085636219977533 | negligible | positive |
| Visibility (km) | Pressure (millibars) | 0.059818381034750526 | -0.1307559436501564 | negligible | positive |
| Apparent Temperature (C) | Wind Speed (km/h) | -0.05664969828939087 | -0.03916168516841837 | negligible | negative |
| Wind Speed (km/h) | Pressure (millibars) | -0.049262805511162334 | -0.22778668725498386 | negligible | negative |
| Temperature (C) | Wind Speed (km/h) | 0.00895696834398354 | 0.016890057674928377 | negligible | positive |
| Humidity | Pressure (millibars) | 0.005454263261942867 | 0.042993243719233 | negligible | positive |
| Temperature (C) | Pressure (millibars) | -0.005447106151535067 | -0.3033460419169909 | negligible | negative |
| Apparent Temperature (C) | Pressure (millibars) | -0.00021899978575568946 | -0.2826207302485079 | negligible | negative |


Key findings:
- Very strong positive link between 'Temperature (C)' and 'Apparent Temperature (C)' (r = 0.99).
- Strong negative link between 'Temperature (C)' and 'Humidity' (r = -0.63).
- Strong negative link between 'Apparent Temperature (C)' and 'Humidity' (r = -0.60).
- 'Temperature (C)' and 'Apparent Temperature (C)' are nearly redundant (|r| >= 0.9) - keep one to avoid multicollinearity in a model.
- 'Visibility (km)' vs 'Pressure (millibars)': Pearson 0.06 but Spearman -0.13 - the relationship is monotonic but not linear (or distorted by outliers/zeros).
- 'Wind Speed (km/h)' vs 'Pressure (millibars)': Pearson -0.05 but Spearman -0.23 - the relationship is monotonic but not linear (or distorted by outliers/zeros).
- 'Temperature (C)' vs 'Pressure (millibars)': Pearson -0.01 but Spearman -0.30 - the relationship is monotonic but not linear (or distorted by outliers/zeros).
- Almost independent of every other feature: ['Pressure (millibars)'].
- Average 'Apparent Temperature (C)' is highest for 'Partly Cloudy' (15.39) and lowest for 'Foggy' (-0.21).
- Average 'Humidity' is highest for 'Foggy' (0.95) and lowest for 'Breezy and Partly Cloudy' (0.55).


## Distribution shapes

Key findings:
- 'Temperature (C)' is roughly symmetric with 2 peak(s) - multimodal, probably mixed regimes (day/night or seasons).
- 'Apparent Temperature (C)' is roughly symmetric with 2 peak(s) - multimodal, probably mixed regimes (day/night or seasons).
- 'Humidity' is left-skewed with 1 peak(s).
- 'Wind Speed (km/h)' is right-skewed with 3 peak(s) - multimodal, probably mixed regimes (day/night or seasons).
- 'Wind Bearing (degrees)' is roughly symmetric with 3 peak(s) - multimodal, probably mixed regimes (day/night or seasons).
- 'Visibility (km)' is roughly symmetric with 1 peak(s).
- 'Pressure (millibars)' is left-skewed with 1 peak(s).

## Figures

- [Missing values per column](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\missing_values.png)
- [Box plots of all numeric features](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\boxplots.png)
- [Noise level per feature](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\noise_levels.png)
- [Noise check - Temperature (C)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\noise_view_temperature_c.png)
- [Noise check - Humidity](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\noise_view_humidity.png)
- [Noise check - Wind Speed (km/h)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\noise_view_wind_speed_km_h.png)
- [Monthly band - Temperature (C)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\monthly_band_temperature_c.png)
- [Monthly band - Apparent Temperature (C)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\monthly_band_apparent_temperature_c.png)
- [Monthly band - Humidity](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\monthly_band_humidity.png)
- [Monthly band - Wind Speed (km/h)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\monthly_band_wind_speed_km_h.png)
- [Monthly band - Wind Bearing (degrees)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\monthly_band_wind_bearing_degrees.png)
- [Monthly band - Visibility (km)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\monthly_band_visibility_km.png)
- [Monthly band - Pressure (millibars)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\monthly_band_pressure_millibars.png)
- [Month-by-month trend - Temperature (C)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\month_lines_temperature_c.png)
- [Month-by-month trend - Humidity](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\month_lines_humidity.png)
- [Pearson correlation heatmap](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\correlation_heatmap.png)
- [Scatter Temperature (C) vs Apparent Temperature (C)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\scatter_temperature_c__apparent_temperature_c.png)
- [Scatter Temperature (C) vs Humidity](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\scatter_temperature_c__humidity.png)
- [Apparent Temperature (C) distribution by Summary](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\facet_apparent_temperature_c_by_summary.png)
- [Humidity distribution by Summary](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\facet_humidity_by_summary.png)
- [KDE of Temperature (C)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\kde_temperature_c.png)
- [KDE of Apparent Temperature (C)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\kde_apparent_temperature_c.png)
- [KDE of Humidity](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\kde_humidity.png)
- [KDE of Wind Speed (km/h)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\kde_wind_speed_km_h.png)
- [KDE of Wind Bearing (degrees)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\kde_wind_bearing_degrees.png)
- [KDE of Visibility (km)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\kde_visibility_km.png)
- [KDE of Pressure (millibars)](C:\Users\Moham\Documents\GitHub\Sumestre_7_TP\ML_SUM_7\Projet1\eda_output\plots\kde_pressure_millibars.png)

## Interpretation notes

IQR and Z-score flags identify unusual values; they do not prove data errors. Weather extremes can be valid.
Correlation describes association and does not establish causation. This report detects data issues only; it does not alter or clean the source dataset.
