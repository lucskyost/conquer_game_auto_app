import json
import os
import urllib.request
import requests
import shutil
import urllib
import sys
import zipfile
from PySide6.QtCore import QUrl, Qt, QObject, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMessageBox, QProgressDialog

class UpdateChecker(QObject):
    progressChanged = Signal(int)  # Signal for progress updates

    def __init__(self):

        super().__init__()
        self.app_version = self.get_current_version()  # Current version of the application
        self.update_url = "https://raw.githubusercontent.com/lucsky0/conquer_auto_app/master/resources/files/update_info.json"  # URL of the update information file
        self.updated = False

    def get_current_version(self):
        with open('./resources/files/update_info.json') as json_file:
            data = json.load(json_file)
            current_version = data['version']
            return str(current_version)

    def check_for_updates(self):
        try:
            self.app_version = self.get_current_version()
            response = requests.get(self.update_url)
            update_info = response.json()
            latest_version = update_info.get("version")
            download_url = update_info.get("download_url")

            if latest_version and download_url:
                if latest_version > self.app_version:
                    self.prompt_update(download_url)
                else:
                    QMessageBox.information(None, "No Updates", "You are already using the latest version of the application.")
            else:
                print("Error", "Unable to check for updates.")
                QMessageBox.warning(None, "Error", "Unable to check for updates.")
        except Exception as e:
            print("Error", f"Error while checking for updates: {str(e)}")
            QMessageBox.critical(None, "Error", f"Error while checking for updates: {str(e)}")

    def prompt_update(self, download_url):
        reply = QMessageBox.question(None, "Update", "There is a new version of the application available. Do you want to update?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.download_update(download_url)

    def download_update(self, download_url):
        try:
            response = requests.get(download_url, stream=True)
            total_size = response.headers.get('content-length',0)
            progress = QProgressDialog("Downloading update...", None, 0, total_size)
            progress.setWindowTitle("Update Progress")
            progress.setWindowModality(Qt.WindowModal)
            progress.setAutoClose(True)
            progress.setMinimumDuration(0)  # Optional: Set to 0 for immediate display
            progress.setFixedWidth(400)

            # Show the progress dialog
            progress.show()

            with open("update.zip", "wb") as zip_file:
                downloaded_size = 0
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        zip_file.write(chunk)
                        downloaded_size += len(chunk)
                        progress.setValue(downloaded_size)
                        # self.progressChanged.emit(downloaded_size * 100 / total_size)  # Emit progress percentage

            # Close the progress dialog
            # progress.setValue(total_size)

            # Extract the ZIP file
            with zipfile.ZipFile("update.zip", "r") as zip_ref:
                zip_ref.extractall("temp_update_folder")

            # Move the extracted content to the application's directory
            update_folder = os.path.join("temp_update_folder", "conquer_auto_app-master")
            for item in os.listdir(update_folder):
                src = os.path.join(update_folder, item)
                dst = os.path.join(os.getcwd(), item)
                if os.path.isdir(src):
                    shutil.copytree(src, dst, dirs_exist_ok=True)  # Để ghi đè lên thư mục nếu đã tồn tại
                else:
                    if os.path.exists(dst):
                        os.remove(dst)  # Xóa tập tin cũ
                    shutil.copy2(src, dst)  # Ghi đè lên tập tin

            QMessageBox.information(None, "Success", "Update installed successfully.")
            self.updated = True
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error while updating: {str(e)}")
        finally:
            # Remove the ZIP file and temporary folder after updating
            if os.path.exists("update.zip"):
                os.remove("update.zip")
            if os.path.exists("temp_update_folder"):
                shutil.rmtree("temp_update_folder")

            

def on_exit():
    try:
        os.execv("./Update.exe", ["./Update.exe"])
    except Exception as e:
        print(f"Error on exit: {str(e)}")
