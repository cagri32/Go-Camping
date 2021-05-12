# Go-Camping
Find an available spot quickly at the busiest camping grounds

# Background
-I was planning to go to Banff National Park this summer for 10 days.
-I knew that Banff was the busiest and fastest-booked camping ground in Canada.
-I still tried checking the website a few times every day to find a consequtive 10-day spot to stay.
-I was changing location and day filters to find a spot and repeating myself frequently.
-Then I thought that I could do this faster and easier if there was a tool for that.
-Therefore, I decided to write this script which would enter all the input and do all the selections I manually did.
-After playing with it a little longer, I added more feature and expanded its functionality.
-So far, it uses default values which are the days I want to stay there.

-I set the script to run at regular intervals to be able to find out when a spot is available.
-The interval can be changed by altering **waittime** variable. 

## Optional parameters can be passed with script to change the values
Optional parameters can be passed with script such as day, month, number of nights, park name and the site name at that park.

Parameters can be seen using the following command:
```
python .\GoCamping.py -h
usage: GoCamping.py [-h] [--month MONTH] [--day DAY] [--nights NIGHTS] [--park PARK] [--site SITE]

optional arguments:
  -h, --help       show this help message and exit
  --month MONTH    Enter the first 3 letters of the month you want to visit in eg. Jun, Aug
  --day DAY        Enter the day as ordinal number eg. 1st, 5th, 23rd
  --nights NIGHTS  Enter the number of nights you want to stay eg. 1, 2, 5
  --park PARK      Enter the name of the park you want to visit eg. Banff, Bruce Peninsula
  --site SITE      Enter the name of the site you want to camp at eg. Two Jack Lakeside
```
**example usage of the optional arguments:**
```
python .\GoCamping.py --month=Jun --day=25th --nights=4
python .\GoCamping.py --park=Fundy --month=Jul --day=25th --nights=4
python .\GoCamping.py --park=Banff --site:Two Jack Lakeside --month=Jul --day=25th --nights=4
```

## My short-term plans for this script are:
[x] to automate it to run in regular intervals
[] to check a larger range of days to find the desired consequtively available spot
[] to make it send me notifications if there is an availability

## My long-term plans are:
[] store the found the data on a database to operate faster and avoid scraping the website
[] to have it calculate the average cost for the planned booking
[] and finally turn it into a website using React JS so that others can benefit from it.

-As of the 7th day of writing the script my efforts were paid off for. I found the spot I was looking for. Going for a camp for 10 days :)
-Now I will continue to look for a better spot at Two Jack Lakeside Site and continue developing this program.


