# Verve Data Engineering Challenge

This repository contains a Python solution for the Verve Data Engineering Challenge. The challenge consists of processing two lists of file names containing impression and click events and generating metrics by app and country dimensions.

## Requirements

- Python 3.x

## Usage

The solution is implemented as a command line application.

```bash
python main.py
```

The application will read the input files, calculate the metrics, and save the output to a JSON file.

## Metrics

The following metrics are calculated for each app and country combination:

- Count of impressions
- Count of clicks
- Sum of revenue

## Output

The output file is a JSON file containing a list of dictionaries with the following fields:

- `app_id`: an identifier of the application
- `country_code`: a 2-letter code for the country
- `impressions`: the count of impressions
- `clicks`: the count of clicks
- `revenue`: the sum of revenue

```json
[
  {
    "app_id": 1,
    "country_code": "US",
    "impressions": 102,
    "clicks": 12,
    "revenue": 10.2
  },
  {
    "app_id": 1,
    "country_code": "GB",
    "impressions": 52,
    "clicks": 4,
    "revenue": 3.12
  },
  ...
]
```

In addition, the application also calculates the top 5 advertisers with the highest revenue per impression rate for each app and country combination. The recommended advertisers are included in the output under the field `recommended_advertiser_ids`.

```json
[
  {
    "app_id": 1,
    "country_code": "US",
    "recommended_advertiser_ids": [32, 12, 45, 4, 1]
  },
  {
    "app_id": 1,
    "country_code": "GB",
    "recommended_advertiser_ids": [12, 45, 32, 1, 4]
  },
  ...
]
```

## Author

This solution was developed by Savelii Moiseenko. If you have any questions or feedback, feel free to contact me at savelii.moiseenko@gmail.com.
