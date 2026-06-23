from browser_use import ChatGoogle
from browser_use.llm.messages import UserMessage
import asyncio

async def test_llm():
    llm = ChatGoogle(model='gemini-2.5-flash')
    response = await llm.ainvoke([UserMessage(content="Say hello")])
    print(response)

asyncio.run(test_llm())