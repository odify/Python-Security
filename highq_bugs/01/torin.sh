#!/bin/bash


check_tor() {
    echo "Checking requirements"

    tor_path=$(which tor)
    if [[ ! -z $tor_path ]]; then
        echo "Installation  dir found succesfully"
        return
    else
        install_tor
    fi
}

install_tor() {
    echo "Could not find a tor installation on your system!"
    read -p "install tor now ? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
    echo " loading.... "


    if [[ ! -z $(which apt-get) ]]; then
        sudo apt-get install tor -y
    elif [[ ! -z $(which yum) ]]; then
        sudo yum install tor -y
    elif [[ ! -z $(which dnf) ]]; then
        sudo dnf install tor -y
    elif [[ ! -z $(which pkg) ]]; then
        sudo pkg install tor -y
    elif [[ ! -z $(which pkg_add) ]]; then
        sudo pkg_add install tor -y
    else
        echo "Failed to get a package manager! You might need to manually install tor."
        exit 1
    fi

    echo "config completed "
}

handle_command() {
    if [[ "$1" == "start" ]]; then
        if sudo systemctl start tor.service; then
            echo "Tor service started"
        else
            echo "Could not start tor service"
        fi
    elif [[ $1 == "stop" ]]; then
        if sudo systemctl stop tor.service; then
            echo "Tor service stopped"
        else
            echo "Could not stop tor service"
        fi
    elif [[ $1 == "restart" ]]; then
        if sudo systemctl restart tor.service; then
            echo "Tor service restarted"
        else
            echo "Tor service could not be restarted"
        fi
    elif [[ $1 == "status" ]]; then
        sudo systemctl status tor.service
    elif [[ $1 == "" ]]; then
        echo "Synthax error"
    else
        echo "unknown"
    fi
}

check_tor
handle_command $1


