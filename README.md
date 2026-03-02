# sopel-respects

A Sopel plugin letting users "Press F to pay respects".

## Installing

```sh
pip install sopel-respects
```

## Using

Triggers on these characters (case-insensitive):

* F
* 𝔽

The F must be the only character on its line, or part of a CTCP ACTION (`/me`)
exactly matching the pattern `presse[ds] F`.

## Credits

This is a continuation of [ActionSack's `sopel-respects`][asak-respects-source],
which has been marked as archived and no longer maintained. It maintains the
same license and authorship credits as the original.

CTCP ACTION support is new to this fork.

[//]: # (asak-respects-source is also used in the NEWS file appended for PyPI)
[asak-respects-source]: https://git.actionsack.com/xnaas-archived/sopel-respects
