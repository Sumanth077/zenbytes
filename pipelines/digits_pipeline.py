from zenml.pipelines import pipeline


@pipeline
def digits_pipeline(importer, trainer, evaluator):
    """Simple data loading -> train -> test pipeline"""
    X_train, X_test, y_train, y_test = importer()
    model = trainer(X_train=X_train, y_train=y_train)
    evaluator(X_test=X_test, y_test=y_test, model=model)
