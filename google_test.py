from browser_use import Agent, Browser, ChatGoogle
import asyncio

async def search_test(query: str):
    browser = Browser()

    agent = Agent(
        task=f"Go to https://google.com and search for '{query}'. Report the titles of the top 3 results.",
        llm=ChatGoogle(model='gemini-2.5-flash'),
        browser=browser,
    )
    result = await agent.run()
    print(result)
    await browser.close()

asyncio.run(search_test("browser-use python library"))