# 🤖 GREG Discord Bot

**GREG** is an all-in-one Discord bot written in Python, featuring AI-powered responses, image generation, and a modular architecture. It is lightweight and suitable even for mobile hosting via Termux or UserLand.

---

## 🚀 Features

- 🎨 **Image Generation** – Generate images using the Prodia API
- 💬 **AI-Powered Replies** – Chat-like interaction via GPT-based tools
- 🧩 **Modular Cogs** – Extend the bot’s functionality with ease
- 🖥️ **Lightweight** – Optimized for mobile terminals (Termux, UserLand)
- 🌐 **Multi-language Support** (planned via `lang/` directory)

---

## 📦 Installation

### Requirements
- Python 3.8+
- `pip` (Python package manager)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/suffaro/greg-discord-bot-py.git
   cd greg-discord-bot-py
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your bot**
   - Rename `config.yml.example` to `config.yml`
   - Fill in required fields like your Discord token and API keys

4. **Run the bot**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

Edit the `config.yml` file:

```yaml
discord_token: "YOUR_DISCORD_BOT_TOKEN"
prodia_api_key: "YOUR_PRODIA_API_KEY"
prefix: "!"
```

## 📝 Roadmap / TODO

- [ ] Add voice channel join/leave support (via FFmpeg)
- [ ] Implement music playbook (YouTube, Spotify, etc.)
- [ ] Improve logging and error handling
- [ ] Add multi-language support
- [ ] Modularize AI chat functionality

## 📱 Mobile Hosting

You can host GREG on mobile platforms:

- ✅ **UserLand** (recommended)
- ✅ **Termux** (supported, but limited)

## 🤝 Contributing

Contributions are welcome!

1. Fork this repo
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes
4. Push the branch: `git push origin feature/YourFeature`
5. Open a pull request
