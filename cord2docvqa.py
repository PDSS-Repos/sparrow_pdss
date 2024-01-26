from datasets import Dataset
import os, glob
import json

test_d = {"gt_parses": [{"question" : "what is the date in the letter", "answer" : "June 11, 1990"}, {"question" : "what is the date in the letter", "answer" : "June 11,1990"}]}

# data_dict = {}

query_dict = {
    "certificate_of_origin": "Is this document a certificate of origin?",
    "bill_of_lading_number": "What is the bill of lading number?",
    "importer_consignee": "Who is the importer/consignee?",
    "gross_weight_kgs": "What is the gross weight of the shipment in KG",
    "cotton_origin": "What is the origin of the cotton?",
    "net_weight_kgs": "What is the net weight of the shipment in KG",
    "number_of_bales": "What is the number of bales?",
    "invoice_date": "what is the data of shipment?",
}


# path = r'C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-ui\donut\docs\json\key'
# for index, filename in enumerate(glob.glob(os.path.join(path, '*.json'))):
#     with open(os.path.join(os.getcwd(), filename), 'r') as f:
#         data = json.load(f)
#         data_dict[index] = {}
#         data_dict[index]["question"] = "Is this document a certificate of origin?"
#         data_dict[index]["answer"] = data['certificate_of_origin']

#         data_dict[index]["question"] = "What is the bill of lading number?"
#         data_dict[index]["answer"] = data['bill_of_lading_number']


#         print(data)


path = r"C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-ui\donut\docs\json"
for index, filepath in enumerate(glob.glob(os.path.join(path, "*.json"))):
    words = []
    bounding_boxes = []
    query = []
    answers = []
    ground_truth = {"gt_parses": []}
    with open(filepath, "r") as f:
        data = json.load(f)
        for word in data["words"]:
            words.append(word["value"])
            bounding_boxes.append(
                [
                    word["rect"]["x1"],
                    word["rect"]["y1"],
                    word["rect"]["x2"],
                    word["rect"]["y2"],
                ]
            )

            if word["label"]:
                question = query_dict[word["label"]]
                query.append(question)
                answers.append(word["value"])
                ground_truth["gt_parses"].append({"question": question,
                                                   "answer": word["value"]})           


    features = {"query": query,
                "answers": answers,
                "words": words,
                "bounding_boxes": bounding_boxes,
                "ground_truth": ground_truth}
    f.close()

    filename = os.path.basename(filepath)
    export_base_path = r"C:\Users\julian.smidek\GitHub\sparrow_pdss\sparrow-data\donut\docs\models\donut\data\features"
    # write to json
    export_path = os.path.join(
        export_base_path,
                          filename)
    with open(export_path, 'w+') as f:
        json.dump(features, f)

    # filename = os.path.basename(filepath)
    # path_key = os.path.join(path,
    #                         "key",
    #                         filename)

    # with open(path_key, 'r') as f:
    #     data = json.load(f)

    #     print(data)