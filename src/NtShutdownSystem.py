import ctypes

class Shutdown:
    def __init__(self):
        self.NTDLL = ctypes.windll.ntdll

    def RtlAdjustPrivilege(self):
        _RtlAdjustPrivilege = self.NTDLL.RtlAdjustPrivilege
        _RtlAdjustPrivilege.argtypes = [
            ctypes.c_ulong,
            ctypes.c_long,
            ctypes.c_long,
            ctypes.POINTER(
                ctypes.c_long
            )
        ]
        _RtlAdjustPrivilege.restype = ctypes.c_long

        status = _RtlAdjustPrivilege(
            19, # Privilege (SE_SHUTDOWN_PRIVILEGE)
            True, # Enable Privilege
            False, # Current Thread
            ctypes.byref(
                ctypes.c_long(0)
            ) # Byref Previous Value As UInt
        )

        if status != 0:
            return False

        else:
            return True

    def NtShutdownSystem(self):
        if self.RtlAdjustPrivilege():
            return self.NTDLL.NtShutdownSystem(
                False # ShutdownNoReboot Action
            )

if __name__ == '__main__':
    shutdown = Shutdown()
    shutdown.NtShutdownSystem()
