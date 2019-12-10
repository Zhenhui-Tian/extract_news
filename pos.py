# tagging in order to find the pattern such as "xx thinks .."
'''
start server
java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -serverProperties StanfordCoreNLP-chinese.properties -port 9000 -timeout 15000
'''
from pyltp import Postagger
import pickle


def cut_sentence(article):

    return
def store_state(file_name, list):
    fileObject = open(file_name, 'wb')
    pickle.dump(list, fileObject)
    print('stored .. ')
    fileObject.close()


fileobject = open(r'C:\Users\Terrence\Documents\NLP\extract_news\temp_data\words.pickle', 'rb')
sentences = pickle.load(fileobject)

pdir = r'C:\Users\Terrence\Documents\NLP\NLP_tools\ltp_data_v3.4.0\ltp_data_v3.4.0\pos.model'
pos = Postagger()
pos.load(pdir)
pos_dict = {'sentence': [], 'tags': []}
for sen in sentences:
    postags = list(pos.postag(sen))
    pos_dict['sentence'].append(sen)
    pos_dict['tags'].append(postags)
store_state(r'C:\Users\Terrence\Documents\NLP\extract_news\temp_data\\pos.pickle', pos_dict)


test_sentence =






