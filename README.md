Covergen
=========

How To Install It
-------------

Tutorial
-------------
When first starting with Covergen, it is best to either look through old cover letters or write some new ones. Once you've noticed some common patterns or have thought of sentences that you would like to reuse. It is a good idea to use the add command to add this information to Covergen's database which is held in a data.json file. For example, if I want to add the phrase "I like swimming" under the swimming name in the hobbies library. I would run the following command.
 ```bash
 ./covergen add hobbies.swimming "I like swimming"
 ```
 The following .coverletter file demonstrates how to use this phrase. You should save this coverletter to tutorial.coverletter
 ```python3
 {covergen[hobbies][swimming]}
 ```
 The following command will compile the .coverletter file depicted above to a .coverletter.output file.
 ```bash
 ./covergen compile tutorial.coverletter
 ```
The previous command will create a file named tutorial.coverletter.output that should contain the following text
```
I like swimming
```

Explanation of Cover Letter Template Format
--------------

How It Works
--------------
