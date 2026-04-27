# get-last-frame

To get started, install Python and the required dependencies, then build the executable.

```bash
# 1. Install Python 3.12 (if you don't have it)
winget install Python.Python.3.12 

# 2. Navigate to your working directory
cd Desktop

# 3. Install required Python packages
pip install opencv-python pyinstaller

# 4. Build the standalone executable
pyinstaller --onefile get_last_frame.py
```
