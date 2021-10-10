from src.Item import Item


# try:
with Item() as bot:
    bot.get_page()
    bot.search_val()
    bot.category()
    bot.submit_btn()
    bot.apply_filters()
    bot.refresh()
    bot.report_listings()
    bot.sd = True
    bot.__exit__()
# except Exception as e:
#     print(e)




