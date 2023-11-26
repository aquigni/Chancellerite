# Chancellerite Telegram bot

Installation

```
cd tgbot
```
On mac:
```
pip3 install virtualenv
virtualenv -p python3 <tgbotpath>
source <tgbotpath>/bin/activate
```

debian:
```
apt install python3-venv tmux
```
then
```
cd <tgbotpath>
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
nano .env
```
YOUR_TELEGRAM_BOT_TOKEN='paste_your_token_here'
```
tmux
```
run script inside tmux

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

```
python3 s.py
```
