# Chancellerite Telegram bot

Installation


Create bot with [@Botfather](https://t.me/BotFather).
Remember to add your Telegram bot token to .env:
```
touch .env
echo 'YOUR_TELEGRAM_BOT_TOKEN=<your_token>' >> .env
```


```
cd tgbot
```
macOS:
```
pip3 install virtualenv
virtualenv -p python3 <tgbotpath>
source <tgbotpath>/bin/activate
```

Debian:
```
apt install python3-venv tmux
```
then
```
cd <tgbotpath>
python3 -m venv venv
```

```
tmux
```
run script inside tmux:

```
source venv/bin/activate
pip3 install -r requirements.txt
python3 s.py
```

Detach from the tmux session by pressing **Ctrl+B**, then **D**.

If you need to come back to the session, use:

```
tmux attach-session
```

To kill tmux session:
```
tmux list sessions
tmux kill-session -t session-name
```
or
```
tmux kill-server
```


First start tmux session, then venv, then script (then detach session and exit venv).
