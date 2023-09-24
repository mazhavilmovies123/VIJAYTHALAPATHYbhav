if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TGxMATRIX/vijay-bot.git /vijay-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /vijay-bot
fi
cd /vijay-bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
