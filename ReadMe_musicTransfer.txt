musicTransfer.py is  a short python program which i created to transfer any files in linux(in my case my playlist) to my windows desktop.

Presently i am dual-booting Windows and Ubuntu on my workstation(lolz), this would update my windows Playlist as n when my Ubuntu Playlist is updated, so when i happen to switch to windows i would have the updated list ( coz one cannot transfer ubuntu files to windows, when running windows #FAIL :P ).

Optional: 
I have used cron jobs to schedule the task of transfering.( One should have prior knowledge of crontab/Cron jobs to use this )
CronJob :  every min this would automatically run in the background 

* * * * * python /path/of/musicTransfer.py

This would check every minute for any update in your playlist in Linux, if it finds a change it will be reflected in Windows else no action would be taken.

Requirement: 
Edit musicTransfer.py : 
1. Give your linuxPathname,the folder where you store your playlist.
2. Give your windowsPathname, the folder where you store your playlist in Win.
3. Done!

If you don't plan on using the Cronjob, you can run musicTransfer.py from the terminal before switching ;-).




