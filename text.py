from randomText import RandomTextClient

client = RandomTextClient(api_key='api_key')
df = client.address.get_random(size=1)
print(df.head(2))
