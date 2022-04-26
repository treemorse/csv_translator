IAM_TOKEN = 't1.9euelZqPi82QnYqVjc3IlZaWkp3Mlu3rnpWam5SZlsyOlJvIi8qNkcyOyYnl8_dvIWBs-e87Ez4L_t3z9y9QXWz57zsTPgv-.3F9XIAFcqTZ-cLjr57wjzpB-CopPsXjCh_znhGLFngizEsFu7KU0goL0YsiyGpErBwembmlGm_j4_olv_0jiBg'
folder_id = 'b1gk67ai46eieplnbj03'

def configure(texts, language):
    target_language = language
    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }
    return (body, headers)