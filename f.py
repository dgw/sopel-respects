"""
Authors: xnaas <me@xnaas.info> (2022)
License: The Unlicense (public domain)
Require: python>=3.8
"""
from sopel import plugin


@plugin.rule('^F$')
def pay_respects(bot, trigger):
	bot.action('pays respects')
