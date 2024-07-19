import aiohttp
import asyncio
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://fantasy.premierleague.com/api/"


async def fetch(session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
    """
    Fetch data from the given URL using the provided session.

    Parameters
    ----------
    session : aiohttp.ClientSession
        The HTTP session to use for the request.
    url : str
        The URL to fetch data from.

    Returns
    -------
    Dict[str, Any]
        The JSON response as a dictionary.
    """
    async with session.get(url) as response:
        if response.status != 200:
            logger.error(f"Error fetching {url}: {response.status}")
            return {}
        return await response.json()


async def get_general_info() -> Dict[str, Any]:
    """
    Get general information about the Fantasy Premier League.

    Returns
    -------
    Dict[str, Any]
        The JSON response containing general information.
    """
    async with aiohttp.ClientSession() as session:
        return await fetch(session, f"{BASE_URL}bootstrap-static/")


async def get_player_info(player_id: int) -> Dict[str, Any]:
    """
    Get detailed information about a specific player.

    Parameters
    ----------
    player_id : int
        The ID of the player to fetch information for.

    Returns
    -------
    Dict[str, Any]
        The JSON response containing player information.
    """
    async with aiohttp.ClientSession() as session:
        return await fetch(session, f"{BASE_URL}element-summary/{player_id}/")


async def get_fixtures() -> Dict[str, Any]:
    """
    Get fixtures information.

    Returns
    -------
    Dict[str, Any]
        The JSON response containing fixtures information.
    """
    async with aiohttp.ClientSession() as session:
        return await fetch(session, f"{BASE_URL}fixtures/")


async def collect_data():
    """
    Collect general information, fixtures, and detailed player information.

    Logs the number of players and fixtures collected.
    """
    general_info = await get_general_info()
    fixtures = await get_fixtures()

    if not general_info or not fixtures:
        logger.error("Failed to fetch general info or fixtures")
        return

    players = general_info.get("elements", [])
    player_details = await asyncio.gather(
        *[
            get_player_info(player["id"]) for player in players[:10]
        ]  # Limited to 10 for testing
    )

    # Log the collected data
    logger.info(f"Collected data for {len(player_details)} players")
    logger.info(f"Collected {len(fixtures)} fixtures")


if __name__ == "__main__":
    asyncio.run(collect_data())
