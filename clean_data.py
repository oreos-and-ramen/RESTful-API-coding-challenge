default_keeps = ["latitude","longitude","daily"]

def clean_data(raw_data, info_keep=default_keeps):
  clean_data = {}

  for k in raw_data:
    if k in info_keep:
      clean_data[k] = raw_data[k]

  return clean_data
