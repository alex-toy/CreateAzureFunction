Create an Azure WebJob
=
In this project, we'll create an Azure web app resource then we will set up a Triggered WebJob for the web app that will fetch the Azure Announcements RSS feed every 30 sec and store the 5 newest announcements to later display to the user.

Unfortunally I was not able to run successfully the command **az webapp webjob triggered run**. If you can help me on that... ;-)

1. Create an Azure Web App:
    - OS: Windows OS
    - Runtime: .Net 4.7 or higher
    - Pricing Tier: Free tier app service plan
2. Upload the web job to the Azure Web App
    - The web job zip file is located: in webjob\AzureAnnouncer.zip
    - This background task fetched the Azure Announcements RSS feed every 30 sec then store the 5 newest announcements to later display to the user
    - Web Job Type: Triggered
    - Triggers: Scheduled
    - CRON Expression: 0/30 * * * * *

Be sure to clean up and delete resources to avoid recurring charges