frnd = ['James', 'Lily', 'Harry', 'Sirius', 'Severus']
time_last_seen = [10,2,3,20,1]

longTimers = { frnd[i]:time_last_seen[i] for i in range(0, len(frnd)) if time_last_seen[i]>8  };
print(longTimers);

LT_via_zip = zip(frnd, time_last_seen);
for eaFrd, eaTime in LT_via_zip:
    print(f"The Friend '{eaFrd}' was last seen since {eaTime} years ");