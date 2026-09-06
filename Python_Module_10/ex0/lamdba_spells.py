mages = [
    {'name': 'Alex', 'power': 40},
    {'name': 'Riley', 'power': 90},
    {'name': 'Jordan', 'power': 65},
]


get_power = lambda mage: mage['power']
print(get_power(mages[0]))

sorted(mages, key=get_power)
sorted(mages, key=lambda mage: mage['power'])



def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'],
        reverse=True,
    )

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(
        filter(
            lambda mage: 
        )
    )

data = [
    {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
    {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
]
print(artifact_sorter(data))