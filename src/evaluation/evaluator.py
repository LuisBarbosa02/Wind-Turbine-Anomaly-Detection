# Import libraries
from sklearn.metrics import classification_report

# Make evaluation
def make_evaluation(preprocessor, model, X_test, y_test):
	"""
	Function to evaluate the performance of the model.
	:return: Dict of all metrics.
	"""
	# Make prediction
	y_pred = model.predict(preprocessor.transform(X_test))

	# Get classification metrics
	report_dict = classification_report(y_test, y_pred, output_dict=True)

	# Arrange metrics
	metrics = {}
	for k_1, v_1 in report_dict.items():
		try:
			for k_2, v_2 in v_1.items():
				metrics[f"{k_1}_{k_2}"] = v_2
		except:
			metrics[k_1] = v_1

	return metrics