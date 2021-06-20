# Quick Shutdown

Ever need to shutdown your computer in the blink of an eye? You got it.


## Usage

```python
python NtShutdownSystem.py
```

## How does it work?

Using the routine `NtShutdownSystem` we are able to shutdown the system quick and easy without any way to recover. Behind the scenes it calls another routine, `PoSetSystemPowerState` which does many things such as the I/O manager sending shutdown IRP's, memory manager writing data back to the respective files, configuration manager flushing any registry changes, I/O manager notifying all the system drivers about the shutdown, and the power manager powers off the system.

## Sources
[NtShutdownSystem](http://undocumented.ntinternals.net/UserMode/Undocumented%20Functions/Hardware/NtShutdownSystem.html)

[ShutdownAction](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/mscs/property-lists)
