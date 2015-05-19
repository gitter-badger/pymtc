# pymtc

## Install

Do follow command in your shell:

    python ./setup.py install

## Usage

Create source some like that:

```python
from pymtc import MakeTestClient


make_test_client = MakeTestClient(token=None)

# Step 1. Count message
count = make_test_client.messageCount(mailbox="101")
print("Mainbox contain {count} message".format(count=count))

# Step 2. List message
message_index = make_test_client.messageIndex(mailbox="101")
message_id = None
for message in message_index:
    message_id = message.get_msg_id()
    print("Message: msg_id = {msg_id!r}".format(msg_id=message_id))


# Step 3. Load message
message_content = make_test_client.messageFetch(message_id)
print("Content:\n\n {content}".format(content=message_content))
```
