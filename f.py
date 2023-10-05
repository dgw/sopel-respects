"""
Authors: xnaas <me@xnaas.info> (2022)
License: The Unlicense (public domain)
"""
from sopel import plugin


@plugin.rule(r"^F$")
def pay_respects(bot, trigger):
	bot.action("pays respects")
