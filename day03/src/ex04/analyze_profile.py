import pstats

if __name__ == "__main__":
    stats = pstats.Stats('profile_stats')
    stats.sort_stats('cumulative').print_stats(5)