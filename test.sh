#!/bin/bash

GREEN="\e[32m"
RED="\e[31m"
NC="\e[0m"

total_checks=0
failed_checks=0

function assess_security {
    local command="$1"
    local success_message="$2"
    local failure_message="$3"

    total_checks=$((total_checks + 1))

    if eval "$command" 2>/dev/null; then
        if [ "$SuccessMode" -eq 1 ]; then
            echo -e "${GREEN}SUCCESS${NC}: $success_message"
        fi
    else
        if [ "$WarningMode" -eq 1 ]; then
            echo -e "${RED}WARNING${NC}: $failure_message"
        fi
        failed_checks=$((failed_checks + 1))
    fi
}

echo 'What mode should this script run as?'

function Scanner_Menu() {
    echo -e "Menu:
    1) Warnings and Successes Displayed
    2) Only Warnings Displayed
    3) Only Successes Displayed
    4) Exit
    "
    echo -n "Mode: "
    read MENU

    case $MENU in
        1)
            WarningMode=1
            SuccessMode=1
            ;;
        2) 
            WarningMode=1
            SuccessMode=0
            ;;
        3)
            WarningMode=0
            SuccessMode=1
            ;;
        4)
            exit
            ;;
        *)
            echo -e "\n\nINVALID: Please choose a valid option!\n\n"
            clear
            Scanner_Menu
            ;;
    esac
}

Scanner_Menu

assess_security "grep -Fxq 'ENCRYPT_METHOD SHA512' /etc/login.defs" \
    "Encryption Method is set to SHA512! (/etc/login.defs)" \
    "The Encryption method is not securely set to SHA512! (/etc/login.defs)"

assess_security "grep 'ENABLED=yes' /etc/ufw/ufw.conf >/dev/null" \
    "UFW is enabled!" \
    "Uncomplicated Firewall is not enabled! (Service)"

assess_security "grep -Fxq 'PASS_MAX_DAYS 90' /etc/login.defs" \
    "Password Max Age is 90! (/etc/login.defs)" \
    "The maximum age for Passwords is insecure! (/etc/login.defs)"

assess_security "grep -Fxq 'PASS_MIN_DAYS 14' /etc/login.defs" \
    "Password Min Age is 14! (/etc/login.defs)" \
    "Password Min Age is not 14! (/etc/login.defs)"

assess_security "grep -Fxq 'UID_MIN 1000' /etc/login.defs" \
    "Minimum User ID is set to higher than 1000! (/etc/login.defs)" \
    "The minimum user UID is not set to be higher than 1000! (/etc/login.defs)"

assess_security "grep -Fxq 'UMASK 077' /etc/login.defs" \
    "UMASK is set to 077! (/etc/login.defs)" \
    "The UMASK is not securely set! (/etc/login.defs)"

success_checks=$(( $total_checks-$failed_checks))

echo "---------------------------"
echo "Total Security Checks: $total_checks"
echo "Suceeded Checks: $success_checks"
echo "Failed Checks: $failed_checks"
echo ""

passcheck=$(expr $success_checks / $total_checks)
passingrate=$(( 3 / 4 ))

if [ $passcheck -lt $passingrate ]; then
    echo -e "${GREEN}Your system passed 75% of the checks and is SECURE.${NC}"
    echo -e "Your score: $passcheck"
else
    echo -e "${RED}Your system failed to pass 75% of the checks and is NOT SECURE.${NC}"
    echo -e "Your score: $passcheck"
fi

