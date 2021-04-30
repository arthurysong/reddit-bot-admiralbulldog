"""Just a demo file to test out how to implement exception handling for praw

Idk if it's my internet but PRAW will fail trying to connect to Reddit's API,
so I need the task to reconnect on it's own if it fails"""

import asyncio
import logging

# TIL this is a coroutine function
async def co(some_number=1):
  while 1: 
    try: 
      print("i am 1")
      await asyncio.sleep(1)
      if (some_number == 2):
        raise Exception('balls')
      print("i am 2")
      await asyncio.sleep(1)
      print("i am 3")
      await asyncio.sleep(1)
      print("i am streaming now")
      await asyncio.sleep(100000000)
    except Exception as e:
      logging.warning("dns failure...")


  # return 42

# TIL this is a coroutine object
# co()

async def main():
  # print(await co())

  # a task is used to run coroutines concurrently
  # task = asyncio.create_task(co())
  # task2 = asyncio.create_task(co())

  # now we can either cancel or await the task
  # print(await task)
  # print(await task2)


  # schedule three calls concurrently
  # await asyncio.gather(
  #   co(),
  #   co(2),
  #   co()
  # )

  # await asyncio.wait(co())
  task = asyncio.create_task(co())
  task2 = asyncio.create_task(co())
  task3 = asyncio.create_task(co(2))

  await task
  await task2
  await task3
  # try: 
  #   await task3
  # except Exception as e:
  #   print("there was an exception")


  try:
    raise Exception('spam', 'eggs')
  except Exception as e: 
    print(type(e))
  
  raise Exception('spam', 'eggs')

  print("i got to here")

# you can get the return by awaiting a coroutine
asyncio.run(main())



