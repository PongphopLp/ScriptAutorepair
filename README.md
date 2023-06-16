************************************************************************************************
Extract then rename files, enclose class and save -> Rename Method -> Mutanerator -> Organize mutants and test files -> kGenProg
************************************************************************************************

**Extract db and save**
The save_pair.py in ExtractSqlite/ use to extract the files from the .db database file.
Also renaming the file name and enclosing the src code method.
Just make sure to correct the path.


**Rename Method**
Just put the rename script in the same directory as output folder from save_pair.py and make sure to correct the path or folder name.
The script doesn't cover all of the case of method name. So after running the script there are 2 pairs that their method name is not changed. (Pair 254 and 269)
But I decided to rename those 2 pair method's name by hand.


**Mutanerator**
The mutate_script.py in Mutation/ use to automatically mutate src code files in every pair. 
Put this file and the result folder from the save_pair script in the Mutanerator repository and edit the important paths written in the script file including path of .jar file, path of pairs folder, and path of output folder for this script.


**Organize mutants and test files structure**
Make sure to put the data folder from save_pair.py that contain the Target_ESTest.java and Target_ESTest_scaffolding.java in the same directory as output folder that contains the mutants files. Then run this script in the directory.
The script will then move both test file of each pair to the specified directory.

**kGenProg**
