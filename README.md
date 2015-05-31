# pymtc

Python Make Test Client version 1.1

## Install

Do follow command in your shell:

    python ./setup.py install

## Usage

Create source some like that:

```python
import pymtc


# Prepare variable and client
user = 'audiopoisk21'
client = pymtc.MakeTestClient()


# Step 1. Fetc message count
print client.messageCount(user)

# Step 2. Fetch index
items = client.messageIndex(user)
print items

# Step 3. Fetch message
for item in items:
    msgid = item.get_msgid()
    msg = client.messageFetch(msgid=msgid)
    print msg


# Step 4. Dispose clisent
client.dispose()
client = None
```
