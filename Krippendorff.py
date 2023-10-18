import krippendorff
data = list()

data.append(df['21110039'].tolist())
data.append(df['21110098'].tolist())
data.append(df['21110129'].tolist())

result = krippendorff.alpha(reliability_data = data, level_of_measurement = "ordinal" , value_domain = ["positive" , "negative" , "neutral"])

print(round(result , 4))
