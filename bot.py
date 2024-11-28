import aiohttp
import asyncio
import json
import re
import os
import random
from colorama import *
from datetime import datetime
from platform import system as s_name
from os import system as sys
import random
from core.helper import get_headers, countdown_timer, extract_user_data, config

class Clayton:
    def __init__(self) -> None:
        self.base_url = "https://tonclayton.fun"
        self.api_base_id = "aT83M535-617h-5deb-a17b-6a335a67ffd5"

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        banner = f"""{Fore.GREEN}
 ██████  ██    ██   ██████  ██    ██  ███    ███  ██████   ███████  ██████  
██       ██    ██  ██       ██    ██  ████  ████  ██   ██  ██       ██   ██ 
██       ██    ██  ██       ██    ██  ██ ████ ██  ██████   █████    ██████  
██       ██    ██  ██       ██    ██  ██  ██  ██  ██   ██  ██       ██   ██ 
 ██████   ██████    ██████   ██████   ██      ██  ██████   ███████  ██   ██     
                                            """
        print(Fore.GREEN + Style.BRIGHT + banner + Style.RESET_ALL)
        print(Fore.GREEN + f" Clayton V2")
        print(Fore.RED + f" FREE TO USE = Join us on {Fore.GREEN}t.me/cucumber_scripts")
        print(Fore.YELLOW + f" before start please '{Fore.GREEN}git pull{Fore.YELLOW}' to update bot")
        print(f"{Fore.WHITE}~" * 60)

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    def set_proxy(self, proxy):
        self.proxy = proxy
        if '@' in proxy:
            host_port = proxy.split('@')[-1]
        else:
            host_port = proxy.split('//')[-1]
        return host_port

    async def find_latest_js_file(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url) as response:
                response.raise_for_status()
                html = await response.text()
                print(html)
                match = re.search(r'\/assets\/index-[^"]+\.js', html)
                print(match)
                return match.group(0).split('/')[-1] if match else None

    async def fetch_api_base_id(self, retries=5, delay=3):
        for attempt in range(retries):
            js_file = await self.find_latest_js_file()
            if js_file:
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"{self.base_url}/assets/{js_file}") as response:
                            response.raise_for_status()
                            js_content = await response.text()
                            match = re.search(r'Yge="([^"]+)"', js_content)
                            if match:
                                self.api_base_id = match.group(1)
                                return
                            else:
                                return None
                except (aiohttp.ClientError, aiohttp.ContentTypeError, json.JSONDecodeError) as e:
                    if attempt < retries - 1:
                        await asyncio.sleep(delay)
                    else:
                        return None
            else:
                if attempt < retries - 1:
                    await asyncio.sleep(delay)
                else:
                    return None


    async def user_authorization(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/authorization'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):

            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def save_user(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/save-user'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def daily_claim(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/daily-claim'
        headers = {
            **self.headers,
            'Content-Length': '0',
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def all_tasks(self, query: str, type: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/{type}'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def start_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/complete'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def claim_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/claim'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def check_tasks(self, query: str, task_id: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/tasks/check'
        data = json.dumps({'task_id': task_id})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt + 1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def user_achievements(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/achievements/get'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
        
    async def claim_achievements(self, query: str, type: str, level: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/user/achievements/claim/{type}/{level}'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def start_game1024(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/start'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def save_tile(self, query: str, session_id: str, tile: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/save-tile'
        data = json.dumps({'session_id':session_id, 'maxTile':tile})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def over_tile(self, query: str, session_id: str, tile: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/game/over'
        data = json.dumps({'session_id':session_id, 'multiplier':1, 'maxTile':tile})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def start_clayball(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/clay/start-game'
        data = {}
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, json=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def end_clayball(self, query: str, score: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/clay/end-game'
        data = json.dumps({'score':score})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def start_gamestack(self, query: str, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/stack/st-game'
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def upadate_stack(self, query: str, score: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/stack/update-game'
        data = json.dumps({'score':score})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None

    async def end_stack(self, query: str, score: int, retries=5):
        url = f'{self.base_url}/api/{self.api_base_id}/stack/en-game'
        data = json.dumps({'score':score, 'multiplier':1})
        headers = {
            **self.headers,
            'Init-Data': query,
            'Content-Type': 'application/json'
        }

        for attempt in range(retries):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, headers=headers, data=data, proxy=self.proxy) as response:
                        response.raise_for_status()
                        if response.status == 200:
                            return await response.json()
                        else:
                            return None
            except (aiohttp.ClientError, aiohttp.ContentTypeError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(3)
                else:
                    return None
                
    async def process_query(self, query: str):
        user = await self.user_authorization(query)
        if not user:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Query ID May Invalid {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}or{Style.RESET_ALL}"
                f"{Fore.YELLOW + Style.BRIGHT} Clayton Server Down {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if user:
            await self.save_user(query)
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['user']['first_name']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['user']['tokens']} $CLAY {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Ticket{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['user']['daily_attempts']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Streak{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {user['dailyReward']['current_day']} day {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            await asyncio.sleep(1)

            daily = user['dailyReward']['can_claim_today']
            if daily:
                claim = await self.daily_claim(query)
                if claim and claim['message'] == 'Daily reward claimed successfully':
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {claim['tokens']} $CLAY {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} Ticket {claim['daily_attempts']} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            for type in ['super-tasks', 'partner-tasks', 'default-tasks', 'daily-tasks']:
                tasks = await self.all_tasks(query, type)
                if tasks:
                    for task in tasks:
                        task_id = task['task_id']
                        is_completed = task['is_completed']
                        is_claimed = task['is_claimed']

                        requires_check = task['task']['requires_check']
                        if not requires_check:
                            if task and not is_completed and not is_claimed:
                                start = await self.start_tasks(query, task_id)
                                if start and start['message'] == 'Task completed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                                    claim = await self.claim_tasks(query, task_id)
                                    if claim and claim['message'] == 'Reward claimed':
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                            elif task and is_completed and not is_claimed:
                                claim = await self.claim_tasks(query, task_id)
                                if claim and claim['message'] == 'Reward claimed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                        else:
                            if task and not is_completed and not is_claimed:
                                check = await self.check_tasks(query, task_id)
                                if check and check['message'] == 'Task completed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Checked{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                                    claim = await self.claim_tasks(query, task_id)
                                    if claim and claim['message'] == 'Reward claimed':
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                            f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                            f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Checked{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                            elif task and is_completed and not is_claimed:
                                claim = await self.claim_tasks(query, task_id)
                                if claim and claim['message'] == 'Reward claimed':
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['reward_tokens']} $CLAY {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['game_attempts']} Ticket {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {task['task']['title']} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Tasks{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

            user_achievements = await self.user_achievements(query)
            if user_achievements:
                for type, achievements in user_achievements.items():
                    if type in ["friends", "games", "stars"]:
                        for achievement in achievements:
                            level = str(achievement['level'])
                            is_completed = achievement['is_completed']
                            is_rewarded = achievement['is_rewarded']

                            if achievement and is_completed and not is_rewarded:
                                claim = await self.claim_achievements(query, type, level)
                                if claim and claim['reward']:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Achievments{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {type} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ][ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {claim['reward']} $CLAY {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ Achievments{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {type} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Achievments{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            await asyncio.sleep(1)

            user = await self.user_authorization(query)
            ticket = user['user']['daily_attempts']
            if ticket > 0:
                while ticket > 0:
                    game_stack = await self.start_gamestack(query)
                    if game_stack and game_stack['session_id']:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT} Is Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ ID{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {game_stack['session_id']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        stack_score = config['stack_score']
                        max_score = random.randint(min(stack_score), max(stack_score))

                        score = 10
                        while score <= max_score:
                            update = await self.upadate_stack(query, score)
                            if update and update['message'] == 'Score updated successfully':
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT} Success to Update {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Score{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {score} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT} Failed to Update {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break

                            score += 10
                            await asyncio.sleep(1)

                        end = await self.end_stack(query, score)
                        if end:
                            ticket -= 1
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {end['earn']} $CLAY {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {end['xp_earned']} XP {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT} Isn't Completed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        break

                    await asyncio.sleep(2)
                    play_clayball = config['play_clayball']
                    if play_clayball:

                        start = await self.start_clayball(query)
                        if start and start['session_id']:
                            ticket = start['attempts']
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Clayball{Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}] [ ID{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {start['session_id']} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )

                            sleep = random.randint(10, 15)
                            for remaining in range(sleep, 0, -1):
                                print(
                                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                                    f"{Fore.YELLOW + Style.BRIGHT} {remaining} {Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT}Seconds to Complete Game{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}   ",
                                    end="\r",
                                    flush=True
                                )
                                await asyncio.sleep(1)

                            clayball_score = config['clayball_score']
                            score = random.randint(min(clayball_score), max(clayball_score))
                            end = await self.end_clayball(query, score)
                            if end:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Clayball{Style.RESET_ALL}"
                                    f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {end['reward']} $CLAY {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ Game Clayball{Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT} Isn't Completed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}              "
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ Game Stack{Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                            break

                if ticket == 0:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Play Game{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} No Ticket Remaining {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Play Game{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} No Ticket Remaining {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )

    async def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]
            with open('proxies.txt', 'r') as file:
                proxies = [line.strip() for line in file if line.strip()]

            while True:
                # await self.fetch_api_base_id()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Proxy's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(proxies)}{Style.RESET_ALL}"
                )
                self.log(
                    f"{Fore.CYAN + Style.BRIGHT}-----------------------------------------------------------------------{Style.RESET_ALL}")

                for i, query in enumerate(queries):
                    query = query.strip()
                    if query:
                        self.log(
                            f"{Fore.GREEN + Style.BRIGHT}Account: {Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT}{i + 1} / {len(queries)}{Style.RESET_ALL}"
                        )
                        if len(proxies) >= len(queries):
                            proxy = self.set_proxy(proxies[i])  # Set proxy for each account
                            self.log(
                                f"{Fore.GREEN + Style.BRIGHT}Use proxy: {Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT}{proxy}{Style.RESET_ALL}"
                            )

                        else:
                            self.proxy=None
                            self.log(
                                Fore.RED + "Number of proxies is less than the number of accounts. Proxies are not used!")

                    user_info = extract_user_data(query)
                    user_id = str(user_info.get('id'))
                    self.headers = get_headers(user_id)
                    try:
                        await self.process_query(query)
                    except Exception as e:
                        self.log(f"{Fore.RED + Style.BRIGHT}An error process_query: {e}{Style.RESET_ALL}")

                    self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}" * 75)
                    account_delay = config['account_delay']
                    await countdown_timer(random.randint(min(account_delay), max(account_delay)))

                cycle_delay = config['cycle_delay']
                await countdown_timer(random.randint(min(cycle_delay), max(cycle_delay)))

        except FileNotFoundError:
            self.log(f"{Fore.RED}File 'query.txt' not found.{Style.RESET_ALL}")
            return
        except Exception as e:
            self.log(f"{Fore.RED+Style.BRIGHT}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        if s_name() == 'Windows':
            sys(f'cls && title Clayton')
        else:
            sys('clear')
        bot = Clayton()
        bot.clear_terminal()
        bot.welcome()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Clayton - BOT{Style.RESET_ALL}",                                       
        )