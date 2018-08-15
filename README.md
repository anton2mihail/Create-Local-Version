# Create Local Version
<h2>This is a python utility</h2>

It takes a source directory that contains some files and creates a new directory on the pc's main drive called ` "DataTest" ` and populates it with the contents of the source directory. The utility also opens a file of your choice after copying.

<h3>To change the source directory go into the python file, and right below the imports there is a variable:</h3>

`sourceDirectoryPath = ""` Insert the directory path that you want to copy here.
  
 <h3>To change desitnation file name navigate to: </h3>

 a variable called `maindrive = i+r":\\DataTest"` Change `"DataTest"` to desired name.
  
<h3>To change opened file simply edit the 9th line:</h3>

```python
filenameToOpen = "filename here"
# Change this
```
