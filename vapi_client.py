# vapi_client.py
import os
from dotenv import load_dotenv
from vapi import Vapi

load_dotenv()

vapi = Vapi(token=os.getenv("VAPI_PRIVATE_KEY"))

async def create_call(customer_number: str):
    response = await vapi.calls.create(
        phone_number_id=os.getenv("VAPI_PHONE_NUMBER_ID"),
        customer={"number": customer_number},
        assistant={
            "model": {
                "provider": "openai",
                "model": "gpt-4o",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant. Keep your responses concise and friendly."
                    }
                ]
            }
        }
    )
    return response
