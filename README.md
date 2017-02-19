# Blockies (for python)

A tiny library for generating blocky identicons.

Python port of the blockies javascript library from https://github.com/alexvandesande/blockies .

# Usage

```
import blockies

data = blockies.create("0xfb6916095ca1df60bb79ce92ce3ea74c37c5d359")
with open('test.png', 'wb') as png:
    png.write(data)
```

# Licence

[WTFPL](http://www.wtfpl.net/)
