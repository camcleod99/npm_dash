# Post-game Anylisis

## Q - Is there any way to make the rebuilding of a docker container any less of an objective ball-ache?

Bluntly speaking having to `docker container down`, `docker container build` and `docker up -d` constantly was something of an ball-ache and I do not appreciate it.

docker compose up -d --build --force-recreate seems to be the best way to do the full reset on app folder save. aliasing it to dc_ur might be the way to go.

## Q - How to check if your ssh is set correctly for github

`$ ssh -T git@github.com`
This should hit the GH server and return the "You're successfully authenticated..." message. What this does is prevent a terminal from being established for you. Very useful for non-interactive SSH scrips.

## SSH Woes

Be sure to add public key: 
- First, check you HAVE one 
	– (client): `$ ls ~/.ssh/id_ed25519.pub`
- If you do not have one, generate it
	- (client): `$ ssh-keygen -t ed25519 -C "your_email@example.com"`
- Then add it to the target server - (client) `$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@ip`
- Then attempt to login, you should be able to do so minus password

If you get password-gated, don't panic, the answer should be in your sshd config:
- open up with Sudo 
	- (Server) `sudo vim /etc/ssh/sshd_conig`
- Check these lines are ether extant or uncommitted
	- PubkeyAuthentication yes
	- AuthorizedKeysFile .ssh/authorized_keys
- Restart SSH
	- (Server) `sudo systemctl restart sshd`
- Then Exit and try to log in again
	- (Server) `exit`
	- (Client) `ssh user@ip`

You *should* now be able to log in minus password, if not then God help you cause I sure as buttons won't.

# DockerFile and Docker Compose

There is, generally speaking, no reason to include copy in your docker file if you intend to mount a location in the docker-compose file.

Just putting it here to save grief.