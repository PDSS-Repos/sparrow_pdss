from pathlib import Path
import json
import cv2
import os


class DonutMetadataGenerator:
    def generate(self, data_dir, files_list, split):
        base_img_dir_path = Path(data_dir).joinpath("key/img")
        img_dir_path = Path(data_dir).joinpath("img/" + split)

        metadata_list = []

        for file_name in files_list:
            file_name_img = base_img_dir_path.joinpath(f"{file_name.stem}.jpg")
            img = cv2.imread(str(file_name_img))
            cv2.imwrite(str(img_dir_path.joinpath(f"{file_name.stem}.jpg")), img)

            with open(file_name, "r") as json_file:
                data = json.load(json_file)
                line = {"gt_parse": data}
                text = json.dumps(line)
                json_file.close()

            _filename = os.path.basename(file_name)
            _file_path = Path(file_name).parent.parent
            _features_path = os.path.join(
                                _file_path,
                                "features",
                                _filename)
            with open(_features_path, "r") as json_file:
                features = json.load(json_file)
                text = json.dumps(features['ground_truth'])
                json_file.close()   

                if img_dir_path.joinpath(f"{file_name.stem}.jpg").is_file():
                    metadata_list.append({
                        "ground_truth": text,
                        "query": features["query"], 
                        "answers": features["answers"],
                        "words": features["words"], 
                        "bounding_boxes": features["bounding_boxes"],
                        "file_name": f"{file_name.stem}.jpg"
                    })

        with open(Path(img_dir_path).joinpath("metadata.jsonl"), "w") as outfile:
            for entry in metadata_list:
                json.dump(entry, outfile)
                outfile.write("\n")