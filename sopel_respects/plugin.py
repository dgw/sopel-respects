"""Press F to pay respects.

Original version released under The Unlicense by xnaas at
https://git.actionsack.com/xnaas/sopel-respects
"""
from sopel import plugin


F_CLASS = '[F𝔽]'


@plugin.rule(rf"^{F_CLASS}$")
def f(bot, trigger):
	bot.action("pays respects")

@plugin.rule(rf'^presse[ds] {F_CLASS}$')
def press_f(bot, trigger):
	bot.action("pays respects")
