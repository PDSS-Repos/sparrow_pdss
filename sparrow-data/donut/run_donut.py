# from tools.donut.metadata_generator import DonutMetadataGenerator
from tools.donut.metadata_generator_docvqa import DonutMetadataGenerator

from tools.donut.dataset_generator import DonutDatasetGenerator
from pathlib import Path
import os
import shutil


def main():
    # define the source and destination directory
    # src_dir_json = 'sparrow-ui/donut/docs/json/key'
    # src_dir_img = 'sparrow-ui/donut/docs/images'
    # dst_dir_json = 'sparrow-data/donut/docs/models/donut/data/key'
    # dst_dir_img = 'sparrow-data/donut/docs/models/donut/data/key/img'
    # src_dir_json = 'sparrow-ui/donut/docs/json/key'
    # src_dir_img = 'sparrow-ui/donut/docs/images'
    # dst_dir_json = 'sparrow-data/donut/docs/models/donut/data/key'
    # dst_dir_img = 'sparrow-data/donut/docs/models/donut/data/key/img'
    src_dir_json = r'C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-ui/donut/docs/json/key'
    src_dir_img = r'C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-ui/donut/docs/images'
    dst_dir_json = r'C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-data/donut/docs/models/donut/data/key'
    dst_dir_img = r'C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-data/donut/docs/models/donut/data/key/img'

    # copy JSON files from src to dst
    files = os.listdir(src_dir_json)
    for f in files:
        src_file = os.path.join(src_dir_json, f)
        dst_file = os.path.join(dst_dir_json, f)
        shutil.copy(src_file, dst_file)

    # copy images from src to dst
    files = os.listdir(src_dir_img)
    for f in files:
        # copy img file, only if file with sane name exists in dst_dir_json
        if os.path.isfile(os.path.join(dst_dir_json, f[:-4] + '.json')):
            src_file = os.path.join(src_dir_img, f)
            dst_file = os.path.join(dst_dir_img, f)
            shutil.copy(src_file, dst_file)

    # Convert to Donut format
    base_path = r'C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-data/donut/docs/models/donut/data'
    data_dir_path = Path(base_path).joinpath("key")
    files = data_dir_path.glob("*.json")
    files_list = [file for file in files]
    # split files_list array into 3 parts, 85% train, 10% validation, 5% test
    train_files_list = files_list[:int(len(files_list) * 0.85)]
    # train_files_list = files_list[:int(len(files_list) * 1)]
    # train_files_list = files_list[:int(len(files_list) * 1)]
    print("Train set size:", len(train_files_list))
    # print(train_files_list)
    validation_files_list = files_list[int(len(files_list) * 0.85):int(len(files_list) * 0.95)]
    # validation_files_list = train_files_list
    print("Validation set size:", len(validation_files_list))
    test_files_list = files_list[int(len(files_list) * 0.95):]
    # test_files_list = train_files_list
    print("Test set size:", len(test_files_list))

    metadata_generator = DonutMetadataGenerator()
    metadata_generator.generate(base_path, train_files_list, "train")
    metadata_generator.generate(base_path, validation_files_list, "validation")
    metadata_generator.generate(base_path, test_files_list, "test")

    # Generate dataset
    dataset_generator = DonutDatasetGenerator()
    dataset_generator.generate(base_path)

if __name__ == '__main__':
    main()