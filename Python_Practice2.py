counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

    for county in counties:


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{'county':'Arapahoe', 'registered_voters': 422829}, {'county':'Denver,' 'registered_voters': 463353}, {'county':'Jefferson', 'registered_voters': 432438}]
for county, registered_voters in voting_data.items():
    print(f"{county} county has {voters:,} registered voters.")