def parse(raw):

    raw = raw.strip()

    part = raw.split(",")

    if len(part) != 3:
        return None

    return {
        "mo": part[0],
        "test": part[1],
        "value": float(part[2])
    }