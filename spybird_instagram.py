import trio
import httpx
import os
from holehe.modules.social_media.instagram import instagram

async def main():

    with open("target_email.txt", "r") as f:
        emails = [line.strip() for line in f.readlines()]

    out_instagram = []
    client = httpx.AsyncClient()

    for email in emails:
        await instagram(email, client, out_instagram)

    with open("hasil_osint_ig.txt", "w") as file:
        for item in out_instagram:
            file.write(f"{item}\n")

    print("Hasil tersimpan di hasil_osint_ig.txt")
    await client.aclose()

trio.run(main)
