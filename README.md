************************************************************************************************
Extract then rename and save -> Mutanerator -> Organize mutants files -> kGenProg
************************************************************************************************

**Extract db and save**
The save_pair.py in ExtractSqlite/ use to extract the files from the .db database file.
Also renaming the file name and enclosing the src code method.
Just make sure to correct the path.


**Mutanerator**
The mutate_script.py in Mutation/ use to automatically mutate src code files in every pair. 
Put this file and the result folder from the save_pair script in the Mutanerator repository and edit the important paths written in the script file including path of .jar file, path of pairs folder, and path of output folder for this script.


**Organize mutants and test files structure**


**kGenProg**
