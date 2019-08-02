# HansBot
This is Hans. Hans gets ze Flammenwerfer and does other entertaining stuff in Discord.

# Local installation
Install deps via `pipenv install`

# Docker image
There's a Dockerfile. Just call `docker-compose build` and you're good to go!  
Check for the environment vars! I would recommend to overwrite them in a `docker-compose.override.yml`

# ToDo
- [ ] Moving users by tagging them (@...) does not work currently
- [ x ] Make Giphy API key customizable
- [ x ] Make target room customizable
- [ ] Make Guild customizable (There's only one?)
- [ x ] Make Discord key customizable
- [ x ] Add Docker image