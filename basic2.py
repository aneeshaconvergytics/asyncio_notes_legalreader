loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()