************************************************************************************************
Extract then rename and save -> Mutanerator -> Organize mutants files -> kGenProg
************************************************************************************************

**Extract db and save**
The save_pair.py in ExtractSqlite/ use to extract the files from the .db database file.
Also renaming the file name and enclosing the src code method.
Just make sure to correct the path.
The output structure will be:
data/
 Pair#/
  Method$/
   Pair#_Method$.java
   Target_ESTest.java
   Target_ESTest_scaffolding.java
  Method$/
   Pair#_Method$.java
   Target_ESTest.java
   Target_ESTest_scaffolding.java
   
Where # is the number of pair from 1 to 1342, and $ is the number of method between 1 and 2.


**Mutanerator**
The mutate_script.py in Mutation/ use to automatically mutate src code files in every pair. 
Put this file and the result folder from the save_pair script in the Mutanerator repository and edit the important paths written in the script file including path of .jar file, path of pairs folder, and path of output folder for this script.


**Organize mutants and test files structure**
Make sure to put the data folder that contain the Target_ESTest.java and Target_ESTest_scaffolding.java in the same directory as output folder that contains the mutants files. Then run this script in this directory.

**kGenProg**
