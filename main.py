from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import logging
import asyncio
from core.handlers import callback_handlers, command_handlers
from core.config.config import BOT_TOKEN

from aiogram_prometheus import (
    BotAiogramCollector,
    DispatcherAiogramCollector,
    PrometheusMetricMessageMiddleware,
    PrometheusMetricStorageMixin,
    PrometheusMetricRequestMiddleware,
    PushGatewayClient,
    StorageAiogramCollector,
)

bot = Bot(BOT_TOKEN, parse_mode="HTML")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
abobus
collector = BotAiogramCollector()
collector.add_bot(bot)
bot.session.middleware(PrometheusMetricRequestMiddleware())

class _Storage(PrometheusMetricStorageMixin, MemoryStorage):
    pass

storage_collector = StorageAiogramCollector()
storage = _Storage(storage_collector)
dp = Dispatcher(storage=storage, bot=bot)

logger.info("Bot started!")

dp.include_routers(callback_handlers.router, command_handlers.router)
dp.message.middleware(PrometheusMetricMessageMiddleware())
DispatcherAiogramCollector(dp)

push_gateway_client = PushGatewayClient('http://pushgateway:9091/', 'app-1')

@dp.startup()
async def on_startup(bot: Bot):
    logger.info("Scheduling Push Gateway metrics push every 5 seconds.")
    push_gateway_client.schedule_push(5)

try:
    asyncio.run(dp.start_polling(bot))
except Exception as ex:
    logger.error('Push gateway error: %s', ex, exc_info=True)
