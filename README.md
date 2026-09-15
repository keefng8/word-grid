# Word Grid

A word puzzle - find as many words as you can in a grid of letters before the clock runs out. Keeps your best scores. Plays entirely offline with a built-in dictionary.

A feature for [Mavis AI](https://www.mavis-ai.com) — a desktop voice assistant.

```
You: "play word grid"
```

Mavis opens it and stands its own panels down so they are not in your way. Say *"show the interface"* to bring them back.

## Install

From the Mavis Appstore — find **Word Grid** and click Install.

Or install it directly:

```python
from utils.feature_install import install_from_github
install_from_github("https://github.com/keefng8/word-grid")
```

## What you can say

- *"play word grid"*
- *"open the word game"*
- *"give me a word puzzle"*
- *"play a word puzzle"*

These are not matched word for word. Mavis gives them to its language model as examples of intent, so close variations work too.

## Requirements

Python 3.8 or newer, and nothing else — the standard library only. No `pip install`, no model to download, no account.

## Building your own

See [Building features for Mavis](https://github.com/keefng8/mavis-feature-docs) — a feature is just a GitHub repository with a `mavis.json`.

## License

MIT — see [LICENSE](LICENSE).
