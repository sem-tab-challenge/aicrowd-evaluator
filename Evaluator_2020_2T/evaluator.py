#!/usr/bin/env python
from datetime import datetime

try:
    from .CEA_Evaluator import CEA_Evaluator
    from .CTA_Evaluator import CTA_Evaluator
except ImportError as e:
    from CEA_Evaluator import CEA_Evaluator
    from CTA_Evaluator import CTA_Evaluator


class TableAnnotationEvaluator:
  def __init__(self, answer_file_path, task_name, round=1):
    """
    `round` : Holds the round for which the evaluation is being done. 
    can be 1, 2...upto the number of rounds the challenge has.
    Different rounds will mostly have different ground truth files.

    `task_name` has to be one of "CEA", "CTA"
    """
    self.answer_file_path = answer_file_path
    self.round = round
    self.task_name = task_name
    valid_task_names = ["CEA", "CTA"]
    assert self.task_name in valid_task_names, \
        "task_name has to be one of %s ".format(",".join(valid_task_names))

    if self.task_name == "CEA":
        self.evaluator = CEA_Evaluator(
                self.answer_file_path,
                round=self.round
                )
    elif self.task_name == "CTA":
        self.evaluator = CTA_Evaluator(
                self.answer_file_path,
                round=self.round
                )

  def _evaluate(self, client_payload, _context={}):
    return self.evaluator._evaluate(
            client_payload,
            _context
    )


if __name__ == "__main__":

    #############################################################################
    # Test CEA Task
    #############################################################################
    # Lets assume the the ground_truth is a CSV file
    # and is present at data/ground_truth.csv
    # and a sample submission is present at data/sample_submission.csv
    answer_file_path = "DataSets/Data_CEA/CEA_Round3_gt.csv"
    _client_payload = {}
    _client_payload["submission_file_path"] = "DataSets/Data_CEA/CEA_Round3_sub0.csv"

    _client_payload["aicrowd_submission_id"] = 1123
    _client_payload["aicrowd_participant_id"] = 1234
    
    # Instaiate a dummy context
    _context = {}
    # Instantiate an evaluator
    cea_start = datetime.now()
    aicrowd_evaluator = TableAnnotationEvaluator(answer_file_path, "CEA")
    # Evaluate
    result = aicrowd_evaluator._evaluate(_client_payload, _context)
    cea_end = datetime.now()
    print(result)
    print('CEA costs time (seconds): ', (cea_end-cea_start))


    #############################################################################
    # Test CTA Task
    #############################################################################
    # Lets assume the the ground_truth is a CSV file
    # and is present at data/ground_truth.csv
    # and a sample submission is present at data/sample_submission.csv
    answer_file_path = "DataSets/Data_CTA/CTA_Round3_gt.csv"
    _client_payload = {}
    _client_payload["submission_file_path"] = "DataSets/Data_CTA/CTA_Round3_sub0.csv"

    _client_payload["aicrowd_submission_id"] = 1123
    _client_payload["aicrowd_participant_id"] = 1234
    
    # Instaiate a dummy context
    _context = {}
    # Instantiate an evaluator
    cta_start = datetime.now()
    aicrowd_evaluator = TableAnnotationEvaluator(answer_file_path, "CTA")
    # Evaluate
    result = aicrowd_evaluator._evaluate(_client_payload, _context)
    cta_end = datetime.now()
    print(result)
    print('CTA costs costs time (seconds): ', (cta_end-cta_start))
