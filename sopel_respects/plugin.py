"""
Authors: xnaas <me@xnaas.info> (2022-2023)
License: The Unlicense (public domain)
"""
from sopel import plugin


@plugin.rule(r"^[F𝔽]$")
def pay_respects(bot, trigger):
	bot.action("pays respects")
