# simmrr

Simple metric for [MSMARCO](msmarco.org) Conversational Search dataset developed at HopHacks, Fall 2019

simmrr is calculated for final query of each session, given the session's second last query. A simple baseline for the task is Mean Reciprocal Rank (MRR) calculated according to count rank of true next query given the second last query of the session.

```get_vectors.py``` takes as input the train, dev and eval query files available [here](https://msmarco.blob.core.windows.net/msmarcoranking/queries.tar.gz). It processes each query, calls the [MS Gen Encoder API](https://msturing.org) to retrieve its corresponding embeddings and saves them to a csv file.

In ```metric.py```, the first function to be run is ```save_embeddings_from_csv()``` which takes the csv generated in the previous file and converts it into a ```.pkl``` file. This is a one-time operation.

The functions ```create_query_pair_set()``` and ```parse_dev_set()``` are also one-time function calls. They take as input [train sessions](https://msmarco.blob.core.windows.net/conversationalsearch/ann_session_train.tar.gz) and [dev sessions](https://msmarco.blob.core.windows.net/conversationalsearch/ann_session_dev.tar.gz)  respectively and creates several ```.pkl``` files that are used to calculate the final metrics.