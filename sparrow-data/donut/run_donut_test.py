from tools.donut.dataset_tester import DonutDatasetTester
from huggingface_hub.hf_api import HfFolder

def main():
    HfFolder.save_token('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')

    dataset_tester = DonutDatasetTester()
    dataset_tester.test("juliansmidek/donut_test")

if __name__ == '__main__':
    main()