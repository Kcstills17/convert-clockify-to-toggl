This script converts a CSV time export from Clockify into a toggl-compatible CSV file for import. 

`Requirements` 

- Python version 3 or greater 
- Pandas 

to install pandas run this command 

```
pip install pandas
```




`Walkthrough Clockify`
1. 1st navigate  to the top right and select -> preferences 
2. Scroll to the bottom to Time settings
3. To make sure this conversion works appropriately. Switch Date-format to be in YYYY-MM-DD format. Also make sure Time-format is 12 hours.

3. In clockify, navigate to Reports -> Detailed 
4. Choose a date range. (If you are on the free plan like me this will only span a year at a time)
5. Click Export -> select CSV 
6. This will download a file. The file will be in the format like so 

```
Clockify Detailed Report - 2025-07-01.csv
```


`Run Script`

 now you can run the following command in the command line 

```

python clockify_to_toggl.py "Clockify Detailed Report - 2025-07-01.csv"

```

This will generate a new file called `toggl_upload.csv` 

You can rename this file to be more specific. 



`Import into Toggl`

1. In Toggl navigate to import/export 
2. click import time entries 
3. find toggl_upload.csv or your specific file name and import 


`Configuration` 
In the script (should be line 6) update your toggl email here 
```
# -------- CONFIG --------
USER_EMAIL = "Youremail@email.com"
# ------------------------
```


`Additional Notes` 
I had some issues initially based off of the formatting the dummy export from toggl provided me. It also included a Stop time which will break the conversion if included as apart of converting the clockify format to a toggl file funny enough.



`Possible Improvements in the future` 

This was created as a result of a need I had with my time tracking. But now that this is finished I may end up adding additional features. 
Some ones on the top of mind 
1. Time-zone conversion 
2. custom tag modifications 

Let me know if you would like to see this added. Or if you want, you can play around and add them yourself. 



`Contact info`

If you have any questions or run into any issues with this program feel free to hit me up on Linkedin. 

[My linkedIn Page](https://www.linkedin.com/in/zane-lee-14496a297/)




