from socialscan.util import Platforms, sync_execute_queries


with open("target_email.txt", "r") as f:
    queries = [line.strip() for line in f.readlines()]


platforms = [Platforms.TWITTER, Platforms.INSTAGRAM]


results = sync_execute_queries(queries, platforms)

with open("hasil_osint_email.txt", "w") as file:
    for result in results:
        file.write(f"{result.query} on {result.platform}: {result.message} "
                   f"(Success: {result.success}, Valid: {result.valid}, Available: {result.available})\n")

print("Hasil tersimpan di hasil_osint_email.txt")
