# OneDrive auto migration

This is a simple script to migrate files between OneDrive accounts.

## Configuration
The only things you need to configure is the "config.json" which takes 4 parameters:

- "source": The source folder where the OneDrive(1) folder is located
- "destination": The destination folder where the OneDrive(2) folder is located
- "copy_existing": Whether to copy (True) or not (False) existing files in the destination folder
- "exception" (optional): A list of files to ignore

Example:
```json
{
    "source": "C:\\Users\\user1\\OneDrive",
    "destination": "C:\\Users\\user2\\OneDrive",
    "copy_existing": false,
    "exception": [
        "README.md"
    ]
}
```
