from dotenv import dotenv_values
from owlmind.pipeline import ModelProvider
from owlmind.simple import SimpleEngine
from owlmind.discord import DiscordBot

if __name__ == '__main__':

    # Load config from .env
    config = dotenv_values('.env')

    # Access variables properly
    TOKEN = config.get('DISCORD_TOKEN')
    URL = config.get('SERVER_URL')
    MODEL = config.get('SERVER_MODEL')
    TYPE = config.get('SERVER_TYPE')
    API_KEY = config.get('SERVER_API_KEY')

    # Configure a ModelProvider if there is an URL
    provider = ModelProvider(type=TYPE,  base_url=URL, api_key=API_KEY, model=MODEL) if URL else None

    # Load Simples Bot Brain loading rules from a CSV
    engine = SimpleEngine(id='bot-1')
    engine.model_provider = provider
    engine.load('rules/bot-rules-5.csv')

    # Kick start the Bot Runner process
    bot = DiscordBot(token=TOKEN, engine=engine, debug=True)
    bot.run()