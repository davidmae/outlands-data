# Set the path to the Python executable
$pythonExe = "python.exe"

# Set the path to the Python script
$scriptPath = "Client\JournalLogs\extract_info.py"

# Run the Python script
& $pythonExe $scriptPath

# Pause the script and wait for user input
Read-Host "Press Enter to continue..."