import logging.config
import asyncio
import sys
import warnings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s:%(lineno)d %(message)s',
    stream=sys.stderr,
)
LOG = logging.getLogger('')


async def operationsub():
    LOG.info('start operationsub')
    LOG.info('operationsub10')
    await asyncio.sleep(1)
    LOG.info('operationsub11')

async def operation():
    LOG.info('start operation')
    task = asyncio.ensure_future(operationsub())
    LOG.info('operation1')
    await asyncio.sleep(0.2)
    LOG.info('operation2')
    await asyncio.sleep(3)
    LOG.info('operation3')

loop = asyncio.get_event_loop()
# LOG.info('enabling debugging')

loop.set_debug(True)
# loop.slow_callback_duration = 0.001
warnings.simplefilter('always', ResourceWarning)

# LOG.info('entering event loop')

asyncio.ensure_future(operation())
loop.run_forever()
loop.close()
exit()
