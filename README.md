# HansBot
This is Hans. Hans gets ze Flammenwerfer and does other entertaining stuff in Discord.

# Local installation
Install deps via `pipenv install`.
Afterwards, run Hans by calling `python hans.py`

# Docker image
There's a Dockerfile. Just call `docker-compose build` and you're good to go!  
Check for the environment vars! I would recommend to overwrite them in a `docker-compose.override.yml`  
or through the corresponding environment variables:  
- HANS_GIPHY_API_KEY: API key for giphy
- HANS_DISCORD_BOT_TOKEN: Discord token (check https://discordapp.com/developers/applications/, select App -> Bot and *copy token*)
- HANS_TARGET_VOICE_ROOM: Target room to move people to when !treppe is called

# ToDo
- [x] Moving users by tagging them (@...) does not work currently
- [x] Make Giphy API key customizable
- [x] Make target room customizable
- [ ] Make Guild customizable (There's only one?)
- [x] Make Discord key customizable
- [x] Add Docker image