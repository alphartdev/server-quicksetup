# Setup file

RED="\e[31m"
BLUE="\e[94m"
WHITE="\e[39m"
function defprint {
        echo -e "$BLUE""$1""$WHITE"
}


defprint "${RED}Starting server quick setup..."

read -p "What's this server name?" name

defprint "Setting up misc packages..."
apt-get -y install python python-pip iftop

defprint "Setting preferences (vi and others)"
cp default/vimrc.local /etc/vim/vimrc.local

defprint "Setting up startup script and profile"
cp default/profile /etc/profile
echo "python /etc/startupscript/startup.py $name" >> /etc/profile

mkdir -p /etc/startupscript/
cp scripts/startup.py /etc/startupscript/

echo "# Host to be pinged at startup, format: name:ip" > /etc/startupscript/hosts
defprint "Please configure the hosts to be pinged at login in /etc/startupscript/hosts"

while true; do
    read -p "Should we delete /etc/motd (warranty notic most of the time)?" yn
        case $yn in
	        [Yy]* ) echo "" >> /etc/motd; break;;
		[Nn]* ) exit;;
	        * ) echo "Please answer yes or no.";;
	esac
done


defprint "${RED}Installation completed!"
