import yaml

with open('test.yml') as f:
    data = yaml.safe_load(f)

print(data['mystery-inc'][0]['name'])   # Fred
for member in data['mystery-inc']:
    print(f"{member['name']}: {member['role']}")
