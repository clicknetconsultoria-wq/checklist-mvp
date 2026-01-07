import os
import httpx

BOT_URL = os.getenv("WHATSAPP_BOT_URL")
BOT_TOKEN = os.getenv("WHATSAPP_BOT_TOKEN")

async def enviar_checklist(payload: dict):
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            f"{BOT_URL}/checklist/send",
            json=payload,
            headers={
                "x-api-key": BOT_TOKEN
            }
        )

    if response.status_code != 200:
        raise Exception(response.text)
