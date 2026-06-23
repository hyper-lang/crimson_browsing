from browser_use import Agent, Browser, ChatGoogle
from pydantic import BaseModel
import asyncio

class SignupResult(BaseModel):
    signed_up: bool
    final_url: str
    wallet_addresses_found: list[str]
    notes: str

async def signup_and_find_wallet(url: str):
    browser = Browser(headless=False)  # visible, so you can step in for KYC/CAPTCHA/email verification

    agent = Agent(
        task=(
            f"Go to {url}. Sign up for a new account using "
            f"the name 'Jordan Lee', email 'jordan.lee.test+{{random}}@example.com', "
            f"and a strong password. Use placeholder values for any other required "
            f"fields, skip optional ones. If email verification is required, pause "
            f"and report that instead of trying to access the email account. "
            f"After signup, navigate to the deposit, wallet, or 'receive crypto' "
            f"section of the account dashboard. Report any wallet/deposit addresses "
            f"shown there for the logged-in account (e.g. BTC, ETH, USDT addresses)."
        ),
        llm=ChatGoogle(model='gemini-2.5-flash'),
        fallback_llm=ChatGoogle(model='gemini-3-flash-preview'),
        browser=browser,
        output_model_schema=SignupResult,
    )

    history = await agent.run()
    result: SignupResult = history.structured_output

    print(result.model_dump_json(indent=2))
    history.save_to_file("signup_run_history.json")

    await browser.close()
    return result

if __name__ == "__main__":
    asyncio.run(signup_and_find_wallet("https://example-exchange.com"))