from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

# Convert predicted probabilities to binary labels
y_pred_binary = (np.array(y_pred) > 0.5).astype(int)
y_test=y_test.reshape(-1,1)

# Calculate classification report
report = classification_report(y_test, y_pred_binary)
print('Classification Report:')
print(report)

# Calculate confusion matrix
confusion_mat = confusion_matrix(y_test, y_pred_binary)
print('Confusion Matrix:', confusion_mat)
print('Accuracy:',accuracy_score(y_test,y_pred_binary))