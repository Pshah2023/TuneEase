import os
import sys
import shutil
import requests

class PathUtility:
    """
    A utility class for handling file paths and locating the MuseScore executable's path.

    Attributes:
        current_file_path (str): The absolute path of the current file.

    Methods:
        __init__(self):
        project_directory(self):
        museScore_path(self):
        
    Example:
        >>> path_util = PathUtility()
        >>> path_util.current_file_path
        /path/to/the/file
    """
    
    def __init__(self):
        self.current_file_path = os.path.abspath(__file__)
        self.checkpoint()

    def project_directory(self):
        """
        Get the path to the project directory.

        Args:
            None

        Returns:
            str: The path to the project directory.

        Example:
            >>> path_util = PathUtility()
            >>> project_dir = path_util.project_directory()
        """
        return os.path.dirname(os.path.dirname(self.current_file_path))

    def museScore_path(self):
        """
        Locate and return the path to the MuseScore executable.

        Args:
            None

        Returns:
            str: The path to the MuseScore executable.

        Raises:
            FileNotFoundError: If MuseScore installation is not found.

        Example:
            >>> path_util = PathUtility()
            >>> muse_score_path = path_util.museScore_path()
        
        Notes:
            - On Linux, this method searches for MuseScore in the 'temp' directory within the project directory.
            - On macOS, it checks specific directories, including the standard installation path and the user's 'bin' directory.
            - On Windows, it searches in common installation paths for both 32-bit and 64-bit versions.
        """
        mscore_mac_executable = 'mscore' if sys.platform != 'win32' else 'mscore.exe'
        museScore_window_executable = 'MuseScore' if sys.platform != 'win32' else 'MuseScore4.exe'
        museScore_linux_executable = 'MuseScore.AppImage' if sys.platform.startswith('linux') else None
        path = shutil.which(mscore_mac_executable)
        if path:
            return path
        path = shutil.which(museScore_window_executable)
        if path:
            return path
        directories = list()
        if sys.platform.startswith('linux'):
            directories += [
                os.path.join(self.project_directory(), 'temp')
            ]
        if sys.platform == 'darwin':
            directories += [
                '/Applications/MuseScore 4.app/Contents/Resources/bin',
                os.path.join(os.getenv('HOME'), 'bin')
            ]
        if sys.platform == 'win32':
            directories += [
                r'C:\Program Files\MuseScore 4\bin',
                r'C:\Program Files (x86)\MuseScore 4\bin'
            ]
        for directory in directories:
            if museScore_window_executable:
                path = os.path.join(directory, museScore_window_executable)
                if os.path.exists(path):
                    return path
            if mscore_mac_executable:
                path = os.path.join(directory, mscore_mac_executable)
                if os.path.exists(path):
                    return path
            if museScore_linux_executable:
                path = os.path.join(directory, museScore_linux_executable)
                if os.path.exists(path):
                    return path
        raise FileNotFoundError('MuseScore installation not found. Use the flag --museScore_path')

    def checkpoint(self):
        if not os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checkpoint.pth")):
            filename = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checkpoint.pth")
            file_url = 'https://github.com/Pshah2023/TuneEase/releases/download/0.1.0/checkpoint.pth'
            response = requests.get(file_url, stream=True)
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            file.write(chunk)
                print(f'Downloaded {filename} successfully.')
            else:
                print(f'Failed to download {file_url}. Status code: {response.status_code}')