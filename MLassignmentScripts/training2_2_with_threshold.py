<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> #Detailed Report</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> from sklearn.metrics import classification_report</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> print(classification_report(y_cv, y_cv_pred))</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> # Making the Confusion Matrix</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> from sklearn.metrics import confusion_matrix</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> cm = confusion_matrix(y_cv, y_cv_pred)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> print(cm)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> #Roc Analization</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> from sklearn.metrics import roc_curve</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> from sklearn.metrics import roc_auc_score</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_cv_pred_pred=classifier.predict(X_cv)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> fpr,tpr,threshold=roc_curve(y_cv,y_cv_pred)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> auc = roc_auc_score(y_cv, y_cv_pred)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> print('AUC: %.3f' % auc)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> plt.plot(fpr, tpr)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> plt.title(&quot;ROC Curve&quot;)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> plt.xlabel(&quot;False Positive Rate&quot;)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> plt.ylabel(&quot;True Positive Rate&quot;)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> plt.show()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">              precision    recall  f1-score   support</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">           0       1.00      1.00      1.00       534</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">           1       1.00      1.00      1.00       536</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    accuracy                           1.00      1070</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">   macro avg       1.00      1.00      1.00      1070</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">weighted avg       1.00      1.00      1.00      1070</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">[[533   1]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> [  0 536]]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">AUC: 0.999</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
wAAAAABJRU5ErkJggg==
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">17</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">18</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-18-24c2ba807431&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">1</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred.prediction.value_counts()</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'numpy.ndarray' object has no attribute 'prediction'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">19</span><span style=" color:#00ff00;">]:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">20</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;&lt;ipython-input-20-24c2ba807431&gt;&quot;</span>, line <span style=" color:#006400;">1</span>, in <span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    y_pred.prediction.value_counts()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\generic.py&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">5274</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">__getattr__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    return object.__getattribute__(self, name)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'DataFrame' object has no attribute 'prediction'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">21</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">22</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">23</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">24</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">25</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">25</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1    10783</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0     1091</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">26</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> threshold=0.6152</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_pred [:,0] = (predicted [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_pred [:,1] = (predicted [:,1] &gt;= threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-26-8501dda4dd34&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">3</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred [:,0] = (predicted [:,0] &lt; threshold).astype('int')</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">NameError:</span> name 'predicted' is not defined</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">27</span><span style=" color:#00ff00;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> threshold=0.6152</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">    ...:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">28</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">29</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">30</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">31</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">32</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">32</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1.0    11872</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0.0        2</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">33</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">34</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">35</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">36</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-36-4f2dcae51a2c&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">1</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred.insert(0,'ID',ID)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'numpy.ndarray' object has no attribute 'insert'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">37</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-37-08bcc622b877&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">1</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred=y_pred.rename(columns={0: 'prediction'})</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'numpy.ndarray' object has no attribute 'rename'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">38</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-38-4206d66c55fd&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">1</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred.set_index('ID', inplace=True)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'numpy.ndarray' object has no attribute 'set_index'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">39</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">40</span><span style=" color:#00ff00;">]:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">41</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">42</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">43</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">44</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">45</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">45</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1    10783</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0     1091</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">46</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">47</span><span style=" color:#00ff00;">]:</span> threshold=0.38</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">48</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">49</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">50</span><span style=" color:#00ff00;">]:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">51</span><span style=" color:#00ff00;">]:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">52</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">53</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">54</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">55</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">56</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">56</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0.0    5946</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1.0    5928</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">57</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">58</span><span style=" color:#00ff00;">]:</span> threshold=0.45</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">59</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">60</span><span style=" color:#00ff00;">]:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">61</span><span style=" color:#00ff00;">]:</span> #Exporting the results as csv file:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">62</span><span style=" color:#00ff00;">]:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">63</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">64</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">65</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">66</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">67</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">67</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1.0    8906</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0.0    2968</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">68</span><span style=" color:#00ff00;">]:</span> threshold=0.3</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">69</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;&lt;ipython-input-69-602be53fa4ec&gt;&quot;</span>, line <span style=" color:#006400;">1</span>, in <span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\frame.py&quot;</span>, line <span style=" color:#006400;">2800</span>, in <span style=" color:#9400d3;">__getitem__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    indexer = self.columns.get_loc(key)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\indexes\base.py&quot;</span>, line <span style=" color:#006400;">2646</span>, in <span style=" color:#9400d3;">get_loc</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return self._engine.get_loc(key)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;pandas\_libs\index.pyx&quot;</span>, line <span style=" color:#006400;">111</span>, in <span style=" color:#9400d3;">pandas._libs.index.IndexEngine.get_loc</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;pandas\_libs\index.pyx&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">116</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">pandas._libs.index.IndexEngine.get_loc</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">TypeError:</span> '(slice(None, None, None), 0)' is an invalid key</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">70</span><span style=" color:#00ff00;">]:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;&lt;ipython-input-70-a8a40d7addae&gt;&quot;</span>, line <span style=" color:#006400;">1</span>, in <span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\frame.py&quot;</span>, line <span style=" color:#006400;">2800</span>, in <span style=" color:#9400d3;">__getitem__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    indexer = self.columns.get_loc(key)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\indexes\base.py&quot;</span>, line <span style=" color:#006400;">2646</span>, in <span style=" color:#9400d3;">get_loc</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return self._engine.get_loc(key)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;pandas\_libs\index.pyx&quot;</span>, line <span style=" color:#006400;">111</span>, in <span style=" color:#9400d3;">pandas._libs.index.IndexEngine.get_loc</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;pandas\_libs\index.pyx&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">116</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">pandas._libs.index.IndexEngine.get_loc</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">TypeError:</span> '(slice(None, None, None), 1)' is an invalid key</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">71</span><span style=" color:#00ff00;">]:</span> #Exporting the results as csv file:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">72</span><span style=" color:#00ff00;">]:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">73</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">74</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">75</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">76</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">77</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">77</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1.0    8906</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0.0    2968</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">78</span><span style=" color:#00ff00;">]:</span> y_pred.to_csv('y_pred_upsampled_RandomForest2_with_threshold_.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">79</span><span style=" color:#00ff00;">]:</span> y_pred.drop('1', axis=1)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;&lt;ipython-input-79-2d46c6fab709&gt;&quot;</span>, line <span style=" color:#006400;">1</span>, in <span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    y_pred.drop('1', axis=1)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\frame.py&quot;</span>, line <span style=" color:#006400;">3997</span>, in <span style=" color:#9400d3;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    errors=errors,</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\generic.py&quot;</span>, line <span style=" color:#006400;">3936</span>, in <span style=" color:#9400d3;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    obj = obj._drop_axis(labels, axis, level=level, errors=errors)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\generic.py&quot;</span>, line <span style=" color:#006400;">3970</span>, in <span style=" color:#9400d3;">_drop_axis</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    new_axis = axis.drop(labels, errors=errors)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\indexes\base.py&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">5017</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    raise KeyError(f&quot;{labels[mask]} not found in axis&quot;)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">KeyError:</span> &quot;['1'] not found in axis&quot;</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">80</span><span style=" color:#00ff00;">]:</span> y_pred.drop(['1'], axis=1)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;&lt;ipython-input-80-0aac3ecb1239&gt;&quot;</span>, line <span style=" color:#006400;">1</span>, in <span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    y_pred.drop(['1'], axis=1)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\frame.py&quot;</span>, line <span style=" color:#006400;">3997</span>, in <span style=" color:#9400d3;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    errors=errors,</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\generic.py&quot;</span>, line <span style=" color:#006400;">3936</span>, in <span style=" color:#9400d3;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    obj = obj._drop_axis(labels, axis, level=level, errors=errors)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\generic.py&quot;</span>, line <span style=" color:#006400;">3970</span>, in <span style=" color:#9400d3;">_drop_axis</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    new_axis = axis.drop(labels, errors=errors)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\indexes\base.py&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">5017</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    raise KeyError(f&quot;{labels[mask]} not found in axis&quot;)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">KeyError:</span> &quot;['1'] not found in axis&quot;</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">81</span><span style=" color:#00ff00;">]:</span> y_pred.drop(columns=['1'])</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;&lt;ipython-input-81-8fe29d810b38&gt;&quot;</span>, line <span style=" color:#006400;">1</span>, in <span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    y_pred.drop(columns=['1'])</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\frame.py&quot;</span>, line <span style=" color:#006400;">3997</span>, in <span style=" color:#9400d3;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    errors=errors,</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\generic.py&quot;</span>, line <span style=" color:#006400;">3936</span>, in <span style=" color:#9400d3;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    obj = obj._drop_axis(labels, axis, level=level, errors=errors)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#006400;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\generic.py&quot;</span>, line <span style=" color:#006400;">3970</span>, in <span style=" color:#9400d3;">_drop_axis</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    new_axis = axis.drop(labels, errors=errors)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;C:\Users\Ege\Anaconda3\lib\site-packages\pandas\core\indexes\base.py&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">5017</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">drop</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    raise KeyError(f&quot;{labels[mask]} not found in axis&quot;)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">KeyError:</span> &quot;['1'] not found in axis&quot;</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">82</span><span style=" color:#00ff00;">]:</span> y_pred.drop(columns=[1])</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">82</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">       prediction</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">ID               </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1             0.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">2             0.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">3             1.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">4             0.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">5             1.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">...           ...</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">11870         1.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">11871         1.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">11872         0.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">11873         1.0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">11874         1.0</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">[11874 rows x 1 columns]</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">83</span><span style=" color:#00ff00;">]:</span> y_pred.drop(columns=[1], inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">84</span><span style=" color:#00ff00;">]:</span> y_pred.to_csv('y_pred_upsampled_RandomForest2_with_threshold_30.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">85</span><span style=" color:#00ff00;">]:</span> X_test= pd.read_csv(Path('brighton-a-memorable-city/testing.csv'), index_col=0)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">86</span><span style=" color:#00ff00;">]:</span> # Predicting the Test set results</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">87</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">88</span><span style=" color:#00ff00;">]:</span> threshold=0.3</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">89</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">90</span><span style=" color:#00ff00;">]:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">91</span><span style=" color:#00ff00;">]:</span> y_pred.drop(columns=[1], inplace=True)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-91-2b444f56cac1&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">1</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred.drop(columns=[1], inplace=True)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'numpy.ndarray' object has no attribute 'drop'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">92</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-92-24c2ba807431&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">1</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred.prediction.value_counts()</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'numpy.ndarray' object has no attribute 'prediction'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">93</span><span style=" color:#00ff00;">]:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">94</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">95</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">96</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">97</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">98</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">98</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0.0    8653</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1.0    3221</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">99</span><span style=" color:#00ff00;">]:</span> y_pred.drop(columns=[1], inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">100</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> threshold=0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">101</span><span style=" color:#00ff00;">]:</span> y_pred = y_pred.astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">102</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> threshold=0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">103</span><span style=" color:#00ff00;">]:</span> y_pred = y_pred.astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">104</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">105</span><span style=" color:#00ff00;">]:</span> threshold=0.3</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">106</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">107</span><span style=" color:#00ff00;">]:</span> y_pred.drop(columns=[1], inplace=True)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#00ffff;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ffff;">  File </span><span style=" color:#00ff00;">&quot;&lt;ipython-input-107-2b444f56cac1&gt;&quot;</span><span style=" color:#00ffff;">, line </span><span style=" color:#00ff00;">1</span><span style=" color:#00ffff;">, in </span><span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ffff00;">    y_pred.drop(columns=[1], inplace=True)</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">AttributeError:</span> 'numpy.ndarray' object has no attribute 'drop'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">108</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> threshold=0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">109</span><span style=" color:#00ff00;">]:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">110</span><span style=" color:#00ff00;">]:</span> y_pred = y_pred.astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">111</span><span style=" color:#00ff00;">]:</span> y_pred.drop(columns=[1], inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">112</span><span style=" color:#00ff00;">]:</span> ID=X_test.index.values</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">113</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">114</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">115</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> threshold=0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred=pd.DataFrame(data=y_pred)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred = y_pred.astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred.drop(columns=[1], inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">116</span><span style=" color:#00ff00;">]:</span> y_pred.insert(0,'ID',ID)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">117</span><span style=" color:#00ff00;">]:</span> y_pred=y_pred.rename(columns={0: 'prediction'})</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">118</span><span style=" color:#00ff00;">]:</span> y_pred.set_index('ID', inplace=True)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">119</span><span style=" color:#00ff00;">]:</span> y_pred.prediction.value_counts()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#ff0000;">Out[</span><span style=" font-weight:600; color:#ff0000;">119</span><span style=" color:#ff0000;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">0    8653</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">1    3221</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Name: prediction, dtype: int64</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">120</span><span style=" color:#00ff00;">]:</span> y_pred.to_csv('y_pred_upsampled_RandomForest2_with_threshold_30.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">121</span><span style=" color:#00ff00;">]:</span> y_pred1 = classifier.predict_proba(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">122</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">123</span><span style=" color:#00ff00;">]:</span> threshold=0.3</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">124</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">125</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">126</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">127</span><span style=" color:#00ff00;">]:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> threshold=0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,1] = (y_pred [:,0] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">128</span><span style=" color:#00ff00;">]:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,1] = (y_pred [:,1] &gt;= threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">129</span><span style=" color:#00ff00;">]:</span> y_pred = classifier.predict_proba(X_test)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> threshold=0.3</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">     ...:</span> y_pred [:,0] = (y_pred [:,0] &lt; threshold).astype('int')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#00ff00;">In [</span><span style=" font-weight:600; color:#00ff00;">130</span><span style=" color:#00ff00;">]:</span> </p></body></html>