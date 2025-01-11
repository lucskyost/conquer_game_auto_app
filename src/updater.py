import os
import shutil


def on_exit():
    try:
        # Path to the updated exe file
        updated_exe_path = "./dist/ConquerAutoApp.exe"

        # Current exe file path
        current_exe = "./ConquerAutoApp.exe"

        # Copy the updated exe to the current directory
        shutil.copyfile(updated_exe_path, current_exe)
        print("copied")
        if os.path.exists("dist"):
            shutil.rmtree("dist")
        # Start the updated exe
        # os.execv(current_exe, [current_exe])
        os.startfile(current_exe)

    except Exception as e:
        print(f"Error on exit: {str(e)}")
on_exit()