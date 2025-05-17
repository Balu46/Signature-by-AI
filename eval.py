# You can import any module, model class, etc.
# We will import the `load_and_predict()` function below to assess your assignment.


def load_and_predict(directory, model_file):
    # The `directory` argument is a folder with the same structure as the provided dataset. Example:
    # /path/to/some/signatures
    #  |_human
    #     |_ 001g01.csv
    #     |_ 001g02.csv
    #     |_ ...
    #  |_gan
    #     |_ 001g01.csv
    #     |_ 001g02.csv
    #     |_ ...
    #  |_sdt
    #     |_ 001g01.csv
    #     |_ 001g02.csv
    #     |_ ...
    #  |_vae
    #     |_ 001g01.csv
    #     |_ 001g02.csv
    #     |_ ...
    #
    # The `model_file` argument is a trained model file, in `.pth` format.
    #
    # This function must implement the following steps:
    # 1. Read the data from the provided directory.
    # 2. Prepare the data according to whatever preprocessing pipeline was used during model training.
    # 3. Load the model checkpoint.
    # 4. Query the model with the data in order to get the predicted class probabilities.
    # 5. Convert probabilities to labels, like in the other assignment (but now there are 4 classes instead of 2).
    # 6. Return a dictionary where keys are absolute file paths and values are the predicted labels for each file. Example:
    # `{ '/path/to/some/signatures/human/001g01.csv': 0, '/path/to/some/signatures/sdt/001g02.csv': 2, ... }`.
    return labels_dict

