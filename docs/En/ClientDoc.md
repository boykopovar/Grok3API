# 🛠️ Description of the `GrokClient` Class

## 🚀 Main class for interacting with the Grok API.

The `GrokClient` class is the primary tool for working with Grok, used for sending requests to the model and automatically saving the history.

> 📁 **Working with history**:  
> When initializing an object of the `GrokClient` class, an object of the `History` class is automatically initialized. The history is automatically loaded from a file when `GrokClient` is initialized.

### 📨 **Accepts:**  
- 🍪 `cookies`: (not necessary) A string or dictionary (or a list of strings / dictionaries for automatic rotation upon reaching the limit) representing the cookie from the grok.com website (obtained via browser → developer tools → Application).
- 🖥️ `use_xvfb`: Flag to use Xvfb on Linux (default `True`).
- 🛡️  `proxy`: URL of the proxy server, used only in case of regional blocking.
- 📋 `history_msg_count`: Number of messages in the history (default `0` - history saving is disabled).  
- 📂 `history_path`: Path to the history file in JSON format. Default: `"chat_histories.json"`.  
- 📄 `history_as_json`: Whether to send the history to Grok in JSON format (for `history_msg_count > 0`). Default: `True`.
- 💾 `history_auto_save`: Automatically rewrite history to file after each message. Default: `True`
- ⏳ `timeout`: Maximum time for client initialization. Default: `120` seconds.

### 🎯 **Returns:**  
- An instance of the `GrokClient` class, ready for use.

---

### Full list of parameters for `GrokClient`:

| Parameter           | Type                                | Description                                                      | Default                          |  
|---------------------|-------------------------------------|------------------------------------------------------------------|----------------------------------|
| `cookies`           | `str` / `dict` / `List[str / dict]` | Cookie from grok.com (not necessary)                             | `-`                              |
| `use_xvfb`          | `bool`                              | Flag to use Xvfb on Linux.                                       | `True`                           |
| `proxy`             | `str`                               | URL of the proxy server, used only in case of regional blocking. | `...`                            |
| `history_msg_count` | `int`                               | Number of messages in the history.                               | `0` (history saving is disabled) |  
| `history_path`      | `str`                               | Path to the history file in JSON format.                         | `"chat_histories.json"`          |  
| `history_as_json`   | `bool`                              | Whether to send the history to Grok in JSON format (if > 0).     | `True`                           |  
| `timeout`           | `int`                               | Maximum time for client initialization (in seconds).             | `120`                            |  

---



### 📋 **Additional information**

- 🌐 **Automatic Browser Initialization**: When the client is initialized, a Chrome session will automatically start to prepare everything for sending requests.  
- 🍪 **Automatic Cookie Rotation**: If a list of cookies (as strings or dictionaries) is provided, cookies will automatically rotate upon reaching the message limit — the new order will be preserved for the current and subsequent requests.  
- 🐧 **Linux Support**: [Detailed instructions for running on Linux](LinuxDoc.md)

> 💡 On Linux without GUI, it is recommended to use Xvfb for stable operation in headless mode.

> 🛠️ To start working with the Grok API, create an instance of `GrokClient` and use its methods, such as `ChatCompletion.create`, to send requests.

---

### 🌟 **Example usage**

```python
from grok3api.client import GrokClient


def main():
    # You can add a list of strings/dictionaries to automatically change when the limit is reached
    # client = GrokClient(cookies="YOUR_COOKIES_FROM_BROWSER")
  
    # Create a client (cookies will be automatically retrieved if not present)
    client = GrokClient()

    # Send a request via ChatCompletion
    response = client.ask(message="Hello, Grok!")
    print(response.modelResponse.message)  # Prints the response from Grok


if __name__ == '__main__':
    main()
```

---

### 🔗 **Related objects**

- **`ChatCompletion`**: An object created within `GrokClient` that provides the `create` method for sending requests to the Grok model. For details, see **[Description of the `create` method](askDoc.md)**.

---

### 📌 **Notes**

- **Error handling**: Exceptions may occur during class initialization (e.g., if cookies could not be obtained). These are logged via `logger.error`.
