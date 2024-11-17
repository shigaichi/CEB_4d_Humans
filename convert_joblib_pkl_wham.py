import joblib
import pickle
import os

from .utils import *


logger = get_addon_logger()


def convert_joblib_pkl_wham():
    path_addon = os.path.dirname(os.path.abspath(__file__))
    # base_file = os.path.join(path_addon,'4D-Humans-main','outputs','results')
    base_file = os.path.join(path_addon, "WHAM", "output", "demo", "video")
    file = os.path.join(base_file, "wham_output_google_colab.pkl")

    # file_converted = os.path.join(base_file,'demo_video_converted.pkl')
    file_converted = os.path.join(base_file, "wham_output.pickle")
    logger.info(
        f"start convert_joblib_pkl_wham. base_file: {base_file}. file_converted: {file_converted}"
    )
    results = joblib.load(file)

    with open(file_converted, "wb") as handle:
        pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # with open('filename.pickle', 'rb') as handle:
    #    b = pickle.load(handle)


if __name__ == "__main__":
    convert_joblib_pkl_wham()
