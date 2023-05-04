import json
from collections import defaultdict

# Step 1: read impressions.json and clicks.json
with open("input_files/impressions.json") as f:
    impressions = json.load(f)

with open("input_files/clicks.json") as f:
    clicks = json.load(f)

# Step 2: process data
impressions_dict = {i.get("id", ""): i for i in impressions}
clicks_per_impression = defaultdict(list)

for click in clicks:
    impression_id = click.get("impression_id", "")
    if impression_id in impressions_dict:
        clicks_per_impression[impression_id].append(click.get("revenue", 0))

results = []
for impression_id, clicks_list in clicks_per_impression.items():
    impression = impressions_dict.get(impression_id, {})
    app_id = impression.get("app_id", "")
    country_code = impression.get("country_code", "")
    clicks_count = len(clicks_list)
    revenue_sum = sum(clicks_list)
    results.append({
        "app_id": app_id,
        "country_code": country_code,
        "impressions": 1,
        "clicks": clicks_count,
        "revenue": revenue_sum
    })

# Step 3: write results to impressions_result.json
with open("output_files/impressions_result.json", "w") as f:
    json.dump(results, f, indent=2)

# Step 4: read impressions_result.json
with open("impressions_result.json") as f:
    results = json.load(f)

# Step 5: aggregate by app_id and country_code
aggregated_results = defaultdict(lambda: defaultdict(lambda: {"impressions": 0, "clicks": 0, "revenue": 0}))
for result in results:
    app_id = result.get("app_id", "")
    country_code = result.get("country_code", "")
    impressions_count = result.get("impressions", 0)
    clicks_count = result.get("clicks", 0)
    revenue_sum = result.get("revenue", 0)
    aggregated_results[app_id][country_code]["impressions"] += impressions_count
    aggregated_results[app_id][country_code]["clicks"] += clicks_count
    aggregated_results[app_id][country_code]["revenue"] += revenue_sum

# Step 6: calculate recommended_advertiser_ids
recommended_advertisers = []
for app_id, countries in aggregated_results.items():
    for country_code, metrics in countries.items():
        impressions_count = metrics.get("impressions", 0)
        advertisers_revenue = defaultdict(float)
        for impression in impressions:
            if impression.get("app_id", "") == app_id and impression.get("country_code", "") == country_code:
                advertiser_id = impression.get("advertiser_id", "")
                revenue = clicks_per_impression.get(impression.get("id", ""), [])
                if len(revenue) > 0:
                    advertisers_revenue[advertiser_id] += sum(revenue) / len(revenue)
        recommended_advertisers_ids = sorted(advertisers_revenue, key=advertisers_revenue.get, reverse=True)[:5]
        recommended_advertisers.append({
            "app_id": app_id,
            "country_code": country_code,
            "recommended_advertiser_ids": recommended_advertisers_ids
        })

# Step 7: write results to recommendations.json
with open("output_files/recommendations.json", "w") as f:
    json.dump(recommended_advertisers, f, indent=2)