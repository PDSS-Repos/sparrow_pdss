from tools.donut.dataset_uploader import DonutDatasetUploader
from huggingface_hub.hf_api import HfFolder

def main():
    HfFolder.save_token('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')

    dataset_uploader = DonutDatasetUploader()
    dataset_uploader.upload('sparrow-data/donut/docs/models/donut/data', "juliansmidek/donut_test")

if __name__ == '__main__':
    main()