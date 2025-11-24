# How to use the User History Archive Microservice:
It's super easy!</br>
If you want to store an action whenever your user does something, write to the input txt file ```uha-input.txt``` with this format: ```user,action```.</br>
If you want to erase the archive, write ```erase``` to ```uha-input.txt```.</br>

To read the archive, your main program can simply read the entire ```uha-output.txt``` file.
