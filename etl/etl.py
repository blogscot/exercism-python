def transform(values):
    return {v.lower(): key for key, vals in values.items() for v in vals}
