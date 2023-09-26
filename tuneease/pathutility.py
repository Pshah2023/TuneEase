import os
import sys
import shutil
import urllib

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
        self.checkpoint_path()
        self.museScore_path()

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
        elif sys.platform == 'darwin':
            directories += [
                '/Applications/MuseScore 4.app/Contents/Resources/bin',
                os.path.join(os.getenv('HOME'), 'bin')
            ]
        elif sys.platform == 'win32':
            directories += [
                r'C:\Program Files\MuseScore 4\bin',
                r'C:\Program Files (x86)\MuseScore 4\bin'
            ]
        for directory in directories:
            if museScore_window_executable:
                path = os.path.join(directory, museScore_window_executable)
                if os.path.exists(path):
                    print(f'Found museScore {path}')
                    return path
            if mscore_mac_executable:
                path = os.path.join(directory, mscore_mac_executable)
                if os.path.exists(path):
                    print(f'Found museScore {path}')
                    return path
            if museScore_linux_executable:
                path = os.path.join(directory, museScore_linux_executable)
                if os.path.exists(path):
                    print(f'Found museScore {path}')
                    return path
        print("Looking for a MuseScore installation. If on Ubuntu, download the below link and place it in the below location")
        print("https://cdn.jsdelivr.net/musescore/v4.1.1/MuseScore-4.1.1.232071203-x86_64.AppImage")
        print(r"C:\Users\ppsha\Documents\Github\TuneEase\temp\MuseScore.AppImage")
        print("On Windows and macOS, install MuseScore through the website: [https://musescore.org/en](https://musescore.org/en).")
        print("For Windows, the attempts made to find it automatically from common locations are tested and working.")
        print("For macOS, the attempts have not been tested but are implemented. Please send an issue to change this message if it works on macOS.")
        raise FileNotFoundError('MuseScore installation not found. If necessary, use the flag --museScore_path <museScore_path>')

    def checkpoint_path(self):
        if not os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checkpoint.pth")):
            def download_progress_bar(blocknum, blocksize, totalsize):
                downloaded = blocknum * blocksize
                percent_complete = (downloaded / totalsize) * 100
                print(f'Downloaded {percent_complete:.2f}% from {totalsize/1073741824}', end='\r')
            print("If this is downloading too slowly, you should use your browser with the below link:")
            file_url = 'https://onedrive.live.com/download?resid=CF5CD532C7BDCDB1%212273&authkey=!AOXAcumYZkpQjn4"' # Do keep the '"' at the end
            print(file_url, "\nThen, move it this spot:")
            filename = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checkpoint.pth")
            print(filename)
            urllib.request.urlretrieve(file_url, filename, reporthook=download_progress_bar)
            print(f'Downloaded {filename}.')
        else:
            print(f'Found {os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checkpoint.pth")}.')
            return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "checkpoint.pth")