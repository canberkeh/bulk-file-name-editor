import os
import datetime


def get_create_date(file):
    creation_time = os.path.getmtime(file)
    print(f"Creation time: {datetime.datetime.fromtimestamp(creation_time).strftime('%Y:%m:%d %H:%M:%S')} for the file: {file}")
    return datetime.datetime.fromtimestamp(creation_time).strftime("%Y:%m:%d %H:%M:%S")


def get_file_extension(file):
    return file.split(".")[-1]


def rename_files(files, appendix):
    for i, file in enumerate(files):
        file_extension = get_file_extension(file)
        new_file_name = f"{appendix}-{i+1}.{file_extension}"
        os.rename(file, os.path.join(files_path, new_file_name))


if __name__ == "__main__":
    files_path = ".\\images"  # Set files path here.
    appendix = "images"  # Set appendix here.

    files = [os.path.join(files_path, file) for file in os.listdir(files_path)]
    for file in files:
        date_taken = get_create_date(file)
    rename_files(files, appendix)
    print("Files renamed successfully.")
