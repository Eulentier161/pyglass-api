# python wrapper for [spyglass-api](https://github.com/dev-ptera/spyglass-api)

```console
pip install pyglass-api
```

```python
from pyglass import PyglassClient

client = PyglassClient() # or PyglassClient("https://api.spyglass.eule.wtf/banano")
acc = client.account.get_overview("ban_1hootubxy68fhhrctjmaias148tz91tsse3pq1pgmfedsm3cubhobuihqnxd")
print(acc.balance)
```
