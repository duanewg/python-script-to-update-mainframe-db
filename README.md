<p align="center">
<!--img src="https://place-hold.it/600x200" alt="Place Holder Image"/-->
<img src="assets/python.png" alt="Python Logo" />
</p>

# Python script to update database tables on iSeries Mainframe
Created a Python script to perform a daily update of a vehicle information in an iSeries database table.  The table was used by a web application that managed parking lot permits.  Prior to this a manual process was used to add vehicles if they weren't available.  

## Environments and Technologies Used

- Python
- SQL
- Windows Server Task Scheduler

## Operating Systems Used

- Windows Server

## High-Level Deployment and Configuration Steps

- Install Python
- Install iSeries ODBC Driver
- Create Python Scripts
    - [get_vehicles.py](blob/main/get_vehicles.py)
    - [insert_vehicles.py](blob/main/insert_vehicles.py)
- Schedule task in Windows Server Task Scheduler


<h2>Architecture Diagram</h2>

<p>
<img src="https://i.imgur.com/DJmEXEB.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>
