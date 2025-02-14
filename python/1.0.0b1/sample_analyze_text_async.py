# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import asyncio
import os
from azure.ai.contentsafety.aio import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions

async def analyze_text_async():
    # analyze text async
    key = os.environ["CONTENT_SAFETY_KEY"]
    endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

    # Create an Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

    async with client:
        # Contruct request
        request = AnalyzeTextOptions(text="You are an idiot")

        # Analyze text
        try:
            response = await client.analyze_text(request)
        except HttpResponseError as e:
            print("Analyze text failed.")
            if e.error:
                print(f"Error code: {e.error.code}")
                print(f"Error message: {e.error.message}")
                raise
            print(e)
            raise

    if response.hate_result:
        print(f"Hate severity: {response.hate_result.severity}")
    if response.self_harm_result:
        print(f"SelfHarm severity: {response.self_harm_result.severity}")
    if response.sexual_result:
        print(f"Sexual severity: {response.sexual_result.severity}")
    if response.violence_result:
        print(f"Violence severity: {response.violence_result.severity}")

async def main():
    await analyze_text_async()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
