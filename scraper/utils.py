# Human-like behavior utils

import asyncio
import random
from config import MIN_DELAY, MAX_DELAY

async def random_delay():
    await asyncio.sleep(random.uniform(MIN_DELAY, MAX_DELAY))



