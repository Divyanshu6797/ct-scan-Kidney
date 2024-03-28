from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger
import os



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        print("new stuff starting")
        os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Divyanshu6797/ct-scan-Kidney.mlflow"
        print("new stuff ending")
        os.environ["MLFLOW_TRACKING_USERNAME"]="Divyanshu6797"
        os.environ["MLFLOW_TRACKING_PASSWORD"]="118413c2287ead00ba2ae4a3d176de2053c8ffce"
        print("mlflow log starting")
        evaluation.log_into_mlflow()
        print("mlflow log ended")




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            
            