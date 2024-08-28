import pandas as pd
from pycaret.classification import *

# Load the data
data = pd.read_csv('diabetes.csv')

# Initialize setup
setup(data, target='Outcome')
#
# # Create the model
model = create_model('rf', bootstrap=True, ccp_alpha=0.0, class_weight=None,
                     criterion='gini', max_depth=None, max_features='sqrt',
                     max_leaf_nodes=None, max_samples=None,
                     min_impurity_decrease=0.0, min_samples_leaf=1,
                     min_samples_split=2, min_weight_fraction_leaf=0.0,
                     n_estimators=100, n_jobs=-1, oob_score=False,
                     random_state=1595, verbose=True, warm_start=False)

# # Evaluate the model
# evaluate_model(model)
#
# # Interpret the model
# interpret_model(model)
#
# # Display the confusion matrix
# plot_model(model, plot='confusion_matrix', save=True)
#
# # Generate a prediction error plot
# plot_model(model, plot='error', save=True)
#
# # Visualize the learning curve
# plot_model(model, plot='learning', save=True)
#
# # Examine the residual plot
# plot_model(model, plot='residuals', save=True)
#
# # Print the important features
# print(get_config('rf')['variable_importances'])
