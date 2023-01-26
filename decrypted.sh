#!/bin/bash
# Script By Slayy2357

PS3='Your Choice : '
options=("Inject Csv Logic" "Inject Csv Client" "Return" "Exit")
select opt in "${options[@]}"
do
    case $opt in
         "Inject Csv Logic")
             cp -r /var/mobile/test/.csv/csv_logic /private/var/mobile/Containers/Data/Application/5392FE75-C39D-4373-A45C-70214939AA96/Documents/updated
echo "Successfully injected Csv_Logic !"
             ;;
         "Inject Csv Client")
             cp -r /var/mobile/test/.csv/csv_client /private/var/mobile/Containers/Data/Application/5392FE75-C39D-4373-A45C-70214939AA96/Documents/updated
echo "Successfully injected Csv_Client !"
             ;;
         "Return")
             python main.py
             ;;
         "Exit")
             break
             ;;
         *) echo "invalid option $REPLY";;
esac
done
