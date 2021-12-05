class SentenceScorer:
  def __init__(self, tf_idf_vectorizer, score_classifier_model):
    self.tf_idf_vectorizer = tf_idf_vectorizer
    self.score_classifier_model = score_classifier_model

  def get_scores(self, proc_comment_texts):
    proc_comment_texts_tf = self.tf_idf_vectorizer.transform(proc_comment_texts)
    return [row[1] for row in self.score_classifier_model.predict_proba(proc_comment_texts_tf)]

