goal is to .... 

-> standardized way for creating instances from the choline.json format 
-> monitoring success / failure of vanilla startup 
-> machine setup of correct python and req.txt from json 
-> file syncing from json 


Probably best to seperate file syncing code from machine creation for better organization 


Notes 


-> there is a size limit for the vastai onstart script -- so we will use our own 

-> the choline.json file format is still under consideration, and is created using the choline init command, which is also still under development

-> choline init gets the system info for things like python versions and req.txt, and also asks for the files that need to be transfered over, and what GPU's you want to use 


