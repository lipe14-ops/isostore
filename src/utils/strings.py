def sanitize_path_string(path: str) -> str:
    return path + '/' if not path.endswith('/') else path


def sanitize_zipped_filename(filename: str, file_extention: str) -> str:
    filename_no_whitespaces = filename.replace(' ', '')
    return f"{filename_no_whitespaces}{file_extention}"