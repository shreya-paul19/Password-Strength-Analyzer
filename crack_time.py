def estimate_crack_time(entropy):

    guesses_per_second = 1_000_000_000

    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} Seconds"

    elif seconds < 3600:
        return f"{seconds / 60:.2f} Minutes"

    elif seconds < 86400:
        return f"{seconds / 3600:.2f} Hours"

    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} Days"

    else:
        years = seconds / 31536000

        if years > 1_000_000:
            return f"{years / 1_000_000:.2f} Million Years"

        return f"{years:.2f} Years"